from kivy.app import App
from Components.SM.SM import SM
from kivy.lang.builder import Builder
from Components.Home.Home import Home,EachTask

Builder.load_file("Components/SM/SM.kv")
Builder.load_file("Components/Home/Home.kv")



class Main(App):
    def build(self):
        return SM()


if  __name__ == "__main__":
    Main().run()


