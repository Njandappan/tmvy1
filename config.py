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
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1504797855))
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "MrTamilKiD")
    # RSS Feed URL
    TAMILMV = os.environ.get("TMV", "https://www.1tamilmv.yt/")
    TAMILBLAST = os.environ.get("TB", "https://www.1tamilblasters.pm/")
    TAMILROCKERS = os.environ.get("TR", "https://2tamilrockers.com/")
    # log channel list
    TAMILMV_LOG = os.environ.get("TMV_LOG", -1002049279065)
    TAMILBLAST_LOG = os.environ.get("TB_LOG", -1002104864901)
    TAMILROCKERS_LOG = os.environ.get("TR_LOG", -1002100329635)




