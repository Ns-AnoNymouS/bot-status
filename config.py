"""
Configuration module for the bot status checker.

This module loads environment variables required for the bot to function,
such as session strings, bot usernames, channel IDs, message IDs, and API credentials.
It also sets up the necessary configuration settings.
"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH")
SESSION_STRING = getenv("SESSION_STRING")
BOTS = [i.strip() for i in getenv("BOTS").split()]
CHANNEL_ID = int(getenv("CHANNEL_ID"))
MESSAGE_IDS = [int(i.strip()) for i in getenv("MESSAGE_IDS").split()]
SLEEP_TIME = int(getenv("SLEEP_TIME", "30"))
GET_NOFIFIED = getenv('GET_NOFIFIED', 'False') == 'True'
