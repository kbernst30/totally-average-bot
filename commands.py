import aiohttp
import constants
import discord
import logging
import os

from bot import TotallyAverageBot
from discord.ext import commands
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def register_commands(bot: TotallyAverageBot):
    load_dotenv()

    @bot.command(name="video", help="Gets the URL of the latest YouTube video")
    async def send_latest_video(ctx: commands.Context):
        logger.info(f'!video command received by {ctx.author}')
        if bot.youtube_api_key is None:
            logger.warn("Cannot attempt YouTube API request... perhaps API key is missing...")
            await ctx.send(constants.YOUTUBE_ERROR_MSG)
            return

        youtube_channel_id = os.getenv(constants.ENV_YOUTUBE_CHANNEL_ID)
        youtube_request_uri = constants.YOUTUBE_LATEST_REQUEST_URI % (bot.youtube_api_key, youtube_channel_id)

        async with aiohttp.ClientSession() as session:
            async with session.get(youtube_request_uri) as response:
                response_js = await response.json()
                latest_youtube_videos = response_js['items']

        if len(latest_youtube_videos) == 0:
            embed = discord.Embed(
                description=constants.YOUTUBE_NO_VID_MSG,
                color=constants.EMBED_COLOR
            )

            await ctx.send(embed=embed)

        else:
            # First video in list is latest based on YouTube documentation
            latest_video = latest_youtube_videos[0]

            # ID is an object that looks like this: {'kind': 'youtube#video', 'videoId': 'k--qYwSMWDQ'}
            video_id = latest_video['id']['videoId']
            video_snippet = latest_video['snippet']
            video_title = video_snippet['title']
            video_description = video_snippet['description']

            # TODO Check if High exists? or if should use default?
            video_thumbnail = video_snippet['thumbnails']['high']['url']

            embed = discord.Embed(
                title=video_title,
                url='https://youtube.com/watch?v=%s' % video_id,
                description=video_description,
                color=constants.EMBED_COLOR
            )

            embed.set_image(url=video_thumbnail)
            embed.set_author(name="Totally Average Gamers", icon_url=bot.user.avatar_url)

            await ctx.send(constants.YOUTUBE_MSG, embed=embed)

    @bot.command(name="podcast", help="Gets the public URL of the Totally Average Gamers podcast")
    async def send_podcast(ctx: commands.Context):
        logger.info(f'!podcast command received by {ctx.author}')
        embed = discord.Embed(
            title="The Totally Average Gamers Podcast",
            url=constants.PODCAST_URL,
            color=constants.EMBED_COLOR
        )

        embed.set_image(url=constants.PODCAST_IMG_URL)
        embed.set_author(name="Totally Average Gamers", icon_url=bot.user.avatar_url)

        await ctx.send(
            constants.PODCAST_MSG,
            embed=embed
        )
