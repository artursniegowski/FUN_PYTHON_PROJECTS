# class for managing the data
import pandas

class StatesDataSettings:
    """
    States Data settings
    """ 
    FILE_NAME_STATES = '50_states.csv'
    FILE_NAME_STATES_MISSED = 'states_to_learn.csv'
    STATE_COLUMN_NAME = 'state'
    STATE_COLUMN_NAME_X_COR = 'x'
    STATE_COLUMN_NAME_Y_COR = 'y'


class StatesDataManager:
    """
    managing the data for the states
    """ 
    def __init__(self) -> None:
        try:
            self.data = pandas.read_csv(StatesDataSettings.FILE_NAME_STATES)
        except FileNotFoundError:
            print(f"Cant Find {StatesDataSettings.FILE_NAME_STATES}. Different dir? does it exists?")
            raise

    def check_if_state_exists_in_database(self, state_name: str) \
        -> tuple[str,int,int]:
        """
        returns name,x,y coordinates if the state_name exists in the database 
        otherwise returns two emty values
        """
        return self.data[self.data[StatesDataSettings.STATE_COLUMN_NAME] == state_name].state.values,\
            self.data[self.data[StatesDataSettings.STATE_COLUMN_NAME] == state_name].x.values, \
            self.data[self.data[StatesDataSettings.STATE_COLUMN_NAME] == state_name].y.values


    def get_all_states(self) -> list[str]:
        """
        returns a list of all states
        """
        return self.data[StatesDataSettings.STATE_COLUMN_NAME].to_list()

    def save_to_csv(self, list_of_states_to_save: list[str], \
        file_name: str = StatesDataSettings.FILE_NAME_STATES_MISSED) -> None:
        """
        save a list of states to a file
        """
        new_data = pandas.DataFrame({StatesDataSettings.STATE_COLUMN_NAME:list_of_states_to_save})
        #new_data = new_data.sort_values(by=['Count'],ascending=False).reset_index(drop=True)
        # convert data to csv
        new_data.to_csv(file_name)
            