from Components.SM import SM
from kivy.app import App
import Components.Screen1.Screen1
import Components.Screen2.Screen2
from kivy.lang import Builder

Builder.load_file("Components/Screen1/Screen1.kv")
Builder.load_file("Components/SM/SM.kv")
Builder.load_file("Components/Screen2/Screen2.kv")


class Main(App):
    def build(self):
        return SM.SM()


if __name__ == '__main__':
    Main().run()
