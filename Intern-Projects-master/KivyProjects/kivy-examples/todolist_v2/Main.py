from kivy.app import App

from kivy.lang.builder import Builder
from Components.Home.Home import Home
from Components.SM.SM import SM
Builder.load_file("Components/SM/SM.kv")
Builder.load_file("Components/Home/Home.kv")



class Main(App):
    def build(self):

        return Home()


if  __name__ == "__main__":
    Main().run()


