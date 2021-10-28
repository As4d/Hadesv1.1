from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from infector import Infector
import time

class MainScreen(Widget):
    
    def RunPress(self):
        self.ids.run_button.text = 'Rerun'
        self.ids.num_files_label.text = str(Infector().getTotalNumberOfFiles()) + " Files Scanned"
        

class Window(App):

    def build(self):
        return MainScreen()

if __name__ == "__main__":
    Window().run()