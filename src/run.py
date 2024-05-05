from datetime import datetime
from helper import *
from api_youtube_manager import *

CONFIG_PATH = 'config/config.json'
YTDLP_PATH = 'output/yt-dlp'
DOWNLOADS_PATH = 'output/downloads'
LOG_PATH = 'output/log.log'
APP_CONFIG = loadJSON(CONFIG_PATH)

youtube_api_key = APP_CONFIG.get("youtube_api_key")
youtube_channel_list = APP_CONFIG.get("youtube_channel_list")
youtube_dlp_download_path = APP_CONFIG.get("ytdlp_download_link")

test_channel_id = "UC6nSFpj9HTCZ5t-N3Rm3-HA"
test_videos = [{'url': 'https://www.youtube.com/watch?v=u1Ijupdjv_I', 'title': 'How To Make Galinstan', 'published_at': '2024-05-02T20:17:10Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=7ByBcO9w6QQ', 'title': 'Words That Look Similar ON YOUR LIPS', 'published_at': '2024-04-26T18:10:57Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=VWO6lbJX-h0', 'title': "A Book That Didn't Age Well", 'published_at': '2024-04-24T18:30:17Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=Tx4qr9x1MrI', 'title': 'A trick that always works...', 'published_at': '2024-04-22T20:42:44Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=aAGvGbSoWVc', 'title': 'The Oldest Camera Photograph', 'published_at': '2024-04-20T16:11:43Z', 'channel_name': 'Vsauce'}]
# Download latest yt-dlp build
# downloadFile(youtube_dlp_download_path, YTDLP_PATH)


def downloadVideosSequential(youtube_channel_list, youtube_api_key):
    for channel in youtube_channel_list:
        # channel_id = channel.get("channel_id") if channel.get("channel_has_id") else get_channel_id(youtube_api_key, channel.get("channel_id"))
        # videos = get_latest_videos(api_key=youtube_api_key, channel_id=channel_id)
        videos = test_videos
        for video in videos:
            video_url = video.get("url")
            video_output = f"{DOWNLOADS_PATH}/{video.get('channel_name')} - {video.get('title')}.mp4"
            audio_output = f"{DOWNLOADS_PATH}/{video.get('channel_name')} - {video.get('title')}.mp3"
            downloadMP4Video(url=video_url, video_output=video_output, yt_dl_path=YTDLP_PATH)
            convertToMP3(input_file=video_output, output_file=audio_output)
            log_message = f"Video: {video.get('title')} - Channel: {video.get('channel_name')} - Published At: {video.get('published_at')} - Downloaded at: {datetime.now()}"
            saveLog(log_message=log_message, file_path=LOG_PATH)


downloadVideosSequential(youtube_channel_list, youtube_api_key)