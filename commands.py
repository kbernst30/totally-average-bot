import aiohttp
import discord
import logging
import os

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

YOUTUBE_LATEST_REQUEST_URI = (
    "https://www.googleapis.com/youtube/v3/search?key=%s&part=snippet&channelId=%s&order=date&type=video"
)

EMBED_COLOR = 0x36457A
PODCAST_URL = "https://anchor.fm/totally-average-gamers"
PODCAST_IMG_URL = "https://s3-us-west-2.amazonaws.com/anchor-generated-image-bank/production/" + \
    "podcast_uploaded_nologo400/11978152/11978152-1610747060322-634d739912be4.jpg"


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
                color=EMBED_COLOR
            )

            await ctx.send(embed=embed)

        else:
            await ctx.send("Need a video here")

    @bot.command(name="podcast", help="Gets the public URL of the Totally Average Gamers podcast")
    async def send_podcast(ctx):
        logger.info(bot.user.avatar_url)
        embed = discord.Embed(
            title="The Totally Average Gamers Podcast",
            url=PODCAST_URL,
            color=EMBED_COLOR
        )

        embed.set_image(url=PODCAST_IMG_URL)
        embed.set_author(name="Totally Average Gamers", icon_url=bot.user.avatar_url)

        await ctx.send(
            "Check out the latest episodes of the Totally Average Gamers podcast!",
            embed=embed
        )
