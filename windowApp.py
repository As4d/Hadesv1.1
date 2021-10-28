from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from infector import Infector

class MainScreen(Widget):
    
    def RunPress(self):
        print(Infector().getTotalNumberOfFiles())

    def RunRelease(self):
        pass
        

class Window(App):

    def build(self):
        return MainScreen()

if __name__ == "__main__":
    Window().run()