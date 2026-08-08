import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://app_user:app_password@mysql:3306/article")
    SERVICE_NAME: str = "article-service"
    PORT: int = int(os.getenv("PORT", 8001))

settings = Settings()