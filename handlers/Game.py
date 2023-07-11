from aiogram.types import Message
import random
from texts import btn1, btn2, btn3

async def Game(m:Message):
    variants = [btn1, btn2, btn3]
    bot_value = random.randint(0,2)
    if (bot_value == 0 and m.text == btn2) or (bot_value == 1 and m.text == btn3) or (bot_value == 2 and m.text == btn1):
        await m.answer(f'Вы проиграли :( \nЯ выбрал {variants[bot_value]}')
    elif m.text == variants[bot_value]:
        await m.answer(f'Ничья\nЯ выбрал {variants[bot_value]}')
    else:
        await m.answer(f'Вы выиграли! :)))\nЯ выбрал {variants[bot_value]}')

def setup_Game(dp):
    dp.register_message_handler(Game, text = [btn1, btn2, btn3])