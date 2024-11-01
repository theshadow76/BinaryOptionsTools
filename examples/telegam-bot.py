from wonda import Bot, Message
from BinaryOptionsTools import pocketoption



def get_args():
    ssid = input("Enter your ssid: ")
    demo = not bool(input("Do you want to use demo or real account? (0: demo, 1: real)"))
    token = input("Enter your telegram token: ")
    return ssid, demo, token

def get_bot(token: str, api): 
    bot = Bot(token)
    
    @bot.on.message
    async def handler(m: Message) -> None:
        if isinstance(m.text, str):
            text = m.text
            if text.startswith("/pocketoption"):
                option = text.split(" ")[1]
                active = text.split(" ")[2]
                amount = int(text.split(" ")[3])
                time = int(text.split(" ")[4])
                if option == "put":
                    api.Put(amount, active, time)
                    return await m.answer(f"Made a `put` trade on {active}")
                elif option == "call":
                    api.Call(amount, active, time)
                    return await m.answer(f"Made a `call` trade on {active}")
            
        await m.answer("Hello world!")
    return bot 

if __name__ == "__main__":
    ssid, demo, token = get_args()
    api = pocketoption(ssid, demo)
    bot = get_bot(token, api)
    bot.run_forever()
