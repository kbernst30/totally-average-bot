import os
import logging

from dotenv import load_dotenv

from bot import TotallyAverageBot
from commands import register_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def main():
    bot = TotallyAverageBot(youtube_api_key=os.getenv('YOUTUBE_API_KEY'))
    register_commands(bot)
    bot.run(TOKEN)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    main()
