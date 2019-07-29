from kivy.app import App
from components.SM import SM
import threading
import json
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from components.Screen1.Screen1 import Screen1


from components.Screen2.Screen2 import Screen2
from components.Screen3.Screen3 import Screen3
from kivy.uix.popup import Popup
from time import strftime
from kivy.clock import Clock
import datetime

from kivy.uix.widget import Widget
from kivy.uix.label import Label
import time

from kivy.lang import Builder

Builder.load_file("C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\components\\Screen1\\Screen1.kv")
Builder.load_file("C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\components\\Screen2\\Screen2.kv")
Builder.load_file("C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\components\\Screen3\\Screen3.kv")
Builder.load_file("C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\components\\SM\\Sm.kv")




class Main(App):

    title="MyToDoList"

    def build(self):
        return SM.SM()



if __name__ == '__main__':
    Main().run()