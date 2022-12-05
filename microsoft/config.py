from pydantic import BaseSettings


class Settings(BaseSettings):
    number_of_fifo: int = 5

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "settings_"
