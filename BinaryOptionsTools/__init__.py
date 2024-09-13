# Made by © Vigo Walker

# Pocket Option
from BinaryOptionsTools.platforms.pocketoption.stable_api import PocketOption
import time
#--------------------- Pocket Option Wrapper ---------------------#
class pocketoption:
    def __init__(self, ssid: str, demo: bool = True) -> None:
        self.ssid = ssid
        self.api = PocketOption(ssid, demo)
        self.api.connect()
    def GetBalance(self) -> int | float:
        data = self.api.get_balance()
        return data
    def Reconnect(self, retries: int = 1) -> bool:
        for i in range(1, retries):
            self.api.connect()
            print("Connecting...")
            time.sleep(5)
        if self.api.check_connect():
            return True
        elif self.api.check_connect() == False:
            return False
        return None
    