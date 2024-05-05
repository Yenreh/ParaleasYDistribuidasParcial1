from helper import *
from api_youtube_manager import *

CONFIG_PATH = 'config/config.json'
DOWNLOADS_PATH = 'output'
APP_CONFIG = loadJSON(CONFIG_PATH)

youtube_api_key = APP_CONFIG.get("youtube_api_key")
youtube_channel_list = APP_CONFIG.get("youtube_channel_list")
youtube_dlp_download_path = APP_CONFIG.get("ytdlp_download_link")


# Download latest yt-dlp build
downloadFile(youtube_dlp_download_path, DOWNLOADS_PATH, "yt-dlp")

print(youtube_channel_list)

# for channel in youtube_channel_list:
#     channel_id = channel.get("channel_id") if channel.get("channel_has_id") else get_channel_id(youtube_api_key, channel.get("channel_id"))
#     print(channel_id)
#     videos = get_latest_videos(api_key=youtube_api_key, channel_id=channel_id)
#     print(videos)
#
#
#
# print(get_latest_videos(api_key=youtube_api_key, channel_id="UC6nSFpj9HTCZ5t-N3Rm3-HA"))

