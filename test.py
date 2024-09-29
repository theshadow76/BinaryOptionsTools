from BinaryOptionsTools import pocketoption
from BinaryOptionsTools.indicators.momentum import rsi

from BinaryOptionsTools.bot.signals import signals

ssid = (r'42["auth",{"session":"bbqncrei2vmgaqhk0a94m3b6kk","isDemo":1,"uid":69634527,"platform":2}]')
api = pocketoption(ssid, True)
print(f"GET BALANCE: {api.GetBalance()}")

sn = signals()
print(sn.sma_cross_over(api))