#Copyright 2024-present, Author: MrTamilKiD

import re
import time
import asyncio
import requests
import feedparser

from bs4 import BeautifulSoup as bs
from pyrogram import Client

from MrTamilKiD.tools.db import u_db
from config import Config

async def tamilmv_rss_feed(bot: Client):
    feed = feedparser.parse(Config.TAMILMV+"index.php?/discover/all.xml/")
    count = 0
    data = []
    global real_dict
    real_dict = {}
    for entry in feed.entries:
        if count >= 20:
            break
        count += 1
        data.append(entry.link)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }
    for url in data:
        html = requests.request("GET", url , headers=headers)
        soup = bs(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])

        for title in big_title:
            if title.find('span') == None:
                pass
            else:
                if title.find('span').text.endswith('torrent'):
                    all_titles.append(title.find('span').text[19:-8])

        for p in range(0, len(mag)):
            try:
                if not await u_db.is_tamilmv_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=Config.TAMILMV_LOG,
                        text=f"<code>/ql {file_link[p]}</code> \n\n <b>{all_titles[p]}</b> \n <b>Updated on <a href='https://t.me/KR_BotX'>TamilMV</a></b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tamilmv(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass


async def tamilblasters_rss_feed(bot: Client):
    feed = feedparser.parse(Config.TAMILBLAST+"index.php?/discover/all.xml/")
    count = 0
    data = []
    global real_dict
    real_dict = {}
    for entry in feed.entries:
        if count >= 40:
            break
        count += 1
        data.append(entry.link)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }
    for url in data:
        html = requests.request("GET", url , headers=headers)
        soup = bs(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])
            all_titles.append(re.sub(r'www\.[a-z0-9.\-]+', '', a.text, flags=re.IGNORECASE).replace('.torrent', '').replace('-', '', 1).replace(' ', '', 2))

        for p in range(0, len(mag)):
            try:
                if not await u_db.is_tb_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=Config.TAMILBLAST_LOG,
                         text=f"<code>/ql {file_link[p]}</code> \n\n <b>{all_titles[p]}</b> \n <b>Updated on <a href='https://t.me/KR_BotX'>TamilBlasters</a></b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tb(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass


# TamilRockers RSS Feed Scraper Function

async def tamilrockers_rss_feed(bot: Client):
    feed = feedparser.parse(Config.TAMILROCKERS+"index.php?/discover/all.xml/")
    count = 0
    data = []
    global real_dict
    real_dict = {}
    for entry in feed.entries:
        if count >= 40:
            break
        count += 1
        data.append(entry.link)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }
    for url in data:
        html = requests.request("GET", url , headers=headers)
        soup = bs(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])
            all_titles.append(re.sub(r'www\.[a-z0-9.\-]+', '', a.text, flags=re.IGNORECASE).replace('.torrent', '').replace('-', '', 1).replace(' ', '', 2))

        for p in range(0, len(mag)):
            try:
                if not await u_db.is_tr_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=Config.TAMILROCKERS_LOG,
                         text=f"<code>/ql {file_link[p]}</code> \n\n <b>{all_titles[p]}</b> \n <b>Updated on <a href='https://t.me/KR_BotX'>TamilRockers</a></b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tr(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass
