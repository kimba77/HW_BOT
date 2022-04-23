from aiogram.utils import executor
from config import dp
from handlers import client, callback, callback_1, callback_2, fsmadmin, fsmadmin_register, notification
from Database import bot_db
import asyncio


async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(notification.scheduler())
    print("Bot is online")


fsmadmin.register_handler_admin(dp)
fsmadmin_register.register_handler_user(dp)
client.register_handlers_client(dp)
callback.register_handler_callback(dp)
notification.register_handler_notification(dp)
callback_1.register_handler_callback(dp)
callback_2.register_handler_callback(dp)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
