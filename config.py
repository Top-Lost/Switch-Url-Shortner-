import os
from dotenv import load_dotenv

load_dotenv("config.env", override=True)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = (os.environ.get("ADMINS","")).split()
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME")