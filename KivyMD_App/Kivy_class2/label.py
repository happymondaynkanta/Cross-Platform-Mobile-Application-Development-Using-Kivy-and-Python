from kivy.app import App 
from kivy.uix.label import Label 
from kivy.core.window import Window 
from kivy.uix.button import Button 



Window.clearcolor = (1, 1, 1, 1)

class LabelApp(App):
    def build(self):
        #label = Label(text= 'This is Smart Hace', font_size ="20sp", bold=True, color=(1, 0, 0, 1))
        button= Button(text='Submit', size_hint=(0.2, 0.2), font_size='20sp', 
                        on_press=self.printpress, on_release=self.printrelease,
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        return button 

    def printpress(self, obj):
        print('Button has been pressed')

    def printrelease(self, obj):
        print('Button has been released')

LabelApp().run()