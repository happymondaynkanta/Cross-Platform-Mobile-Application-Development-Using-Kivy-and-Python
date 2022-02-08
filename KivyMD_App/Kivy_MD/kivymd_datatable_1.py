
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 check=True,
                                 rows_num=10,
                                 column_data=[
                                     ("No.", dp(18)),
                                     ("Food", dp(20)),
                                     ("Calories", dp(20))
                                 ],
                                 row_data=[
                                     ("1", "Burger", "380"),
                                     ("2", "Oats", "150"),
                                     ("3", "Beans", "150"),
                                     ("4", "Rice", "150"),
                                     ("5", "Plantain", "150"),
                                     ("5", "Fufu", "150"),
                                     ("6", "Eba", "150"),
                                     ("7", "Semo", "150"),
                                     ("8", "Wheat", "150"),
                                     ("9", "Yam", "150"),
                                     ("10", "Cassava", "150")
                                 ]
                                 )
        data_table.bind(on_check_press=self.check_press)
        data_table.bind(on_row_press=self.row_press)
        screen.add_widget(data_table)
        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

DemoApp().run()