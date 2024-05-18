## README.md

# Bot Status Checker

This project is a Telegram bot that monitors the uptime status of specified bots and updates their status in a designated channel. It periodically sends a `/start` command to each monitored bot and checks if the bot is responsive. The results are then posted to a channel, and notifications can be sent if a bot is down.

This project is a clone of [https://github.com/odysseusmax/bug-free-broccoli](https://github.com/odysseusmax/bug-free-broccoli) with improved performance by using `pyromod` which helps in receiving messages instead of waiting for a specific amount of time even if the message is received.

## Features

- Monitors the status of multiple bots.
- Updates the status messages in a designated channel every specific amount of time.
- Sends notifications if a bot is down.
- Uses `pyromod` for efficient message handling.

## Requirements

- Python 3.7+
- `pyromod` library
- `pytz` library

## Configuration

Before running the bot, you need to configure the following constants in a `.env` file:

```python
API_HASH = "your_api_hash"
API_ID = "your_api_id"
BOTS = "bot1 bot2 bot3"  # List of bot usernames to monitor (seperated by space)
MESSAGE_IDS = "12345678 87654321"  # List of message IDs to update (seperated by space)
CHANNEL_ID = -1001234567890  # ID of the channel where status updates are posted
SESSION_STRING = "your_session_string" # check Generating Session String
SLEEP_TIME = 60  # Time in minutes between each check
GET_NOFIFIED = True  # Set to True to receive notifications in saved messages if a bot is down (default: False)
```

## Generating Session String

To generate the session string, use the `session.py` script:

```python
from pyrogram import Client

API_ID = input("Please enter the API ID: ")
API_HASH = input("Please enter the API HASH: ")
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

with app:
    SESSION_STRING = app.export_session_string()
    app.send_message("me", f"Your session string: `{SESSION_STRING}`")
    print(SESSION_STRING)
```

## Running the Bot

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Ns-AnoNymouS/bot-status.git
    cd bot-status
    ```

2. **Install the Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Generate the Session String**:
    - Run the `session.py` script to generate the session string and update `.env`.

4. **Configure the Constants**:
    - Create a `.env` file with the required configuration constants as shown above.

5. **Run the Bot**:
    ```bash
    python main.py
    ```

That's it! Your bot should now be running and checking the status of the specified bots, with added buttons for better interaction.

## Heroku Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Ns-AnoNymouS/bot-status/tree/master)