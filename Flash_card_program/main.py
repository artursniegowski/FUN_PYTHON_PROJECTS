from CSV_reader_manager import CSVReaderManager
from random import choice
import tkinter


# constants - settings
# background
BACKGROUND_COLOR = "#B1DDC6"
# main window settings
MAIN_WINDOW_TITLE = "Flash cards"
MAIN_WINDOW_PADDING_X = 50
MAIN_WINDOW_PADDING_Y = 50
# button settings
BUTTON_CHECK_FILE_NAME = "./images/right.png"
BUTTON_CROSS_FILE_NAME = "./images/wrong.png"
# settings for canvas - flash card
CARD_FRONT_FILE_NAME = "./images/card_front.png"
CARD_BACK_FILE_NAME = "./images/card_back.png"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
CANVAS_LANGUAGE_TEXT_FONT = ('Ariel',40,'italic')
CANVAS_WORD_TEXT_FONT = ('Ariel',60,'bold')
# settings for data files
DEFAULT_WORDS_FILE_NAME = "./data/french_words.csv"
WORDS_TO_LEARN_FILE_NAME = "./data/french_words_to_learn.csv"
# setting for the current word
random_word = {}
#====================================================#




# -------------------------- Reads words .csv file as a list of dict -------- #
data_reader = CSVReaderManager(file_name=WORDS_TO_LEARN_FILE_NAME,\
    file_name_default=DEFAULT_WORDS_FILE_NAME)
data_words: list[dict] = data_reader.return_data_as_dict()

# --------------- word is known - delete it from the list --------------------
def delete_word():
    """
    the check button was pressed which means the word is knowb, therfore will be
    removed from the list
    """
    if random_word in data_words and len(data_words) >  1:
        data_words.remove(random_word)
        data_reader.save_data_as_csv(data_words)
        pick_random_word()

# ---------------------------- Picks random french word -------------------- #
def pick_random_word():
    """
    picks random french word
    """
    global flip_timer, random_word
    window_main.after_cancel(flip_timer)

    random_word = choice(data_words)
    canvas.itemconfig(canvas_image, image=flash_card_front_image)
    canvas.itemconfig(languge_text_canvas, fill='black')
    canvas.itemconfig(word_text_canvas, fill='black')
    canvas.itemconfig(languge_text_canvas,text='French')
    canvas.itemconfig(word_text_canvas, text = random_word['French'])

    flip_timer = window_main.after(3000,flip_card,random_word)

# ---------------------------- Fliping card -------------------------------- #
def flip_card(word: dict):
    """
    fliping card and showing translation in english
    """
    canvas.itemconfig(canvas_image, image=flash_card_back_image)
    canvas.itemconfig(languge_text_canvas, fill='white')
    canvas.itemconfig(word_text_canvas, fill='white')
    canvas.itemconfig(languge_text_canvas,text='English')
    canvas.itemconfig(word_text_canvas, text = word['English'])


# ---------------------------- UI SETUP ------------------------------------ #
# creating the main window
window_main = tkinter.Tk()
window_main.title(MAIN_WINDOW_TITLE)
window_main.config(padx=MAIN_WINDOW_PADDING_X, pady=MAIN_WINDOW_PADDING_Y, \
    bg=BACKGROUND_COLOR)
# initial value for the timer
flip_timer = window_main.after(3000,flip_card)

# creating canvas flash card on the screen
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, \
    highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_front_image = tkinter.PhotoImage(file=CARD_FRONT_FILE_NAME)
flash_card_back_image = tkinter.PhotoImage(file=CARD_BACK_FILE_NAME)
canvas_image = canvas.create_image(CANVAS_WIDTH/2,CANVAS_HEIGHT/2,\
    image=flash_card_front_image)
languge_text_canvas = canvas.create_text(CANVAS_WIDTH/2,CANVAS_HEIGHT/2-100, \
    text="Title",font=CANVAS_LANGUAGE_TEXT_FONT)
word_text_canvas = canvas.create_text(CANVAS_WIDTH/2,CANVAS_HEIGHT/2, \
    text="word",font=CANVAS_WORD_TEXT_FONT)
canvas.grid(row=0,column=0,columnspan=2) 


# creating buttons
button_check_image = tkinter.PhotoImage(file=BUTTON_CHECK_FILE_NAME)
button_check = tkinter.Button(image=button_check_image, highlightthickness=0,\
     command=delete_word)
button_check.grid(row=1,column=1) 

button_cross_image = tkinter.PhotoImage(file=BUTTON_CROSS_FILE_NAME)
button_cross = tkinter.Button(image=button_cross_image, highlightthickness=0,\
     command=pick_random_word)
button_cross.grid(row=1,column=0)

# initial settings of the flash card
pick_random_word()

# waiting on the user to close the window
window_main.mainloop()