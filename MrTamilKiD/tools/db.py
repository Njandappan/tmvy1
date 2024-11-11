#Copyright 2024-present, Author: MrTamilKiD

import datetime
import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.users = self.db.UsersData
        self.black = self.db.TamilMV_List
        self.tb = self.db.TamilBlaster_List
        self.tr = self.db.TamilRockers_List

    def tamilmv(self, Name, link, url):
        return dict(
            FileName = Name,
            magnet_link = link,
            magnet_url = url,
            upload_date=datetime.date.today().isoformat()
        )

    async def add_tamilmv(self, Name, link, url):
        user = self.tamilmv(Name, link, url)
        await self.black.insert_one(user)

    async def is_tamilmv_exist(self, Name, link, url):
        user = await self.black.find_one({'magnet_url': url})
        return True if user else False

    def tbx(self, Name, link, url):
        return dict(
            FileName = Name,
            magnet_link = link,
            magnet_url = url,
            upload_date=datetime.date.today().isoformat()
        )

    async def add_tb(self, Name, link, url):
        user = self.tbx(Name, link, url)
        await self.tb.insert_one(user)

    async def is_tb_exist(self, Name, link, url):
        user = await self.tb.find_one({'magnet_url': url})
        return True if user else False

    # TamilRockers DB Functions

    def tr(self, Name, link, url):
        return dict(
            FileName = Name,
            magnet_link = link,
            magnet_url = url,
            upload_date=datetime.date.today().isoformat()
        )

    async def add_tr(self, Name, link, url):
        user = self.tr(Name, link, url)
        await self.tr.insert_one(user)

    async def is_tr_exist(self, Name, link, url):
        user = await self.tr.find_one({'magnet_url': url})
        return True if user else False

u_db = Database(Config.DB_URL, Config.DB_NAME)