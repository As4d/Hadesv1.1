from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from infector import Infector
from user import UserInfo
import time

class MenuScreen(Screen):
    pass

class RunSelectionScreen(Screen):        
    pass

class SearchVulnerableFileNamesScreen(Screen):

    def runSearchVulnerableFileNames(self):
        print(Infector().searchVulnerableFileNames())

class WindowManager(ScreenManager):
    pass        

class Hades(App):

    def build(self):
        return Builder.load_file('hades.kv')

if __name__ == "__main__":
    Hades().run()