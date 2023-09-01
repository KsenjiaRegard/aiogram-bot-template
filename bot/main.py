from aiogram import executor
from utils.loader import dp
import handlers, middlewares, filters
from utils.notification.notify_admins import on_startup_notify

async def on_startup(dispatcher):
	await on_startup_notify(dispatcher)

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup)