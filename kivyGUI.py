import kivy
from kivy.app import App
from kivy.uix.label import Label


class Window(App):
    def build(self):
        return Label(text = "Hello world ", font_size = 72)

Window().run()