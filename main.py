from aiogram import types, Dispatcher,Bot,executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

main_menyu = InlineKeyboardMarkup()
birinshi = InlineKeyboardButton(text='a',callback_data='bir')
ekinshi = InlineKeyboardButton(text='b',callback_data='eki')
ushinshi = InlineKeyboardButton(text='c',callback_data='ush')
main_menyu.add(birinshi,ekinshi,ushinshi)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
first = KeyboardButton(text='bir')
second = KeyboardButton(text='2')
thrid = KeyboardButton(text='3')
fourth = KeyboardButton(text='4')
fith = KeyboardButton(text='5')
sixth = KeyboardButton(text='6')
seventh = KeyboardButton(text='7')
eighth = KeyboardButton(text='8')
ninth = KeyboardButton(text='9')
zeroth = KeyboardButton(text='0')
main_menu.add(first,second,thrid)
main_menu.add(fourth,fith,sixth)
main_menu.add(seventh,eighth,ninth)
main_menu.add(zeroth)
api = '7714022614:AAH6SFp_gPRCT7r6UuXuMsEdk8GCxZ-IILk'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(text='bir')
async def send_first(sms:types.Message):
    await sms.answer(text='Siz 1 degen knopkani bastiniz')

@dp.message_handler(text='2')
async def send_first(sms:types.Message):
    await sms.answer(text='Qanday sorawlariniz bar')

@dp.message_handler(text='3')
async def send_first(sms:types.Message):
    await sms.answer(text='Qanday muzikalardi unatasiz')

@dp.message_handler(text='4')
async def send_first(sms:types.Message):
    await sms.answer(text='Classical')

@dp.message_handler(text='5')
async def send_first(sms:types.Message):
    await sms.answer(text='Pop')

@dp.message_handler(text='6')
async def send_first(sms:types.Message):
    await sms.answer(text='Rock')

@dp.message_handler(text='7')
async def send_first(sms:types.Message):
    await sms.answer(text='Jazz')

@dp.message_handler(text='8')
async def send_first(sms:types.Message):
    await sms.answer(text='Hip-hop')

@dp.message_handler(text='9')
async def send_first(sms:types.Message):
    await sms.answer(text='Dance')

@dp.message_handler(text='0')
async def send_photo(sms:types.Message):
    photo = open(file='photo_2024-12-26_12-00-25.jpg', mode='rb')
    await sms.reply_photo(
        photo=photo,
        caption='Bul muzika alemi'
    )

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Assalamu aleykum',reply_markup=main_menu)

@dp.message_handler(commands=['Barno'])
async def send_suwret(sms:types.Message):
    suwret = open(file='image.png', mode='rb')#read binary
    await sms.answer_photo(
        photo=suwret,
        caption='Bul python logosi')

@dp.message_handler(commands=['Salem'])
async def send_salem(sms:types.Message):
    await sms.answer(text='Qalay',reply_markup=main_menyu)   

if __name__=='__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)
