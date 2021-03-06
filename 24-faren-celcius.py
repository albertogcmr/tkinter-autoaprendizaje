from tkinter import *


def fahrenheit_to_celcius(f):
    return (f-32)/1.8


def convert():
    """ convert fahrenheit to celsius """
    try:
        f=float(var_fahenheit.get())
        c = fahrenheit_to_celcius(f)
        var_celcius.set(c)
    except ValueError:
        var_celcius.set('ValueError')
    else:
        print('else: cambio realizado')
    finally:
        print('finally: fin conversión')


# variables
my_window = Tk()
var_fahenheit = StringVar()
var_celcius = StringVar()

# build the GUI
label_fah = Label(my_window, text='Introduce Fahrenheit')
label_cel = Label(my_window, text='Temperatura en Celcius')
button_1 = Button(my_window, text='Convertir', command=convert)
entry_1 = Entry(my_window, textvariable=var_fahenheit)
label_result = Label(my_window, textvariable=var_celcius)

label_fah.grid(row=0, column=0)
label_cel.grid(row=1, column=0)
button_1.grid(row=2, column=0)
entry_1.grid(row=0, column=1)
label_result.grid(row=1, column=1)

my_window.mainloop()
