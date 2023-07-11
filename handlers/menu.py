from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from texts import btn1,btn2,btn3

async def menumessage(m:Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton(btn1))
    keyboard.row(KeyboardButton(btn2))
    keyboard.row(KeyboardButton(btn3))
    await m.answer("Выберите действие:", reply_markup=keyboard)

def SetupMenu(dp):
    dp.register_message_handler(menumessage, commands="start")