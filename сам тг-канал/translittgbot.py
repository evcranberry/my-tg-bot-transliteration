import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message 
from aiogram.filters.command import Command

bot = Bot('7147966252:AAHg8QtPOqWfnUqWdNvpUXkry0zSg1OnYAQ')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

base_url = 'https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/'

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = (f'Добрый день, {user_name}! Вас приветствует transliteration bot. Я принимаю в качестве сообщений ФИО в кириллице и отдаю ФИО на латинице [в соответствии с Приказом МИД России от 12.02.2020 № 2113](https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/)')
    logging.info(f'{user_name}: {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text, parse_mode='Markdown')

trans_dict = {
    'а' : 'a',
    'б' : 'b',
    'в' : 'v',
    'г' : 'g',
    'д' : 'd',
    'е' : 'e',
    'ё' : 'e',
    'ж' : 'zh',
    'з' : 'z',
    'и' : 'i',
    'й' : 'i',
    'к' : 'k',
    'л' : 'l',
    'м' : 'm',
    'н' : 'n',
    'о' : 'o',
    'п' : 'p',
    'р' : 'r',
    'с' : 's',
    'т' : 't',
    'у' : 'u',
    'ф' : 'f',
    'х' : 'kh',
    'ц' : 'ts',
    'ч' : 'ch',
    'ш' : 'sh',
    'щ' : 'shch',
    'ь' : '',
    'ы' : 'y',
    'ъ' : 'ie',
    'э' : 'e',
    'ю' : 'yu',
    'я' : 'ia'
}
def trans_com(name):
    eng_name = ''
    for char in name:
        if char.lower() in trans_dict:
            if char.islower():
                eng_name += trans_dict[char]
            else:
                eng_name += trans_dict[char.lower()].upper()
        else:
            eng_name += char
    return eng_name

@dp.message()
async def tranliterate(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name}: {user_id} отправил текст: {text}')
    await message.answer(text=trans_com(text))

if __name__ == '__main__': 
    dp.run_polling(bot)

