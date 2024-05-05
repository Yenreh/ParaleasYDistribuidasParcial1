import multiprocessing
import threading
from datetime import datetime
from helper import *
from api_youtube_manager import *

CONFIG_PATH = 'config/config.json'
YT_DLP_PATH = 'output/yt-dlp'
DOWNLOADS_PATH = 'output/downloads'
LOG_PATH = 'output/log.log'
APP_CONFIG = loadJSON(CONFIG_PATH)

youtube_api_key = APP_CONFIG.get("youtube_api_key")
youtube_channel_list = APP_CONFIG.get("youtube_channel_list")
youtube_dlp_download_link = APP_CONFIG.get("ytdlp_download_link")

test_channel_id = "UC6nSFpj9HTCZ5t-N3Rm3-HA"
test_videos = [{'url': 'https://www.youtube.com/watch?v=u1Ijupdjv_I', 'title': 'How To Make Galinstan', 'published_at': '2024-05-02T20:17:10Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=7ByBcO9w6QQ', 'title': 'Words That Look Similar ON YOUR LIPS', 'published_at': '2024-04-26T18:10:57Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=VWO6lbJX-h0', 'title': "A Book That Didn't Age Well", 'published_at': '2024-04-24T18:30:17Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=Tx4qr9x1MrI', 'title': 'A trick that always works...', 'published_at': '2024-04-22T20:42:44Z', 'channel_name': 'Vsauce'}, {'url': 'https://www.youtube.com/watch?v=aAGvGbSoWVc', 'title': 'The Oldest Camera Photograph', 'published_at': '2024-04-20T16:11:43Z', 'channel_name': 'Vsauce'}]

downloadFile(youtube_dlp_download_link, YT_DLP_PATH)


def downloadVideo(video, downloads_path, yt_dl_path):
    video_url = video.get("url")
    video_output = f"{downloads_path}/{video.get('channel_name')} - {video.get('title')}.mp4"
    audio_output = f"{downloads_path}/{video.get('channel_name')} - {video.get('title')}.mp3"
    downloadMP4Video(url=video_url, video_output=video_output, yt_dl_path=yt_dl_path)
    convertToMP3(input_file=video_output, output_file=audio_output)
    log_message = f"Video: {video.get('title')} - Channel: {video.get('channel_name')} - Published At: {video.get('published_at')} - Downloaded at: {datetime.now()}"
    saveLog(log_message=log_message, file_path=LOG_PATH)


def downloadVideosSequential(youtube_channel_list, youtube_api_key):
    for channel in youtube_channel_list:
        # channel_id = channel.get("channel_id") if channel.get("channel_has_id") else get_channel_id(youtube_api_key, channel.get("channel_id"))
        # videos = get_latest_videos(api_key=youtube_api_key, channel_id=channel_id)
        videos = test_videos
        for video in videos:
            downloadVideo(video, DOWNLOADS_PATH, YT_DLP_PATH)

def downloadVideosMultiThreaded(youtube_channel_list, youtube_api_key, num_threads):
    threads = []
    for channel in youtube_channel_list:
        # channel_id = channel.get("channel_id") if channel.get("channel_has_id") else get_channel_id(youtube_api_key, channel.get("channel_id"))
        # videos = get_latest_videos(api_key=youtube_api_key, channel_id=channel_id)
        videos = test_videos
        for video in videos:
            if len(threads) < num_threads:
                thread = threading.Thread(target=downloadVideo, args=(video, DOWNLOADS_PATH, YT_DLP_PATH))
                thread.start()
                threads.append(thread)
            else:
                for thread in threads:
                    thread.join()
                threads = []
                thread = threading.Thread(target=downloadVideo, args=(video, DOWNLOADS_PATH, YT_DLP_PATH))
                thread.start()
                threads.append(thread)
    for thread in threads:
        thread.join()

def downloadVideosMultiProcessing(youtube_channel_list, youtube_api_key, num_processes):
    processes = []
    for channel in youtube_channel_list:
        # channel_id = channel.get("channel_id") if channel.get("channel_has_id") else get_channel_id(youtube_api_key, channel.get("channel_id"))
        # videos = get_latest_videos(api_key=youtube_api_key, channel_id=channel_id)
        videos = test_videos
        for video in videos:
            if len(processes) < num_processes:
                process = multiprocessing.Process(target=downloadVideo, args=(video, DOWNLOADS_PATH, YT_DLP_PATH))
                process.start()
                processes.append(process)
            else:
                for process in processes:
                    process.join()
                processes = []
                process = multiprocessing.Process(target=downloadVideo, args=(video, DOWNLOADS_PATH, YT_DLP_PATH))
                process.start()
                processes.append(process)
    for process in processes:
        process.join()

