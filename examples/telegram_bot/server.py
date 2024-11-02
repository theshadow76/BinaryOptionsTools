from robyn import Robyn, Request, Response, Headers
from BinaryOptionsTools import pocketoption
import nest_asyncio
nest_asyncio.apply()


def get_args():
    ssid = input("Enter your ssid: ")
    demo = not bool(int(input("Do you want to use demo or real account? (0: demo, 1: real) ")))
    if demo:
        print("DEMO")
    else:
        print("REAL")
    return ssid, demo
app = Robyn(__file__)
ssid, demo = get_args()
api = pocketoption(ssid, demo)


@app.post("/pocketoption")
async def handler(request: Request):
    global api
    body = request.json()
    pair = body["pair"]
    action = body["action"]
    time_frame = int(body.get("time_frame", 60))
    amount = int(body.get("amount", 10))
    
    if action == "put":
        api.Put(amount, pair, time_frame)
    else:
        api.Call(amount, pair, time_frame)
        
    return Response(status_code=200, headers=Headers({}), description="OK")




if __name__ == "__main__":
    app.start(port=3000)

