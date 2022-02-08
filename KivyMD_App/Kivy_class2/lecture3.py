from kivy.app import App 
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window 
from kivy.uix.button import Button 

Window.clearcolor = (1, 1, 1, 1)
#Window.size = (360, 600)

class BoxApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical', spacing=10, padding= 40)
        img = Image(source='love.png')
        button = Button(text="Login", size_hint=(None, None), width=100, height=50, pos_hint={'center_x':0.5})
        layout.add_widget(img)
        layout.add_widget(button)
              
        return layout

BoxApp().run()