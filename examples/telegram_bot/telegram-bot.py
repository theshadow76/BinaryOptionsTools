import requests

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from dotenv import load_dotenv
import os
load_dotenv()

def make_request(pair: str, action: str, amount: int, time_frame: int):
    data = {
        "pair": pair,
        "action": action,
        "time_frame": time_frame,
        "amount": amount
    }
    url = "http://localhost:3000/pocketoption"
    headers = {
        "Content-Type": "application/json",
    }
    return requests.post(url, headers=headers, json=data)


def get_args():
    token = os.getenv("TOKEN")
    time_frame = int(os.getenv("TIME_FRAME", default= 60)) # It expects it to be an integer representing seconds
    amount = int(os.getenv("AMOUNT", default=10)) # The amount of dollars to trade
    return token, time_frame, amount


def parser(text: str) -> tuple[str, str] | None: 
    try:
        pair = text.split(":")[1].strip().split(" ")[0].replace("/", "") + "_otc"
        if "ПРОДАВАТЬ" in text or "🔴" in text:
            option = "put"
        elif "ПОКУПАТЬ" in text or "🟢" in text:
            option = "call"
        else:
            return None
        return pair, option
    except Exception as e:
        print("ERROR:", e)
    

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global time_frame, amount, api
    print("Recieved message:", update.message.text)
    parsed = parser(update.message.text)
    if isinstance(parsed, tuple):
        pair, option = parsed[0], parsed[1]

        response = make_request(pair, option, amount, time_frame)
        print(response.text)
        return        
    return

if __name__ == "__main__":
    token, time_frame, amount = get_args()
    
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT, handler))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    # tests = [
    #     """Валютная пара: EUR/JPY 🇪🇺/🇯🇵
    #     Сигнал: ПРОДАВАТЬ 🔴
    #     Текущая цена: 165.964
    #     Время опциона: 1 минут ⏱️
    #     """,
    #     """
    #     Валютная пара: AUD/USD 🇦🇺/🇺🇸
    #     Сигнал: ПОКУПАТЬ 🟢
    #     Текущая цена: 0.65744
    #     Время опциона: 1 минут ⏱️
    #     """,
    #     """
    #     Валютная пара: EUR/USD 🇪🇺/🇺🇸Сигнал: ПРОДАВАТЬ 🔴
    #     Текущая цена: 1.08307Время опциона: 1 минут ⏱️
    #     """
    # ]
    # for test in tests:
    #     print(parser(test))