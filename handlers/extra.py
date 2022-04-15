from aiogram import types, Dispatcher
from config import bot


async def secret_word(message: types.Message):
    await message.reply("Yes, my master 🙇")


async def echo_and_ban(message: types.Message):
    ban_words = ['bitch', 'damn', 'fuck']
    # if message.text.lower() in ban_words:
    #     await bot.send_message(message.chat.id,
    #                            f"Ban for the word, User: {message.from_user.full_name}")
    #     await bot.delete_message(message.chat.id,
    #                              message.message_id)
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await bot.send_message(message.chat.id,
                                   f"Ban for the word, User: {message.from_user.full_name}")
            await bot.delete_message(message.chat.id,
                                     message.message_id)
    if message.text.startswith("Pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)
    elif message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "dorei" in word.text)
    dp.register_message_handler(echo_and_ban)

async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply("1. /quiz command will start quiz series of problems\n"
                        "Whenever you press Следующая Викторина will appear next quiz\n"
                        "Note: Bot-Admin will delete cursed words, so that's why be careful")

async def hello(massage: types.Message):
    await massage.reply(text="Hello my friend\nThere is command list:\n /help\n /start\n /quiz\n 'dice' для игры с костью ")

