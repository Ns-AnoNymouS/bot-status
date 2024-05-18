"""
This script initializes a Pyrogram client, prompts the user for API credentials if not provided,
exports the session string, sends it to the user's "Saved Messages" on Telegram, and prints it.

Modules:
    - pyrogram: To interact with the Telegram API.
    - config: To import the API_ID and API_HASH from the configuration file.

Constants:
    - API_ID (int): The Telegram API ID.
    - API_HASH (str): The Telegram API Hash.

Functionality:
    - The script initializes the Pyrogram client using the provided API credentials.
    - It exports the session string for the client.
    - It sends the session string to the user's "Saved Messages" chat on Telegram.
    - It prints the session string to the console.
"""

from pyrogram import Client
from config import API_ID, API_HASH

if API_ID == 0:
    API_ID = input("Please enter the API ID: ")
if API_HASH is None:
    API_HASH = input("Please enter the API HASH: ")
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

with app:
    SESSION_STRING = app.export_session_string()
    app.send_message("me", f"Your session string: `{SESSION_STRING}`")
    print(SESSION_STRING)
