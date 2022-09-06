#This class is responsible for structuring the flight data.

class FlightData:
    """
    This class is responsible for structuring the flight data.
    """
    def __init__(self, price, currency, origin_city, origin_airport, destination_city, \
        destination_airport, out_date, return_date, fly_out_number, \
            return_fly_number, stop_overs=0, via_city="") -> None:
        self.currency = currency
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.fly_out_number = fly_out_number
        self.return_fly_number = return_fly_number

        self.stop_overs = stop_overs
        self.via_city = via_city


    def return_format_data_for_email(self) -> str:
        """
        return nicely formated data for an email content
        """
        if self.stop_overs:
            link = f"https://www.skyscanner.com/transport/flights/{self.origin_airport}/{self.destination_airport}/{self.out_date}/{self.return_date}/"
            return f"""Only {self.currency} {self.price} to fly from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport}, from {self.out_date} (flight: {self.fly_out_number}) to {self.return_date} (flight: {self.return_fly_number}).
            
        The flight has 1 stop over, via {self.via_city}\n"""+link
        else:
            link = f"https://www.skyscanner.com/transport/flights/{self.origin_airport}/{self.destination_airport}/{self.out_date}/{self.return_date}/"
            return f"Only {self.currency} {self.price} to fly from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport}, from {self.out_date} (flight: {self.fly_out_number}) to {self.return_date} (flight: {self.return_fly_number}). \n"+link


    def __str__(self) -> str:
        return f"{self.destination_city}: {self.currency} {self.price}"
