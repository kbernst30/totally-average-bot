import constants
import os
import logging

from dotenv import load_dotenv

from bot import TotallyAverageBot
from commands import register_commands


def main():
    load_dotenv()
    discord_token = os.getenv(constants.ENV_DISCORD_TOKEN)
    youtube_key = os.getenv(constants.ENV_YOUTUBE_API_KEY)

    bot = TotallyAverageBot(youtube_api_key=youtube_key)
    register_commands(bot)
    bot.run(discord_token)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    main()
