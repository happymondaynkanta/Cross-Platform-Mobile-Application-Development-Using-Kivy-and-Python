



from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
#from kivy.core.window import Window

#Window.size = (300, 500)

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo'
                        left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items:[["clock", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                    MDLabel:
                        text: 'hello World'
                        halign: 'center'

                    MDBottomAppBar:
                        MDToolbar:
                            title: 'HACE'
                            left_action_items:[["coffee", lambda x: nav_drawer.toggle_nav_drawer()]]
                            mode: 'end'
                            type: 'bottom'
                            on_action_button: app.navigation_draw()

        MDNavigationDrawer:
            id: nav_drawer

"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(navigation_helper)

        return screen


DemoApp().run()