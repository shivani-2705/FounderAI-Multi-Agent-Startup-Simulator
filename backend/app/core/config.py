from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str

    environment: str

    debug: bool

    host: str
    port: int

    api_v1_prefix: str

    database_url: str

    ollama_host: str

    llm_provider: str

    llm_model: str

    llm_temperature: float

    llm_timeout: int

    log_level: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()