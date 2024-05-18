"""
This script defines a Telegram bot that monitors the uptime status of specified bots and
updates their status in a designated channel.

The bot periodically sends a /start command to each monitored bot and
checks if the bot is responsive. The results are then posted to a channel, and
notifications can be sent if a bot is down.

Modules:
    - logging: Configures logging for the script.
    - time: Used for sleeping between checks.
    - datetime: Used for getting the current time.
    - pytz: Used for timezone conversions.
    - pyromod: Provides the Client class for interacting with Telegram.
    - pyrogram: Used for handling filters and message handlers.
    - config: Contains configuration constants like
                API_HASH, API_ID, BOTS, MESSAGE_IDS,
                CHANNEL_ID, SESSION_STRING, SLEEP_TIME, and GET_NOFIFIED.

Classes:
    - Bot: A subclass of pyromod. Client that implements the bot functionality.

Functions:
    - status: Responds to the status command to confirm the bot is up and running.
"""

import time
import logging
import datetime

import pytz
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyromod import Client
from pyromod.exceptions import ListenerTimeout
from config import (
    API_HASH,
    API_ID,
    BOTS,
    MESSAGE_IDS,
    CHANNEL_ID,
    SESSION_STRING,
    SLEEP_TIME,
    GET_NOFIFIED,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


class Bot(Client):  # pylint: disable=too-many-ancestors
    """
    A Telegram bot that checks the uptime status of specified bots and
    updates the status messages in a channel.

    Attributes:
        None

    Methods:
        __init__():
            Initializes the Bot client with the given
            session string, API ID, and API hash.
        run():
            Starts the bot and runs the status check loop.
        check():
            Periodically checks the status of specified bots and
            updates the status messages in the channel.
    """

    def __init__(self):
        """
        Initializes the Bot client with the given session string, API ID, and API hash.
        """
        super().__init__(
            name="StatusCheckBot",
            session_string=SESSION_STRING,
            api_id=API_ID,
            api_hash=API_HASH,
        )

    async def start(self):
        """
        Starts the bot by invoking the parent class's start method.

        This method is an asynchronous override that ensures the bot client
        starts correctly, utilizing the parent class's implementation.
        """
        await super().start()

    def run(self):
        """
        Starts the bot and runs the status check loop.
        """
        super().run(self.start())
        super().run(self.check())
        super().run(self.stop())

    async def check(self):
        """
        Periodically checks the status of specified bots and
        updates the status messages in the channel.
        """
        self.add_handler(
            MessageHandler(
                status, filters=(filters.command("status", ".") & filters.me)
            )
        )
        try:
            while True:
                logger.info("starting to check uptime..")
                edit_text = "**🤖 NS BOTS Status** (Updated every 1 hour)\n\n"
                for bot in BOTS:
                    logger.info("checking @%s", bot)
                    try:
                        await self.ask(chat_id=bot, text="/start", timeout=10)
                    except ListenerTimeout:
                        logger.warning("@%s is down", bot)
                        edit_text += (
                            f"__Bot Name:__ @{bot}\n__Bot Status:__ Down ❌\n\n"
                        )
                        if GET_NOFIFIED:
                            await self.send_message("me", f"@{bot} was down")
                    else:
                        logger.info("all good with @%s", bot)
                        edit_text += f"__Bot Name:__ @{bot}\n__Bot Status:__ Up ✅\n\n"

                time_now = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                formatted_time = time_now.strftime("%d %B %Y %I:%M %p")

                edit_text += f"__Last checked on {formatted_time} (**IST**)__"

                for message_id in MESSAGE_IDS:
                    await self.edit_message_text(CHANNEL_ID, message_id, edit_text)
                    time.sleep(5)
                logger.info("everything done! sleeping for %s mins...", SLEEP_TIME)

                time.sleep(SLEEP_TIME * 60)
        except KeyboardInterrupt:
            logger.info("Stopping the session....")

    async def stop(self, *args, **kwargs):
        """
        Stops the bot by invoking the parent class's stop method.

        This method is an asynchronous override that ensures the bot client
        stops correctly, utilizing the parent class's implementation. It can
        also accept additional arguments and keyword arguments if needed.
        """
        await super().stop(*args, **kwargs)


async def status(_, message):
    """
    Responds to the status command to confirm the bot is up and running.

    Args:
        _ (Client): The client instance.
        message (Message): The incoming message object.
    """
    await message.edit(text="Bot is up and running....")


if __name__ == "__main__":
    Bot().run()
