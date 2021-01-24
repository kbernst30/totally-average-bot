import aiohttp
import discord
import logging
import os

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

YOUTUBE_LATEST_REQUEST_URI = (
    "https://www.googleapis.com/youtube/v3/search?key=%s&part=snippet&channelId=%s&order=date&type=video"
)


def register_commands(bot):
    load_dotenv()

    @bot.command(name="video", help="Gets the URL of the latest YouTube video")
    async def send_latest_video(ctx):
        if bot.youtube_api_key is None:
            await ctx.send("Uh-oh... Looks like I can't get the latest YouTube post. Try again later.")
            return

        youtube_request_uri = YOUTUBE_LATEST_REQUEST_URI % (bot.youtube_api_key, os.getenv('YOUTUBE_CHANNEL_ID'))

        async with aiohttp.ClientSession() as session:
            async with session.get(youtube_request_uri) as response:
                response_js = await response.json()
                latest_youtube_videos = response_js['items']

        if len(latest_youtube_videos) == 0:
            embed = discord.Embed(
                description="I can't seem to find any recent videos on YouTube... how average :neutral_face:",
                color=0x36457A
            )

            await ctx.send(embed=embed)

        else:
            await ctx.send("Need a video here")
