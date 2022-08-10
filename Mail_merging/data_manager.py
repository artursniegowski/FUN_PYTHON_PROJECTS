# class for managing the read/ write operations
import json

class DataManager:
    """
    Managing the read, write operations of ta file
    """
    def __init__(self, template_name: str, names_file_names: str ) -> None:
        self.file_name_for_names = names_file_names
        self.file_name_for_template = template_name

    def read_names_json(self, file_name: str) -> list[str]:
        """
        reads the list of names from the json file and 
        returns a list of names.
        If the read is not successful i will return None
        """
        names = []
        try:
            with open(file_name,'r') as f:
                names = json.load(f)
        except FileNotFoundError:
            print(f"Error, Cant open {file_name}, check if file exists or if the \
                directory is correct")
        except Exception as e:
            print(type(e))
            print(f"Exception {e} was caught!")
        else:
            print(f"Reading names from {file_name} was successful!")


        if names:
            return names['names']
        else:
            return None


    def read_template(self, file_name: str) -> str:
        """
        returns the tempalte file as a string
        if there is an error return None
        """
        data = 0
        try:
            with open(file_name,'r') as f:
                data = f.read()
        except FileNotFoundError:
            print(f"Error, Cant open {file_name}, check if file exists or if the \
                directory is correct")
        except Exception as e:
            print(type(e))
            print(f"Exception {e} was caught!")
        else:
            print(f"Reading template from {file_name} was successful!")
            return data
        
        return None

    def write_data_to_output(self) -> None:
        """
        based on the data read from files in folder input,
        create messages in the folder outpu
        """
        names = self.read_names_json(self.file_name_for_names)
        template_data = self.read_template(self.file_name_for_template)

        if names and template_data:
            for name in names:
                new_data = template_data.replace("[name]",name,1)
                try:
                    with open(f"./output/letter_for_{name}.txt",'w') as f:
                        f.write(new_data)
                except Exception as e:
                    print(type(e))
                    print(f"Exceptio {e} was caught!")
                else:
                    print(f"Writing was sucessful")
        else:
            # operation was not successful
            print("Abort operation")
            return None

    