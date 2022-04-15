from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, fsmadmin

fsmadmin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)