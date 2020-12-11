import keyboard
import os
import time
import win32gui
import win32con

class Blockify:
    path = ''

    def __init__(self):
        self.read_path()
        self.start()

    def read_path(self):
        file = open('path.txt', 'r', encoding='utf-8')
        self.path = file.read()
    
    def open_application(self):
        if(self.path == ''):
            raise Exception('Path is not specified!')

        os.startfile(self.path)

    def close_application(self):
        os.system("TASKKILL /F /IM Spotify.exe")

    def restart_application(self):
        self.close_application()
        self.open_application()

    def wait(self, sec):
        time.sleep(sec)

    def resume_playback(self):
        keyboard.press_and_release("space")

    def minimize_window(self):
        window = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(window, win32con.SW_MINIMIZE)

    def start(self):
        self.restart_application()
        self.wait(2.3)

        self.resume_playback()
        self.minimize_window()
        
Blockify()