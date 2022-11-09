from hashlib import new
from screen_viewer import ScreenView
from data_manager import StatesDataManager

# creating the screen object with the map
my_screen = ScreenView()

# creatitng the databse for with the states and coresponding coordinates
data_manager = StatesDataManager()


# initial settings for the game
guess_number = 0
guessed_states = []

# main loop of the game
while len(guessed_states) < 50:
    user_answer = my_screen.prompt_user_input(guess_number)
    user_answer = user_answer.strip().title()

    # exiting the game
    if user_answer == "Exit":
        all_states = data_manager.get_all_states()
        missed_states = []
        # checking which states were missed
        for state in all_states:
            if not state in guessed_states:
                missed_states.append(state)
        # saving the missed states into a file
        data_manager.save_to_csv(list_of_states_to_save=missed_states)
        # ending while loop
        break
        
    state_name, x_data, y_data = \
        data_manager.check_if_state_exists_in_database(user_answer)
    
    # if data exists for the user input
    if len(state_name) > 0 and len(x_data) > 0 and len(y_data) > 0 \
        and not state_name in guessed_states:
        my_screen.draw_state_name(str(*state_name),int(x_data),int(y_data))
        guessed_states.append(str(*state_name))
        guess_number += 1
