import datetime

from src.channel import Channel
import isodate

from src.video import Video


class PlayList:
    """Класс для представления плейлиста"""

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        playlist_data = Channel.youtube.playlists().list(part='snippet',
                                                         id=self.id_playlist
                                                         ).execute()
        # название плейлиста
        self.title = playlist_data['items'][0]['snippet']['title']
        # ссылка на плейлист
        self.url = f"https://www.youtube.com/playlist?list={self.id_playlist}"

    def __total_duration(self):
        """Возвращает суммарную продолжительность всех видео в плейлисте"""
        total = datetime.timedelta()
        for duration in self.duration_videos():
            total += duration

        return total

    def duration_videos(self):
        """Возвращает список продолжительностей видео"""
        duration_videos = []

        for video in self.get_video_data()['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration_videos.append(duration)

        return duration_videos

    def get_video_ids(self):
        """Возвращает список id видео"""
        playlist_videos = Channel.youtube.playlistItems().list(playlistId=self.id_playlist,
                                                               part='contentDetails',
                                                               maxResults=50,
                                                               ).execute()
        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    def get_video_data(self):
        """Возвращает список данных о видео"""
        video_response = Channel.youtube.videos().list(part='contentDetails,statistics',
                                                       id=','.join(self.get_video_ids())
                                                       ).execute()
        return video_response

    def show_best_video(self):
        """Возвращает url популярного видео из плейлиста"""
        best_video_url = ""
        most_likes = 0
        for id_ in self.get_video_ids():
            video = Video(id_)
            if int(video.like_count) > int(most_likes):
                most_likes = video.like_count
                best_video_url = video.url_video

        return best_video_url

    @property
    def total_duration(self):
        """Возвращает результат приватного метода total_duration"""
        return self.__total_duration()

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{__class__.__name__}('{self.id_playlist}')"
