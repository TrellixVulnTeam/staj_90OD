from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from Components.SM.SM import SM
from kivy.lang.builder import Builder

Builder.load_file("Components/SM/SM.kv")
Builder.load_file("Components/Login/Login.kv")




class Main(App):
    def build(self):
        return SM()

if __name__=="__main__":
    sa = Main()
    sa.run()