import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GridLayout(GridLayout):
    
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text = "Whos better"))
        self.add_widget(TextInput(multiline= False))

        self.add_widget(Label(text = "W/L: "))
        self.add_widget(TextInput(multiline= False))

class Window(App):

    def build(self):
        return GridLayout()

Window().run()