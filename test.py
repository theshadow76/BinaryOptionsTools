from BinaryOptionsTools import pocketoption

ssid = (r'42["auth",{"session":"bbqncrei2vmgaqhk0a94m3b6kk","isDemo":1,"uid":69634527,"platform":2}]')
api = pocketoption(ssid, True)
print(f"GET BALANCE: {api.GetBalance()}")