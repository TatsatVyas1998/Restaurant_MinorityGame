import tkinter as tk
import requests

from PIL import Image, ImageTk


app= tk.Tk()

HEIGHT=800
WIDTH=800

def format_response(covid_test):
    try:
        info= 'Blank: '
    except:
        info= 'There was a problem retrieving that information...'

    return info

roundsFrame.pack()


var=IntVar()
c= Checkbutton(window, text="Groups",variable=var,background="#2a2a2a",activebackground="#2a2a2a",fg="white",selectcolor="#2a2a2a")
c.pack()


buttonRun = Button(window, text="RUN SIMULATION",fg="white",bg="black",pady="15").pack(pady=15)

#var=IntVar()
#c= Checkbutton(window, text="Groups",variable=var)


window.mainloop()