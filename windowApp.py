from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from infector import Infector
from user import UserInfo
import time

class MenuScreen(Screen):
    
    def runScan(self):
        pass

class ScanScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass        

class Window(App):

    def build(self):
        return Builder.load_file('window.kv')

if __name__ == "__main__":
    Window().run()