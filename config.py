import os

from pyrogram import Client

API_ID = int(os.environ.get("API_ID") or 0)
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

SEND_TEXT = """ Hello {},
`I am Bitly Bot to shorten links.
Send a valid link to shorten.`

This bot is a part of [Ks Projects](https://t.me/Ks_Projects).
"""

bot = Client(
    name="mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)