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
