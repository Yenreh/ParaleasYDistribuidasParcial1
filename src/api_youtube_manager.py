from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration
import html


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


def get_latest_videos(api_key, channel_id, min_duration=None, max_results=5):
    youtube = build('youtube', 'v3', developerKey=api_key)
    try:
        # Initialize list to store valid video URLs and their details
        video_data = []
        # Keep fetching videos until we have enough
        next_page_token = None
        while len(video_data) < max_results:
            # Obtain the list of videos from the channel
            videos = youtube.search().list(
                part='id,snippet',
                channelId=channel_id,
                order='date',
                maxResults=max_results,
                type='video',
                pageToken=next_page_token
            ).execute()

            # Extract the IDs of video and their details
            for item in videos['items']:
                video_id = item['id']['videoId']
                channel_name = item['snippet']['channelTitle']
                title = item['snippet']['title']
                published_at = item['snippet']['publishedAt']

                # Get video details including duration
                video_details = youtube.videos().list(
                    part='contentDetails',
                    id=video_id
                ).execute()

                duration_str = video_details['items'][0]['contentDetails']['duration']
                duration = parse_duration(duration_str)

                # Check if duration is greater than min_duration
                if min_duration is None or duration.total_seconds() > min_duration:
                    video_data.append({
                        'url': 'https://www.youtube.com/watch?v=' + video_id,
                        'title': html.unescape(title),
                        'published_at': published_at,
                        'channel_name': channel_name
                    })

            # Update nextPageToken for next page of results
            next_page_token = videos.get('nextPageToken')

            # Break the loop if there are no more pages
            if not next_page_token:
                break

        return video_data[:max_results]

    except HttpError as e:
        print("Error:", e)
        return None