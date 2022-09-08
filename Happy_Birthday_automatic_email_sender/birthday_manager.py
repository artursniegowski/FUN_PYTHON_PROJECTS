# class managing the csv read/write operations
import pandas
import datetime as dt

class CSVReaderManager:
    """
    class for managing the read operations from a csv file
    """
    def __init__(self, file_name: str) -> None:
        try:
            self.data = pandas.read_csv(file_name)
        except FileNotFoundError:
            print(f"Could not find {file_name}")
            self.data = pandas.DataFrame() # create empty data frame
            
    def return_data_as_dict(self) -> list[dict]:
        """
        if read_csv was sucesfull it will return a dictionary of the data read
        otherwise (if not sucesful) it will return None
        """
        if not self.data.empty :
            return self.data.to_dict(orient="records")
        else:
            return None


    def return_current_day_birthday_data(self) -> list[dict]:
        """
        returns the curent day birthday people, if dosent exists 
        return None or empty list
        """
        actual_day = dt.datetime.now().day
        actual_month = dt.datetime.now().month
        new_data = []
        if all_data := self.return_data_as_dict():
            new_data = [data for data in all_data if data['day'] == actual_day \
                and data['month'] == actual_month]
        else:
            return None
        return new_data
