import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> str:
        """Возвращает информацию о канале."""
        return json.dumps(self.channel, indent=2, ensure_ascii=False)
