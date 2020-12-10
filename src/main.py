import os
import time

path = "C:\\Users\\Piotr Błachnio\\Desktop\\Spotify"

def close_application():
    os.system("TASKKILL /F /IM Spotify.exe")

def open_application():
    os.startfile(path)

if __name__ == "__main__":
    close_application()
    time.sleep(1)
    open_application()