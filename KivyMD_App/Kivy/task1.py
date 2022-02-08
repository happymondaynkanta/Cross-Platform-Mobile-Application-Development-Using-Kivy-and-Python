# this script is for the KIVY file taska.kv
import kivy
from kivy.app import app
from kivy.uix.floatlayout import FloatLayout


class Task1App(App):
    def build(self):
        return FloatLayout

if __name__ == "__main__":
    Task1App().run()