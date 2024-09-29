from BinaryOptionsTools import pocketoption
from BinaryOptionsTools.indicators.momentum import rsi

ssid = (r'42["auth",{"session":"bbqncrei2vmgaqhk0a94m3b6kk","isDemo":1,"uid":69634527,"platform":2}]')
api = pocketoption(ssid, True)
print(f"GET BALANCE: {api.GetBalance()}")

print(rsi(api, 60, "EURUSD_otc", 14))

print(api.Call(amount=1, active="EURUSD_otc", expiration=7, add_check_win=True))