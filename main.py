from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config
import handlers, middlewares
from utils.notify_admins import on_startup_notify

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_startup(dispatcher):
	# Notify about launch
	await on_startup_notify(dispatcher)

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup)