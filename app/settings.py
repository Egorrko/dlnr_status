import json
from datetime import timedelta, timezone
from dateutil import tz
from pathlib import Path
from typing import List, Optional

from model import Server
from pydantic import BaseSettings, validator

SETTINGS_PATH = 'settings.json'


class Settings(BaseSettings):
    BOT_TOKEN: str
    CHANNEL_USERNAME: str
    MESSAGE_ID: int
    TIMEZONE: tz.tzfile
    SERVERS: List[Server]

    @validator('TIMEZONE', pre=True)
    def prepare_timezone(cls, value):
        if value:
            return tz.gettz(value)

    class Config:
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings,):
            return (lambda _: json.loads(Path(SETTINGS_PATH).read_bytes()),)

    def save(self):
        Path(SETTINGS_PATH).write_text(self.json(ensure_ascii=False, indent=2), encoding='utf-8')


settings = Settings()
