from pydantic_settings import BaseSettings, Field

class Settings(BaseSettings):
    """
    loads and validates api keys and other settings from environment variables or .env file
    """
    anthropic_api_key: str = Field(..., env="ANTHROPIC_API_KEY")
    logging_level: str = Field("INFO", env="LOGGING_LEVEL")
    model_name: str = Field("claude-haiku-4-5", env="MODEL_NAME")
    
    class Config:
        env_file = ".env"