from BinaryOptionsTools import pocketoption
from BinaryOptionsTools.bot.signals import signals
ssid = (r'42["auth",{"session":"vtftn12e6f5f5008moitsd6skl","isDemo":1,"uid":27658142,"platform":2}]')
api = pocketoption(ssid, True)

print(signals().sma_cross_over(api=api))