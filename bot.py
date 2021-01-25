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

        super().__init__(intents=intents, command_prefix='!')  # type: ignore

    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member: discord.Member):
        logger.info(f'{member.name} joined!')

        welcome_channel_id = "711984249095586358"
        message = f'**Welcome {member.name}!** We are so excited that you have joined our ' + \
            'community. Our Totally Average Mods and Team are here to answer any questions you ' + \
            'might have and to keep this place safe and respectful. Use !help in any channel to ' + \
            'see how Totally Average Bot can assist you. \n\nPlease take a moment to read over ' + \
            'the rules in <#' + welcome_channel_id + '> and react to get access to the community and then feel ' + \
            'free to introduce yourself and join in the conversation!\n\n Thank you, \nThe Totally Average Gamers Team'

        embed = discord.Embed(
            title="Welcome to the Totally Average Gamers",
            description=message,
            color=0x36457A
        )

        embed.set_author(name="Totally Average Gamers", icon_url=self.user.avatar_url)

        await member.create_dm()
        await member.dm_channel.send(embed=embed)
