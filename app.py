import os
import requests
from dotenv import load_dotenv
from save_db import save_trophies_logs
from database import initialize_database
# Load environment variables from .env file
load_dotenv()

# Retrieve API key and player ID from environment variables
API_KEY = os.getenv("KEY")
PLAYER_ID = os.getenv("PLAYER")

# Clash of Clans API endpoint
API_URL = f"https://api.clashofclans.com/v1/players/%23{PLAYER_ID}"

# Headers for the API request
HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_trophies():
     try:
          # Make the API request
          response = requests.get(API_URL, headers=HEADERS)
          response.raise_for_status()  # Raise an error for HTTP errors

          # Parse the JSON response
          data = response.json()

          # Extract trophies data
          trophies = data.get("trophies", "No trophies data found")
          save_trophies_logs(trophies)
          print(f"Player Trophies: {trophies}")

     except requests.exceptions.RequestException as e:
          print(f"An error occurred: {e}")

if __name__ == "__main__":
     initialize_database()
     get_trophies()