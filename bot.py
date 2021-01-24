import discord
import logging

from discord.ext import commands

logger = logging.getLogger(__name__)

YOUTUBE_API_KEY = "youtube_api_key"


class TotallyAverageBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        logger.info("Starting TotallyAverageBot...")

        intents = discord.Intents.default()
        # Needed intent to track on_member_join and on_member_leave
        intents.members = True

        self.youtube_api_key = kwargs.get(YOUTUBE_API_KEY) if YOUTUBE_API_KEY in kwargs else None

        super().__init__(intents=intents, command_prefix='!')

    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
        logger.info(f'{member.name} joined!')
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )
