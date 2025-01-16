from aiogram import types, Dispatcher,Bot,executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
first = KeyboardButton(text='id')
second = KeyboardButton(text='lastname')
thrid = KeyboardButton(text='firstname')
fourth = KeyboardButton(text='username')
main_menu.add(first,second)
main_menu.add(thrid,fourth)

api='7051245348:AAGiwFpJ3sG9qrNRxo7jJORTJfVDIRkR_nE'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(text='id')
async def send_first(sms:types.Message):
    await sms.answer(text=f'Sizdin ID iniz:{sms.from_id}')

@dp.message_handler(text='lastname')
async def send_second(sms:types.Message):
    await sms.answer(text=f'Sizdin telegramdagi atiniz:{sms.from_user.last_name}')

@dp.message_handler(text='firstname')
async def send_thrid(sms:types.Message):
    await sms.answer(text=f'Sizdin telegramdagi atiniz:{sms.from_user.first_name}')

@dp.message_handler(text='username')
async def send_fourt(sms:types.Message):
    await sms.answer(text=f'Sizdin telegramdagi username:{sms.from_user.username}')

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Baslaw',reply_markup=main_menu)

if __name__=='__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)