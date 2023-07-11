from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_polling
from handlers import SetupHandlers

def main():
    bot = Bot("6343032238:AAEJrU6jrdiixvF7cSJCfiUcKoMMR6czrdo")
    dp = Dispatcher(bot)
    start_polling(dp, on_startup=OnStartUp)

async def OnStartUp(dp):
    SetupHandlers(dp)
    print("Bot started")

main()