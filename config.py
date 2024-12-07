#Copyright 2024-present, Author: MrTamilKiD

import os
import logging
from logging.handlers import RotatingFileHandler

# Logging >>>
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# Invoke Data >>>
class Config:
    API_ID = int(os.environ.get("API_ID", "11329245"))
    API_HASH = os.environ.get("API_HASH", "90988dcdd5ddd4d0a28843a1e2605924")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7659191951:AAGht2-znb4u99CI3zJklD9ikhFr8yDYEBk")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1364321375))
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Tmvrss:Tmvrss@cluster0.zakos.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    # RSS Feed URL
    TAMILMV = os.environ.get("TMV", "https://www.1tamilmv.at/")
    TAMILBLAST = os.environ.get("TB", "https://www.1tamilblasters.my/")
    TAMILROCKERS = os.environ.get("TR", "https://2tamilrockers.com/")
    # log channel list
    TAMILMV_LOG = os.environ.get("TMV_LOG", -1002308254593)
    TAMILBLAST_LOG = os.environ.get("TB_LOG", -1002308254593)
    TAMILROCKERS_LOG = os.environ.get("TR_LOG", -1002308254593)




