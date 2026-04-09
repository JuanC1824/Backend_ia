import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Robotransit AI")
    ENV: str = os.getenv("ENV", "development")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "defaultsecret")
    TIMEZONE: str = os.getenv("TIMEZONE", "America/Bogota")
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "https://frontend-eight-beta-69.vercel.app,http://localhost:4200,http://localhost:8080,http://127.0.0.1:4200,http://127.0.0.1:8080")
    ZAPIER_WEBHOOK_URL: str = os.getenv("ZAPIER_WEBHOOK_URL", "https://hooks.zapier.com/hooks/catch/26766525/uxipdqf/")

settings = Settings()