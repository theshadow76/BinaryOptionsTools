from BinaryOptionsTools.platforms.pocketoption.stable_api import PocketOption

ssid = (r'42["auth",{"session":"n6ghkt8nk931jj6ffljoj8knj3","isDemo":1,"uid":85249466,"platform":2}]')
api = PocketOption(ssid, True)
api.connect()

df = api.get_candles("AUDNZD_otc", 1, count=9000, count_request=100)
df.to_csv("history-AUDNZD_otc.csv")