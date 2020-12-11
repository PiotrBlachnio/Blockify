import keyboard
import os
import time
import win32gui
import win32con
from dotenv import load_dotenv
load_dotenv()

path = "C:\\Users\\Piotr Błachnio\\Desktop\\Spotify"

def close_application():
    os.system("TASKKILL /F /IM Spotify.exe")

def open_application():
    os.startfile(path)

if __name__ == "__main__":
    close_application()
    time.sleep(1)
    open_application()
    time.sleep(4)
    keyboard.press_and_release("space")
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)