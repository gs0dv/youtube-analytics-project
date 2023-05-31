from src.channel import Channel


class Video:
    """Класс для видео из ютуба"""

    def __init__(self, id_video):
        video_response = Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=id_video
                                                       ).execute()

        # id видео
        self.id_video = id_video
        # название видео
        self.video_title = video_response['items'][0]['snippet']['title']
        # ссылка на видео
        self.url_video = f"https://www.youtube.com/watch?v={self.id_video}"
        # количество просмотров
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        # количество лайков
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title

    def __repr__(self):
        return f"{__class__.__name__}('{self.id_video}')"


class PLVideo(Video):
    """Класс для плейлиста из ютуба"""

    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist

    def __str__(self):
        return self.video_title

    def __repr__(self):
        return f"{__class__.__name__}('{self.id_video}', '{self.id_playlist}')"
