from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from infector import Infector
from filehelper import FileHelper
from user import UserInfo
from databasemanager import DatabaseManager
import time
import json


class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class RunSelectionScreen(Screen):
    pass


class SimulateAttackScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.count = 0
        self.fileHelper = FileHelper()
        self.infector = Infector(self.fileHelper)
        self.user = UserInfo()

    def runSimulateAttack(self):

        fileExtensions = ["txt", "zip", "exe"]
        for extension in fileExtensions:
            self.fileHelper.findAllFiles(extension)
        self.increment = 100 / (self.fileHelper.getTotalNumberOfFiles())
        self.Clock = Clock.schedule_interval(self.updateProgressbar, 0.0000001)
        self.ids.progressLabel.text = str(self.count)

    def cancelProgressbar(self, *args):
        self.ids.progressLabel.text = "Finished"
        self.ids.progressBar.value = 0
        self.count = 0
        self.Clock.cancel()
        self.user.updateCounts()
        self.user.updateScanInfo()
        DatabaseManager().updateUser()

    def updateProgressbar(self, *args):
        self.ids.progressBar.value += self.increment
        self.count += 1
        self.ids.progressLabel.text = "{}/{}".format(
            str(self.count), str(self.fileHelper.getTotalNumberOfFiles())
        )
        if self.ids.progressBar.value == 100:
            self.cancelProgressbar()


class SearchVulnerableFileNamesScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.count = 0
        self.fileHelper = FileHelper()

    def runSearchVulnerableFileNames(self):
        fileExtensions = ["txt", "zip", "exe"]
        for extension in fileExtensions:
            self.fileHelper.findAllFiles(extension)
        self.increment = 100 / (self.fileHelper.getTotalNumberOfFiles())
        self.Clock = Clock.schedule_interval(self.updateProgressbar, 0.0000001)
        self.ids.progressLabel.text = str(self.count)

    def cancelProgressbar(self, *args):
        self.ids.progressLabel.text = "{} Files".format(
            str(self.infector.searchVulnerableFileNames())
        )
        self.ids.progressBar.value = 0
        self.count = 0
        self.Clock.cancel()

    def updateProgressbar(self, *args):
        self.ids.progressBar.value += self.increment
        self.count += 1
        self.ids.progressLabel.text = "{}/{}".format(
            str(self.count), str(self.fileHelper.getTotalNumberOfFiles())
        )
        if self.ids.progressBar.value == 100:
            self.cancelProgressbar()


class WindowManager(ScreenManager):
    pass


class Hades(App):
    def build(self):
        return Builder.load_file("hades.kv")


if __name__ == "__main__":
    Hades().run()
