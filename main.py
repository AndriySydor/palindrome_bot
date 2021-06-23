import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

# log level
logging.basicConfig(level=logging.INFO)

# initialisation of the bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# palindrome checking function
def palindrome(text):
    text = text.lower()
    text = list(text)
    for i in range(0, int(len(text) / 2)):
        if text[i] != text[0 - i - 1]:
            return False
    return True


# 'start' command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI can tell if your word is a palindrome!")


# 'palindrome' command
@dp.message_handler(commands=['description'])
async def send_ask(message: types.Message):
    await message.reply("Please enter the word and bot will answer whether it is a palindrome or not")


# palindrome checking in the chat
@dp.message_handler(content_types=['text'])
async def send_palindrome(message: types.Message):
    if palindrome(message.text):
        await message.answer("This is really palindrome!")
    else:
        await message.answer("Sorry, this is not a palindrome((")


# long polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
