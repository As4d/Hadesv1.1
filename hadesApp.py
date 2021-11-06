from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from infector import Infector
from user import UserInfo
import time

class MenuScreen(Screen):
    pass

class RunSelectionScreen(Screen):        
    pass

class SearchVulnerableFileNamesScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.infector = Infector()
        self.increment = 100/(self.infector.getTotalNumberOfFiles())
        self.count = 0

    def runSearchVulnerableFileNames(self):
        self.Clock = Clock.schedule_interval(self.updateProgressbar, 1/99999999999999999999999999999999)
        self.ids.progressLabel.text = str(self.count)

    def cancelProgressbar(self, *args):
        self.ids.progressLabel.text =  "{} Files".format(str(self.infector.searchVulnerableFileNames()))
        self.Clock.cancel()
    
    def updateProgressbar(self, *args):
        self.ids.progressBar.value += self.increment
        self.count += 1
        self.ids.progressLabel.text = "{}/{}".format(str(self.count), str(self.infector.getTotalNumberOfFiles()))
        if self.ids.progressBar.value == 100:
            self.cancelProgressbar()

class WindowManager(ScreenManager):
    pass        

class Hades(App):

    def build(self):
        return Builder.load_file('hades.kv')

if __name__ == "__main__":
    Hades().run()