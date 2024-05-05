from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_channel_id(api_key, username):
    youtube = build('youtube', 'v3', developerKey=api_key)
    try:
        # Buscar el canal por su nombre de usuario
        search_response = youtube.search().list(
            q=username,
            part='snippet',
            type='channel'
        ).execute()

        # Extraer el ID del canal de la respuesta
        channel_id = search_response['items'][0]['snippet']['channelId']

        return channel_id

    except Exception as e:
        print("Error:", e)
        return None


def get_latest_videos(api_key, channel_id, max_results=5):
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        # Obtener la lista de videos del canal
        videos = youtube.search().list(
            part='id',
            channelId=channel_id,
            order='date',
            maxResults=max_results,
            type='video'
        ).execute()

        # Extraer las IDs de video
        video_ids = [item['id']['videoId'] for item in videos['items']]

        # Construir las URLs de los videos
        video_urls = ['https://www.youtube.com/watch?v=' + video_id for video_id in video_ids]

        return video_urls

    except HttpError as e:
        print("Error:", e)
        return None
