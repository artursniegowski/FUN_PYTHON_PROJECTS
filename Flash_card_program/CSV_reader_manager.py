# class for reading the csv files and managing the data
import pandas

class CSVReaderManager:
    """
    class for managing the read operations from a csv file
    """
    def __init__(self, file_name: str, file_name_default: str) -> None:
        self.file_name = file_name
        try:
            self.data = pandas.read_csv(file_name)
        except FileNotFoundError:
            self.data = pandas.read_csv(file_name_default)
            print(f"Could not find {file_name}, read {file_name_default} instead")
            
    def return_data_as_dict(self) -> list[dict]:
        """
        if read_csv was sucesfull it will return a dictionary of the data read
        otherwise (if not sucesful) it will return None
        """
        if not self.data.empty :
            return self.data.to_dict(orient="records")
        else:
            return None

    def save_data_as_csv(self, data_to_write: list[dict]) -> None:
        """
        saves the dictionary to csv
        """
        if self.file_name:
            data_to_save = pandas.DataFrame(data_to_write)
            data_to_save.to_csv(self.file_name,index=False)