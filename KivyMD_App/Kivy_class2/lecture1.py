from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = Image(source="love.png")
        return img 

MainApp().run()