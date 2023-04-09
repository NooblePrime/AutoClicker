#Made by NooblePrime
import PySimpleGUI as sg
from time import sleep
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key
import threading
clicking = False
cps = 1000

def clicker():
        global clicking
        while clicking == True:
            Controller().click(Button.left, 1)
            sleep(1/cps)

def press_callback(key):
    global clicking
    if key == Key.f6:
        clicking = not clicking
        if clicking == True:
            thread = threading.Thread(target = clicker)
            thread.start()

layout = [
    [sg.Text("Enter clicks per second. If nothing, a letter or a number above 1000 is entered, will default to 1000.\nPress Submit to enter a new value and F6 to start or stop clicking.")],
    [sg.Text('Clicks per second:', size =(13, 1)), sg.InputText()],
    [sg.Submit()]]

window = sg.Window("Nooble's Autoclicker", layout)
listen = Listener(on_press=press_callback)
listen.start()
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        listen.stop()
        break
    if event == "Submit":
        if values[0].isnumeric() and int(values[0]) <= 1000 and values[0] != '':
            cps = int(values[0])
        else:
            cps = 1000
