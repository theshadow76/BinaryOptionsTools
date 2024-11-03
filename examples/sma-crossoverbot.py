from BinaryOptionsTools import pocketoption
import ta
import time
# import pandas as pd

ssid = (r'42["auth",{"session":"vtftn12e6f5f5008moitsd6skl","isDemo":1,"uid":27658142,"platform":2}]')
demo = True
api = pocketoption(ssid, demo)

def GetCandles(symbol, timeframe, limit=100):
    # Fetch candle data for a given symbol and timeframe
    candles = api.GetCandles(symbol, timeframe, limit)
    #df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')  # Assuming 'timestamp' is in seconds
    return candles

def DetectSMAsimple(symbol, timeframe, period=14):
    # Fetch the candles for the given symbol and timeframe
    df = api.GetCandles(symbol, timeframe)
    print(f"DF: {df}")
    # Calculate the simple moving average using the 'close' price
    df['SMA'] = ta.trend.sma_indicator(df['close'], window=period)
    
    # Check if last SMA is bullish or bearish
    if df['SMA'].iloc[-1] > df['close'].iloc[-2]:  # Bullish
        return "Bullish"
    elif df['SMA'].iloc[-1] < df['close'].iloc[-2]:  # Bearish
        return "Bearish"
    else:
        return "Neutral"

def DetectSMAStream(symbol, timeframe, period=14, interval=60):
    # Continuously fetch and detect SMA trend
    while True:
        try:
            result = DetectSMAsimple(symbol, timeframe, period)
            print(f"SMA Trend: {result}")
            # Wait for the next update (based on interval)
            time.sleep(interval)
        except KeyboardInterrupt:
            break

# Detect SMA once
print(DetectSMAsimple("EURUSD_otc", 1))

# Stream SMA trend detection every minute
DetectSMAStream("EURUSD_otc", 1, interval=60)

#NOTE: DetectSMAsimple is just the basic calculation and DetectSMAStream is like a stream of data, constantly detecting sma and if last sma was bullish or bearish