import os
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path)

# env var
API_KEY = os.getenv("API_KEY")
MAX_TOKEN = int(os.getenv("MAX_TOKEN"))

BOT_MAIL = os.getenv("BOT_MAIL")
BOT_MAIL_PASSWD = os.getenv("BOT_MAIL_PASSWD")

TARGET_MAIL = os.getenv("TARGET_MAIL")

DB_PATH = os.getenv("DB_PATH")  