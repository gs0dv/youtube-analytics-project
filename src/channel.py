import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        # id канала
        self.__channel_id = self.channel['items'][0]['id']
        # название канала
        self.title = self.channel['items'][0]['snippet']['title']
        # описание канала
        self.description = self.channel['items'][0]['snippet']['description']
        # ссылка на канал
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        # количество подписчиков
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        # количество видео
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        # общее количество просмотров
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return cls.youtube

    def print_info(self) -> str:
        """Возвращает информацию о канале."""
        return json.dumps(self.channel, indent=2, ensure_ascii=False)

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""

        attributes_chanel = {'channel_id': self.channel_id,
                             'title': self.title,
                             'description': self.description,
                             'url': self.url,
                             'subscriber_count': self.subscriber_count,
                             'video_count': self.video_count,
                             'view_count': self.view_count}

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(attributes_chanel, file, indent=4)

    def __repr__(self):
        return f"Channel ({self.channel_id})"
