ENV_DISCORD_TOKEN = 'DISCORD_TOKEN'
ENV_YOUTUBE_API_KEY = 'YOUTUBE_API_KEY'
ENV_YOUTUBE_CHANNEL_ID = 'YOUTUBE_CHANNEL_ID'

DISCORD_WELCOME_MSG_TITLE = 'Welcome to the Totally Average Gamers'
DISCORD_WELCOME_MSG_BODY = '**Welcome %s!** We are so excited that you have joined our ' + \
            'community. Our Totally Average Mods and Team are here to answer any questions you ' + \
            'might have and to keep this place safe and respectful. Use !help in any channel to ' + \
            'see how Totally Average Bot can assist you. \n\nPlease take a moment to read over ' + \
            'the rules in <#%s> and react to get access to the community and then feel ' + \
            'free to introduce yourself and join in the conversation!\n\n Thank you, \nThe Totally Average Gamers Team'

YOUTUBE_LATEST_REQUEST_URI = 'https://www.googleapis.com/youtube/v3/search?key=%s&part=snippet&' + \
            'channelId=%s&order=date&type=video'

YOUTUBE_ERROR_MSG = 'Uh-oh... Looks like I can\'t get the latest YouTube post. Try again later.'
YOUTUBE_NO_VID_MSG = 'I can\'t seem to find any recent videos on YouTube... how average :neutral_face:'
YOUTUBE_MSG = 'Check out our latest video on YouTube!'

PODCAST_URL = 'https://anchor.fm/totally-average-gamers'
PODCAST_IMG_URL = 'https://s3-us-west-2.amazonaws.com/anchor-generated-image-bank/production/' + \
            'podcast_uploaded_nologo400/11978152/11978152-1611774431960-61630a52af02f.jpg'
PODCAST_MSG = 'Check out the latest episodes of the Totally Average Gamers podcast!'

EMBED_COLOR = 0x36457A

CHANNEL_INFO = {
    'general': 'This is a test',
}
