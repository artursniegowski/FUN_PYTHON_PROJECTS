#This class is responsible for talking to the Flight Search API.
import requests
from flight_data import FlightData

class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """
    def __init__(self, tequila_api_end_point: str, tequila_api_key: str) -> None:
        self.tequila_api_end_point = tequila_api_end_point
        self.api_tequila_auth_header = {
            'apikey': tequila_api_key,
        }

    def get_destination_code(self, city_name: str) -> str:
        """
        returns the IATA Code for the given city name
        """
        data_to_search = {
            'term': city_name,
            'locale': 'en-US',
            'location_types': 'city',
            'limit': 10,
            'sort': 'name',
        }

        respond_flight_search = requests.get(url=f"{self.tequila_api_end_point}/locations/query",
                                            params=data_to_search,
                                            headers=self.api_tequila_auth_header)
        respond_flight_search.raise_for_status() # check for errors
        return respond_flight_search.json()['locations'][0]['code']


    def check_flights(self, origin_city_code, destination_city_code, \
        from_time, to_time) -> FlightData :
        """
        returns a FlightData object representing the the flight data for 

        
        we're looking only for direct flights, that leave anytime between 
        tomorrow and in 6 months (6x30days) time. We're also looking for 
        round trips that return between 7 and 28 days in length. 
        The currency of the price we get back should be in GBP.
        """
        CURRENCY_CODE = 'PLN'

        # 01/04/2021 # dd/mm/yyyy - date
        # data for the api as aprameters
        flight_data_search = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"), 
            'date_to': to_time.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'adults': 1,
            'children': 0,
            'infants': 0,
            'curr': CURRENCY_CODE,
        }

        
        reposnd_fligt_data = requests.get(url=f"{self.tequila_api_end_point}/v2/search",
                                            params=flight_data_search,
                                            headers=self.api_tequila_auth_header)
        #print(reposnd_fligt_data)
        reposnd_fligt_data.raise_for_status() # check for errors
        
        try:
            data = reposnd_fligt_data.json()['data'][0]
        except IndexError:
            # the flight data is empty, 
            # try to find a connecting flight instead with two stopovers
            flight_data_search['max_stopovers'] = 2
            
            reposnd_fligt_data = requests.get(url=f"{self.tequila_api_end_point}/v2/search",
                                            params=flight_data_search,
                                            headers=self.api_tequila_auth_header)
            try: 
                data = reposnd_fligt_data.json()['data'][0]
            except IndexError: 
                # the flight data is empty,
                # return none
                return None
            else:
                flight_data = FlightData(
                    currency=CURRENCY_CODE,
                    price=data['price'],
                    origin_city=data['route'][0]['cityFrom'],
                    origin_airport=data['route'][0]['flyFrom'],
                    destination_city=data['route'][1]['cityTo'],
                    destination_airport=data['route'][1]['flyTo'],
                    out_date=data['route'][0]['local_departure'].split("T")[0],
                    return_date=data['route'][2]['local_departure'].split("T")[0],
                    fly_out_number = data['route'][0]['operating_carrier']+data['route'][0]['operating_flight_no']+'->'+\
                        data['route'][1]['operating_carrier']+data['route'][1]['operating_flight_no'],
                    return_fly_number = data['route'][2]['operating_carrier']+data['route'][2]['operating_flight_no']+'->'+\
                        data['route'][3]['operating_carrier']+data['route'][3]['operating_flight_no'],
                    stop_overs = 2,
                    via_city = data['route'][0]['cityTo'],
                )

                return flight_data
        else:
            flight_data = FlightData(
                currency=CURRENCY_CODE,
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split("T")[0],
                return_date=data['route'][1]['local_departure'].split("T")[0],
                fly_out_number = data['route'][0]['operating_carrier']+data['route'][0]['operating_flight_no'],
                return_fly_number = data['route'][1]['operating_carrier']+data['route'][1]['operating_flight_no'],
            )

            return flight_data
