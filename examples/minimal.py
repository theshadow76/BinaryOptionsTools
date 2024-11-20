from BinaryOptionsTools import pocketoption
import sys
print(sys.path)

ssid = input("Enter your ssid: ")
api = pocketoption(ssid, True)

# Get current balance
print(f"GET BALANCE: {api.GetBalance()}")
