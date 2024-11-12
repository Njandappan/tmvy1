#Copyright 2024-present, Author: MrTamilKiD

import time
from typing import Union
from pyrogram import Client as pyClient
from pyrogram.storage import Storage
from config import Config, LOGGER
from MrTamilKiD.tools.rss import tamilmv, tamilblasters, tamilrockers
from MrTamilKiD.tools.rss_feed import tamilmv_rss_feed, tamilblasters_rss_feed, tamilrockers_rss_feed

class Client(pyClient):
    """ Custom Bot Class """

    def init(self, session_name: Union[str, Storage] = "TamilMVAutoRss-Bot"):
        super().init(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="MrTamilKiD/plugins"
            )
        )

    async def start(self):
        await super().start()
        LOGGER.info("Bot Started!")
        for chat in Config.TAMILMV_LOG, Config.TAMILBLAST_LOG:
            await self.send_message(chat, "Bot Started!")
        while True:
            print("TamilMV Scraper Running...")
            # await tamilmv(self)
            # time.sleep(30)
            print("TamilMV RSS Feed Running...")
            await tamilmv_rss_feed(self)
            time.sleep(150) 
            print("TamilBlasters Scraper Running...")
            # await tamilblasters(self)
            # time.sleep(30)
            print("TamilBlasters RSS Feed Running...")
            await tamilblasters_rss_feed(self)
            time.sleep(150)
            # print("TamilRockers Scraper Running...")
            # await tamilrockers(self)
            # time.sleep(30)
            # print("TamilRockers RSS Feed Running...")
            # await tamilrockers_rss_feed(self)
            print("Sleeping for 5 minutes...")
            time.sleep(300)

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("Bot Stopped!")
