# Made by Vigo Walker

from BinaryOptionsTools import pocketoption
from ta.trend import MACD
import time

ssid = (r'42["auth",{"session":"vtftn12e6f5f5008moitsd6skl","isDemo":1,"uid":27658142,"platform":2}]')
demo = True
api = pocketoption(ssid, demo)

last_trade = None  # Track the last trade type (either "call" or "put")

while True:
    try:
        data = api.GetCandles("EURUSD_otc", 5)

        # MACD calculation
        macd_indicator = MACD(data["close"], window_slow=26, window_fast=12, window_sign=9)
        macd_line = macd_indicator.macd()
        signal_line = macd_indicator.macd_signal()
        histogram = macd_indicator.macd_diff()

        # Get the last values for the MACD, signal line, and histogram
        macd_val = macd_line.iloc[-1]
        signal_val = signal_line.iloc[-1]
        hist_val = histogram.iloc[-1]

        print(macd_val)
        print(signal_val)
        print(hist_val)

        # Conditions for bullish and bearish crossovers
        bullish_crossover = macd_val > signal_val
        bearish_crossover = macd_val < signal_val

        if bullish_crossover and last_trade != "call":
            print("Bullish crossover detected - Placing a CALL order")
            api.Call(expiration=5, amount=10)
            last_trade = "call"

        elif bearish_crossover and last_trade != "put":
            print("Bearish crossover detected - Placing a PUT order")
            api.Put(expiration=5, amount=10)
            last_trade = "put"
        else:
            print("No trade...")

        time.sleep(1)  # Delay to avoid overloading the API

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")
