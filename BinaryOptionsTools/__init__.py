# Made by © Vigo Walker

# Pocket Option
from BinaryOptionsTools.platforms.pocketoption.stable_api import PocketOption

#--------------------- Pocket Option Wrapper ---------------------#
class pocketoption:
    def __init__(self, ssid: str, demo: bool = True) -> None:
        self.ssid = ssid
        self.api = PocketOption(ssid, demo)
        self.api.connect()
    def GetBalance(self):
        data = self.api.get_balance()
        return data