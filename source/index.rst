BinaryOptionsTools documentation
================================

Welcome to the documentation of BinaryOptionsTools!

QuickStart
----------

Example to get balance::

   from BinaryOptionsTools import pocketoption

   ssid = (r'YOUR_SSID')
   api = pocketoption(ssid, True)
   print(f"GET BALANCE: {api.GetBalance()}")