from aiogram import types, Dispatcher,Bot,executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

awqat_menyu = InlineKeyboardMarkup()
lavash = InlineKeyboardButton(text='lavash🫔',callback_data='lv')
burger = InlineKeyboardButton(text='burger🍔',callback_data='bg')
fastfood = InlineKeyboardButton(text='fastfood🌭',callback_data='fast')
awqat_menyu.add(lavash,burger,fastfood)

pitsa = InlineKeyboardButton(text='pitsa🍕',callback_data='pizza')
awqat_menyu.add(pitsa)

ishimlik_menyu= InlineKeyboardMarkup()
vino = InlineKeyboardButton(text='Vino🥂')
chay = InlineKeyboardButton(text='Chay🍵')
suw = InlineKeyboardButton(text='Suw🥛')
ishimlik_menyu.add(vino,chay,suw)

pitsa_menyu = InlineKeyboardMarkup()
Pepperoni = InlineKeyboardButton(text='Pepperoni',callback_data='peppi')
Margaritto = InlineKeyboardButton(text='Margaritto',callback_data='mar')
Chessy = InlineKeyboardButton(text='Chessy',callback_data='chesy')
pitsa_menyu.add(Pepperoni,Margaritto,Chessy)

lavash_menyu= InlineKeyboardMarkup()
shashlikli = InlineKeyboardButton(text='Shashlikli',callback_data='shsh')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
first = KeyboardButton(text='awqatlar')
second = KeyboardButton(text='ishimlik')
thrid = KeyboardButton(text='biz tuwrali')
fourth = KeyboardButton(text='Baylanis ushin')
main_menu.add(first,second,thrid)
main_menu.add(fourth)

api='7950346740:AAEJk51uIIiicKhCqCDPdUKJB8JWieyS6gM'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(text='awqatlar')
async def send_first(sms:types.Message):
    await sms.answer(text='Bizde tomendegi awqatlar bar',reply_markup=awqat_menyu)

@dp.message_handler(text='🥤ishimlik🧋')
async def send_first(sms:types.Message):
    await sms.answer(text='Bizde tomendegi ishimlikler bar',reply_markup=ishimlik_menyu)

@dp.message_handler(text='🔍biz tuwrali🔍')
async def send_first(sms:types.Message):
    await sms.answer(text='Safia restorani\n')

@dp.message_handler(text='📱Baylanis ushin📱')
async def send_fourt(sms:types.Message):
    await sms.answer(text='Administrator:996542321\ninsta:@sofiii')

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Assalamu aleykum',reply_markup=main_menu)

@dp.callback_query_handler()
async def send_callback(call:types.CallbackQuery):
    data = call.data
    if data=='pizza':

        await call.answer(text='Siz pitsa sayladiniz')
        await call.message.answer(
            text='Siz tomendegi pitsalardin birin saylasaniz boladi:',
            reply_markup=pitsa_menyu
            )
    elif data=='peppi':

        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='photo_2024-12-26_12-00-25.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='bahasi: 60 000 swm')
    elif data=='mar':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='photo_2024-12-26_12-00-25.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='bahasi: 70 000 swm')
    elif data=='chesy':

        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='photo_2024-12-26_12-00-25.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='bahasi: 80 000 swm'
        )


if __name__=='__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)