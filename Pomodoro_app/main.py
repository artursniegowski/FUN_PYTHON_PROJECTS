from cgitb import text
import tkinter

# Constant Variables
# main settings
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# main window settings
MAIN_WINDOW_TITLE = "POMODORO"
MAIN_WINDOW_PADDING_X = 30
MAIN_WINDOW_PADDING_Y = 10
# canvas settings
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
CANVAS_FILL_TEXT_COLOR = "white"
CANVAS_TEXT_FONT = (FONT_NAME,35,'bold')
FILE_NAME_TOMATO = "tomato.png"
# Label settings
TIMMER_LABEL_TEXT = "TIMER"
TIMMER_LABEL_TEXT_FONT = (FONT_NAME,35,'bold')
CHECK_MARK_LABEL = '✔'
CHECK_MARK_LABEL_TEXT_FONT = (FONT_NAME,15,'bold')
# buttons settings
BUTTON_RESET_TEXT = "Reset"
BUTTON_START_TEXT = "Start"
reps = 0 
pomodoro_timer = None

########################## TIMER RESET ###############################
def reset_timmer():
    # reseting the timer
    window_main.after_cancel(pomodoro_timer)
    # reseting other values 
    canvas.itemconfig(timmer_text_canvas, text="00:00")
    label_timmer['text'] = TIMMER_LABEL_TEXT
    label_timmer["fg"] = GREEN
    label_check_marks['text'] = ''
    global reps
    reps = 0

########################## TIMER MECHANISM ###############################
# starting the count down
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    # if it is the 8th rep:
    # long break - and reset
    if reps % 8 == 0 :
        count_down(long_break_sec)
        label_timmer['text'] = 'BREAK'
        label_timmer["fg"] = RED
    # if it is the 2st/4rd/6th rep:
    # short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timmer['text'] = 'BREAK'
        label_timmer["fg"] = PINK
    # if it is the 1st/3rd/5th/7th rep:
    # work sec timer
    else:
        count_down(work_sec)
        label_timmer['text'] = 'WORK'
        label_timmer["fg"] = GREEN


########################## COUNTDOWN MECHANISM ###############################
def count_down(count):
    
    # 00:00
    count_min = int(count // 60)
    count_sec = int(count % 60)
    timer_value = f"{count_min:02d}:{count_sec:02d}"

    # updating the value of text on the vanvas with the value count
    canvas.itemconfig(timmer_text_canvas, text=timer_value)
    if count > 0 :
        # calls count_down after 1000ms with the argument = count -1
        global pomodoro_timer # we need to use this varibale out of 
                              # scope of this funciton - this is why global
        pomodoro_timer = window_main.after(1000, count_down, count-1)
    else: # if it goes to zero start again the timer
        start_timer()
        marks = ''
        if reps % 8 == 0:
            marks = CHECK_MARK_LABEL * 4
        else:
            marks = (reps%8)//2 * CHECK_MARK_LABEL
        label_check_marks['text'] = marks

########################## UI SETUP ###############################

# creating the main window
window_main = tkinter.Tk()
window_main.title(MAIN_WINDOW_TITLE)
window_main.config(padx=MAIN_WINDOW_PADDING_X, pady=MAIN_WINDOW_PADDING_Y,\
     bg=YELLOW)

# creating canvas witht the tomato pic and time value text
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, \
    highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=FILE_NAME_TOMATO)
canvas.create_image(CANVAS_WIDTH/2,CANVAS_HEIGHT/2,image=tomato_image)
timmer_text_canvas = canvas.create_text(CANVAS_WIDTH/2,CANVAS_HEIGHT/2+20, \
    text="00:00", fill=CANVAS_FILL_TEXT_COLOR,font=CANVAS_TEXT_FONT)
canvas.grid(row=1,column=1) 

# creating timmer label
label_timmer = tkinter.Label(text=TIMMER_LABEL_TEXT, fg=GREEN,\
    font=TIMMER_LABEL_TEXT_FONT, bg=YELLOW)
label_timmer.grid(row=0,column=1) 

# creating start button 
button_start = tkinter.Button(text=BUTTON_START_TEXT,highlightthickness=0, \
    command=start_timer)
button_start.grid(row=2,column=0)

# creating reset button 
button_reset = tkinter.Button(text=BUTTON_RESET_TEXT,highlightthickness=0, \
    command=reset_timmer)
button_reset.grid(row=2,column=2) 

# creatitng check marks as label
label_check_marks = tkinter.Label(fg=GREEN,\
    font=CHECK_MARK_LABEL_TEXT_FONT, bg=YELLOW)
label_check_marks.grid(row=3,column=1) 

# waiting on the user to close the window
window_main.mainloop()