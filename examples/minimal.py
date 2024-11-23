import logging.config
from BinaryOptionsTools import pocketoption

import logging
logging.basicConfig(level=logging.INFO)

ssid = input("Enter your ssid: ")
api = pocketoption(ssid, True)

# Get current balance
print(f"GET BALANCE: {api.GetBalance()}")