from config import bot, SEND_TEXT

from BitlyAPI import shorten_url
from BitlyAPI.exceptions import BitlyException, BitlyApiNotWorking

from pyrogram import filters
from pyrogram.types import Message


@bot.on_message(filters.private & filters.command("start"))
async def start_(_, msg: Message):
    await msg.reply(
        SEND_TEXT.format(msg.from_user.mention),
        disable_web_page_preview=True
    )


@bot.on_message(filters.private & filters.command("help"))
async def help_(_, msg: Message):
    await msg.reply(
        SEND_TEXT.format(msg.from_user.mention),
        disable_web_page_preview=True
    )


@bot.on_message(filters.private & filters.text)
async def reply_bitly_link(_, msg: Message):
    try:
        url = msg.text
        shortened_url = shorten_url(url)
        await msg.reply(
            f"**Shortened Url:**\n`{shortened_url}`",
            disable_web_page_preview=True
        )
    except BitlyException as err:
        await msg.reply(f"**ERROR:** `{str(err)}`")
    except BitlyApiNotWorking:
        await msg.reply("Bitly API is Down!")


if __name__ == "__main__":
    bot.run()