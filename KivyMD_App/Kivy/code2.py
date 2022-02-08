import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.click = Button(text = "Find More About Happyson", font_size=40)
        self.add_widget(self.click)

        self.inside = GridLayout()
        self.inside.cols = 2


        self.inside.add_widget(Label(text = "First Name:"))
        self.firstname = TextInput(multiline = False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text = "Last Name:"))
        self.lastname = TextInput(multiline = False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text = "Email:"))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text = "School:"))
        self.schoolname = TextInput(multiline = True)
        self.inside.add_widget(self.schoolname)

        self.add_widget(self.inside)

        self.back = Button(text="Return", font_size=40)
        self.add_widget(self.back)

        self.side = GridLayout()
        self.side.cols = 3

        self.sign_in = Button(text = "Sign In", font_size=40)
        self.side.add_widget(self.sign_in)

    
        self.sign_up = Button(text = "Sign Up", font_size=40)
        self.side.add_widget(self.sign_up)

        self.reset = Button(text = "Reset", font_size=40)
        self.side.add_widget(self.reset)

        self.add_widget(self.side)



        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.firstname.text
        last = self.lastname.text
        email = self.email.text

        print("Name:", name, "Last name:", last, "Email:", email)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()





