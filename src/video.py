from src.channel import Channel


class Video:
    """Класс для видео из ютуба"""

    def __init__(self, id_video):
        is_data = True
        video_response = Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=id_video
                                                       ).execute()
        try:
            self.title = video_response['items'][0]['snippet']['title']
        except IndexError:
            is_data = False
        finally:
            # id видео
            self.id_video = id_video
            # название видео
            self.title = video_response['items'][0]['snippet']['title'] if is_data else None
            # ссылка на видео
            self.url_video = f"https://youtu.be/{self.id_video}" if is_data else None
            # количество просмотров
            self.view_count = video_response['items'][0]['statistics']['viewCount'] if is_data else None
            # количество лайков
            self.like_count = video_response['items'][0]['statistics']['likeCount'] if is_data else None

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{__class__.__name__}('{self.id_video}')"


class PLVideo(Video):
    """Класс для плейлиста из ютуба"""

    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{__class__.__name__}('{self.id_video}', '{self.id_playlist}')"
