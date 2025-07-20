import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # This tells Pydantic to load settings from a file named .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

    # Define your settings here
    # The type hint (str) is important for validation
    DATABASE_URL: str
    # === ADD THESE JWT SETTINGS ===
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

# Create a single instance of the settings to be used throughout the app
settings = Settings()