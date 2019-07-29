from kivy.uix.screenmanager import Screen
from components.Screen2.Screen2 import Screen2
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from threading import Timer
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

import random
from kivy.uix.button import Button


import json

class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)
        self.ScrollBoxLayout = BoxLayout(orientation="vertical", id="box", size_hint=(1, .9), pos_hint={'top': 1})
        self.newScroolView = ScrollView(id="boxScroll", do_scroll_x=False, do_scroll_y=True, size=self.size,
                                        bar_width=5,size_hint_y=None)

        self.ScrollBoxLayout.add_widget(self.newScroolView)
        self.add_widget(self.ScrollBoxLayout)

    def on_enter(self, *args):
        self.file = open('C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json')
        self.file_read = self.file.read()
        self.file_data = json.loads(self.file_read)
        #newBoxLayout = BoxLayout(orientation="vertical", id="box", size_hint_y=None, pos_hint={"top":1},spacing=3)
        #newBoxLayout.bind(minimum_height=newBoxLayout.setter("height"))
        self.ids.Scroll.clear_widgets()

        for object in self.file_data:
            if object["Name"] != "":


                myBoxLayout = BoxLayout(orientation="horizontal",  size_hint=(1,None),height=50,id=object["Name"])


                remButton=Button(height=50,size_hint=(.1,None),on_press=self.remove_task,text="X")
                newLabel = ButtonLabels(

                    text=(object["Name"] + " -->" + "You have until " + str(object["Date"]) + " am"),
                    size_hint=(1, None), height=50, strikethrough=object["State"], id=object["Name"])

                myBoxLayout.add_widget(newLabel)
                myBoxLayout.add_widget(remButton)

                self.ids.Scroll.add_widget(myBoxLayout)

        s = Timer(0.1, self.SetUpSiparisSatirColor)
        s.start()

    def random_color(self):
        r = lambda: random.randint(0, 255)
        return ('#%02X%02X%02X' % (r(), r(), r()))

    def SetUpSiparisSatirColor(self):
        with self.canvas.before:
            Color(rgba=get_color_from_hex("#2a3f54"))
            Rectangle(pos=self.ScrollBoxLayout.pos,
                      size=self.ScrollBoxLayout.size)

    def remove_task(self,instance):
        list = []
        file = open('C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json')
        file_read = file.read()
        file_data = json.loads(file_read)
        for z in file_data:
            list.append(z)
        for i in list:

            for object in list:
                if instance.parent.id==object["Name"]:
                    list.remove(object)
                    self.ids.Scroll.remove_widget(instance.parent)
        with open("C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json", "w") as jsonFile:
            json.dump(list, jsonFile)





class Task(BoxLayout):
    def __init__(self, text="", **kwargs):
        super(Task, self).__init__(**kwargs)
        self.ids.label.text = text


class ButtonLabels(ButtonBehavior,Label):
    def __init__(self,**kwargs):
        super(ButtonLabels,self).__init__(**kwargs)

    def on_press(self):


        file = open('C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json')
        file_read = file.read()
        file_data = json.loads(file_read)

        for object in file_data:
            if self.id == object["Name"]:
                if (self.strikethrough==True):
                    self.strikethrough=False
                    object["State"]=False

                elif (self.strikethrough == False):
                    self.strikethrough=True
                    object["State"]=True
        with open("C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json", "w") as jsonFile:
            json.dump(file_data, jsonFile)
