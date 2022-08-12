import tkinter

# settings
TITLE_WINDOW = 'Mi to Km Converter'
WINDOW_WIDTH = 290
WINDOW_HEIGHT = 80
TEXT_MILES = 'Miles'
TEXT_KM = 'Km'
TEXT_IS_EQUAL_TO = 'is equal to'
TEXT_VALUE = '0'
BUTTON_TEXT_CALCULATE = 'Calculate'


# creating the main window
window = tkinter.Tk()
window.title(TITLE_WINDOW)
#window.minsize(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
window.config(padx=20,pady=20)

# creating labels
label_miles = tkinter.Label(text=TEXT_MILES)
label_miles.grid(column=2,row=0)
label_miles.config(padx=10,pady=10)

label_km = tkinter.Label(text=TEXT_KM)
label_km.grid(column=2,row=1)
label_km.config(padx=10,pady=10)

label_is_equal_to = tkinter.Label(text=TEXT_IS_EQUAL_TO)
label_is_equal_to.grid(column=0,row=1)
label_is_equal_to.config(padx=10,pady=10)

label_value = tkinter.Label(text=TEXT_VALUE)
label_value.grid(column=1,row=1)
label_value.config(padx=10,pady=10)

# creating the input box
input_field = tkinter.Entry(width=8)
input_field.grid(column=1,row=0)

# function for convertin the miles to km
def convert_miles_to_km() -> float:
    """
    function for converting miles to km
    """
    converted_km = 0
    if miles := input_field.get().strip():
        converted_km = 1.609344 * float(miles)
        label_value['text'] = str(float(int(converted_km*1000))/1000) 


# creating the calculate button
button_calculate = tkinter.Button(text=BUTTON_TEXT_CALCULATE,command=convert_miles_to_km)
button_calculate.grid(column=1,row=2)
button_calculate.config(padx=10,pady=10)


# waiting on the user to close the window
window.mainloop()