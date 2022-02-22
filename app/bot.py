from aiogram import Bot, Dispatcher
from settings import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


async def send_info_to_channel(text: str):
    if not settings.MESSAGE_ID:
        msg = await bot.send_message(settings.CHANNEL_USERNAME, text)
        settings.MESSAGE_ID = msg.message_id
        settings.save()
    else:
        await bot.edit_message_text(text, settings.CHANNEL_USERNAME, settings.MESSAGE_ID)
