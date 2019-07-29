from kivy.uix.screenmanager import Screen

from kivy.lang import Builder
Builder.load_file("Components/Screen1/Screen1.kv")

class Screen1(Screen):

    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)

    def add_task(self):



        pass



