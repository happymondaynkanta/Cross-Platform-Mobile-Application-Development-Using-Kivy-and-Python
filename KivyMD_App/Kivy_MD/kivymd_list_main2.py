

from kivymd.app import MDApp
from kivy.lang import Builder

# Using the multi-string builder method

list_helper = """
Screen:
    ScrollView:
        MDList:
            OneLineListItem:
                text: 'Item 1'
            
            OneLineListItem:
                text: 'Item 2'

"""

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper)

        return screen
        



DemoApp().run()