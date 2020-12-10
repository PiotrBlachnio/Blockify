import os
import time
import base64
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

class SpotifyClient:
    client_id = None
    client_secret = None
    access_token = None
    access_token_expires = datetime.now()
    access_token_did_expire = True
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials_base64(self):
        if(self.client_id == None or self.client_secret == None):
            raise Exception("You must set client_id and client_secret")

        client_credentials = f"{self.client_id}:{self.client_secret}"
        client_credentials_base64 = base64.b64encode(client_credentials.encode())

        return client_credentials_base64.decode()

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def get_token_headers(self):
        client_credentials_base64 = self.get_client_credentials_base64()

        return {
            "Authorization": f"Basic {client_credentials_base64}"
        }

    def perform_auth(self):
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()

        response = requests.post(self.token_url, data=token_data, headers=token_headers)
        
        is_response_valid = response.status_code in range (200, 299)
        if not is_response_valid:
            return False

        data = response.json()
        now = datetime.now()
        self.access_token = data["access_token"]
        self.access_token_expires = now + timedelta(seconds=data["expires_in"])
        self.access_token_did_expire = now > self.access_token_expires

        return True

client = SpotifyClient(CLIENT_ID, CLIENT_SECRET)
client.perform_auth()

print(client.access_token)
# path = "C:\\Users\\Piotr Błachnio\\Desktop\\Spotify"

# def close_application():
#     os.system("TASKKILL /F /IM Spotify.exe")

# def open_application():
#     os.startfile(path)

# if __name__ == "__main__":
#     close_application()
#     time.sleep(1)
#     open_application()