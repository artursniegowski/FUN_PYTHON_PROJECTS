#This class is responsible for talking to the Google Sheet.
import requests

class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self, sheety_end_point: str, api_sheety_basic_password: str) -> None:
        self.sheety_end_point = sheety_end_point
        self.api_sheety_auth_header = {
            'Authorization':api_sheety_basic_password,
        }

    def return_data_from_table(self, data_name: str,row_num: int = 0) -> None:
        """
        return thw whole data from the sheety table,
        if row_num specified returns only the row number, 
        otherwise return thw whoel table
        """
        if row_num == 0:
            respond_sheety = requests.get(url=self.sheety_end_point,
                                            headers=self.api_sheety_auth_header,)
            respond_sheety.raise_for_status() # checking for errors
            return respond_sheety.json()[data_name]
        else :
            respond_sheety = requests.get(url=f"{self.sheety_end_point}/{str(row_num)}",
                                            headers=self.api_sheety_auth_header,)
            respond_sheety.raise_for_status() # checking for errors
            return respond_sheety.json()[data_name]
        

    def update_a_row(self, row_num_to_update: int ,**kwargs) -> None:
        """
        updating a row in the sheety spreadsheet
        defined columns: 
        city: str - name of a city - like TOKYO
        IATA_code: str - IATA code for the city - like TYO
        lowest_price: float - threshold for the lowest price to be notify - like 400
        
        example of updating a 9 row
        update_a_row(row_num_to_update=9,city='Santiago',iataCode='SAN',lowestPrice=300)

        """
        data_to_write = {}
        data_to_write['price'] = {}
        city_name = kwargs.get('city','City_Name_missing')
        iata_Code = kwargs.get('iataCode','IATA_Code_not_defined')
        lowest_price = kwargs.get('lowestPrice',0)
        
        # updates only values that are defined
        if city_name != 'City_Name_missing': data_to_write['price']['city'] = city_name
        if iata_Code != 'IATA_Code_not_defined': data_to_write['price']['iataCode'] = iata_Code
        if lowest_price != 0: data_to_write['price']['lowestPrice'] = lowest_price
        

        # data_to_write = {
        #     'price': {
        #         'city': kwargs.get('city','City_Name_missing'),
        #         'iataCode': kwargs.get('iataCode','IATA_Code_not_defined'),
        #         'lowestPrice': kwargs.get('lowestPrice',0),
        #     }
        # }

        respond_sheety = requests.put(url=f"{self.sheety_end_point}/{str(row_num_to_update)}",
                                        json=data_to_write,
                                        headers=self.api_sheety_auth_header,)
        respond_sheety.raise_for_status() # checking for errors


    def create_a_row(self, data_name: str, **kwargs) -> None:
        """
        function or creating a row in our sheety file,
        defined columns: 
        city: str - name of a city - like TOKYO
        IATA_code: str - IATA code for the city - like TYO
        lowest_price: float - threshold for the lowest price to be notify - like 400
        
        example of creating a row in a spreadsheet 'price' !
        create_a_row(data_name='price',city='Santiago',iataCode='SAN',lowestPrice=100)
        
        example of creating a row in a spreadsheet 'user' !
        create_a_row(data_name='user',firstName='Adam',lastName='Sanders',email='test@gmail.com')

        """
        data_to_write = {}
        data_to_write[data_name] = {}

        # updates only values that are defined
        if kwargs.get('city',None): data_to_write[data_name]['city'] = kwargs.get('city',None)
        if kwargs.get('iataCode',None): data_to_write[data_name]['iataCode'] = kwargs.get('iataCode',None)
        if kwargs.get('lowestPrice', None): data_to_write[data_name]['lowestPrice'] = kwargs.get('lowestPrice', None)
        if kwargs.get('firstName', None): data_to_write[data_name]['firstName'] = kwargs.get('firstName', None)
        if kwargs.get('lastName', None): data_to_write[data_name]['lastName'] = kwargs.get('lastName', None)
        if kwargs.get('email', None): data_to_write[data_name]['email'] = kwargs.get('email', None)
        


        # data_to_write = {
        #     'price': {
        #         'city': kwargs.get('city','City_Name_missing'),
        #         'iataCode': kwargs.get('iataCode','IATA_Code_not_defined'),
        #         'lowestPrice': kwargs.get('lowestPrice',0),
        #     }
        # }

        respond_sheety = requests.post(url=self.sheety_end_point,
                                        json=data_to_write,
                                        headers=self.api_sheety_auth_header,)
        respond_sheety.raise_for_status() # checking for errors

    
