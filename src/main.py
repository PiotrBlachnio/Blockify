import os
import time
from dotenv import load_dotenv

# class SpotifyClient:
#     def __init__(self):
#         self.user_id = spotify_user_id

#     def pause(self):

load_dotenv()

MY_ENV_VAR = os.getenv('TEST')

print(MY_ENV_VAR)



# path = "C:\\Users\\Piotr Błachnio\\Desktop\\Spotify"

# def close_application():
#     os.system("TASKKILL /F /IM Spotify.exe")

# def open_application():
#     os.startfile(path)

# if __name__ == "__main__":
#     close_application()
#     time.sleep(1)
#     open_application()
