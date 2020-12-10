import os

def close_application():
    os.system("TASKKILL /F /IM Spotify.exe")

if __name__ == "__main__":
    close_application()