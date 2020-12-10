import os
import time
import base64
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

token_url = "https://accounts.spotify.com/api/token"
token_data = {
    "grant_type": "client_credentials"
}

client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_b64 = base64.b64encode(client_credentials.encode())

token_headers = {
    "Authorization": f"Basic {client_credentials_b64.decode()}"
}

response = requests.post(token_url, data=token_data, headers=token_headers)
print(response.json())

class SpotifyClient:
    client_id = None
    client_secret = None
    access_token = None
    access_token_expires = datetime.now()

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret




# path = "C:\\Users\\Piotr Błachnio\\Desktop\\Spotify"

# def close_application():
#     os.system("TASKKILL /F /IM Spotify.exe")

# def open_application():
#     os.startfile(path)

# if __name__ == "__main__":
#     close_application()
#     time.sleep(1)
#     open_application()
