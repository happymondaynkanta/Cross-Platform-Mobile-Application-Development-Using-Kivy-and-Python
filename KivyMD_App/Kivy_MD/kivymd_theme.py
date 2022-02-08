


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton, MDFloatingActionButtonSpeedDial, MDIconButton, MDRoundImageButton, MDRaisedButton


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello World',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})

        btn = MDFloatingActionButton(icon="language-python", pos_hint={'center_x':0.5, 'center_y': 0.6})
        
        screen.add_widget(btn_flat)
        screen.add_widget(btn)
        return screen


DemoApp().run()