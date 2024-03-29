from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout 


class TextApp(App):
    def build(self):
        layout = GridLayout (cols=2, row_force_default=True, row_default_height=40,
                            spacing=10, padding=20)
        self.weight = TextInput(text= 'Enter weight')
        self.height = TextInput(text= 'Enter height')
        submit = Button(text= 'Submit', on_press=self.submit)

        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)

        return layout
    def submit(self, obj):
        print('weihjt:' + self.weight.text)
        print('heihjt:' + self.height.text)



TextApp().run() 