from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from .routers import default_router, stars_parsing_router
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
dp.include_routers(default_router, stars_parsing_router,)
bot_commands = [
    BotCommand(command="/start", description="Start working"),
    BotCommand(command="/students_stars", description="Get all students stars"),
]

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(bot_commands)
    # bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


