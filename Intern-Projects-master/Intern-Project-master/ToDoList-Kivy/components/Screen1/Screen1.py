import random
from threading import Timer

from kivy.uix.popup import Popup

from components.Screen2.Screen2 import Screen2
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.label import Label
import datetime
from kivy.core.text import Label as CoreLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock as KivyClock, Clock
import json

from kivy.utils import rgba

class Screen1(Screen):

    def __init__(self, **kwargs):

        super(Screen1, self).__init__(**kwargs)
        self.welcome = ""
        self.WelcomeBoxLayout=BoxLayout(orientation="vertical", id="welcome", size_hint=(1, .1), pos_hint={'top': 1})
        self.WelcomeBoxLayout.add_widget(Label(text="WELCOME TO  MY APP"))
        self.add_widget(self.WelcomeBoxLayout)

        self.ScrollBoxLayout=BoxLayout(orientation="vertical", id="box", size_hint=(1, .8), pos_hint={'top': .9})
        self.newScroolView = ScrollView(id="boxScroll", do_scroll_x=False, do_scroll_y=True, size=self.size, bar_width=5)

        self.ScrollBoxLayout.add_widget(self.newScroolView)
        self.add_widget(self.ScrollBoxLayout)

        Clock.schedule_interval(self.ClockFunction, 3)

    def ClockFunction(self, *args):
        an = datetime.datetime.now()
        hour = an.hour
        min = an.minute
        if hour < 10:
            saat = "0" + str(hour)
        else:
            saat = str(hour)
        if min < 10:
            dak = "0" + str(min)
        else:
            dak = str(min)
        instant = saat + ":" + dak

        self.file = open('data.json')
        self.file_read = self.file.read()
        self.file_data = json.loads(self.file_read)

        for object in self.file_data:
            if object["Date"] == instant:
                if object["State"] == False:
                    object["State"] = True
                    the_popup = Popup(title="Time out",content=Label(text="For event "+object["Name"]+",Time is up!"),size_hint=(None,None),size=(300,150))
                    the_popup.open()
                    with open("data.json", "w") as jsonFile:
                        json.dump(self.file_data, jsonFile)
                    break

        self.on_enter()


    def on_enter(self, *args):
        file = open('C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json')
        file_read = file.read()
        file_data = json.loads(file_read)
        self.newScroolView.clear_widgets()
        newBoxLayout = BoxLayout(orientation="vertical", id="box", size_hint_y=None, spacing=3)
        newBoxLayout.bind(minimum_height=newBoxLayout.setter("height"))


        for object in file_data:
            if object["Name"] != "":

                    newLabel = ButtonLabel(

                        text=(object["Name"] + " -->" + "You have until " + str(object["Date"]) + " pm"),
                        size_hint=(1, None), height=50, strikethrough=object["State"], id=object["Name"])

                    newBoxLayout.add_widget(newLabel)



            else:
                newLabel = ButtonLabel(
                        text=(object["Name"] + " -->" + "You have until " + str(object["Date"]) + " am"),
                        size_hint=(1, None), height=50, strikethrough=object["State"], id=object["Name"])

                newBoxLayout.add_widget(newLabel)




        self.newScroolView.add_widget(newBoxLayout)

        s = Timer(0.1, self.SetUpSiparisSatirColor)
        s.start()



    def random_color(self):
        r = lambda: random.randint(0, 255)
        return ('#%02X%02X%02X' % (r(), r(), r()))

    def SetUpSiparisSatirColor(self):


        with self.WelcomeBoxLayout.canvas.before:
            Color(rgba=get_color_from_hex("#4287f5"))
            Rectangle(pos=self.WelcomeBoxLayout.pos,
                      size=self.WelcomeBoxLayout.size)
        with self.canvas.before:
            Color(rgba=get_color_from_hex("#2a3f54"))
            Rectangle(pos=self.ScrollBoxLayout.pos,
                      size=self.ScrollBoxLayout.size)


class ButtonLabel(ButtonBehavior,Label):
    def __init__(self,**kwargs):
        super(ButtonLabel,self).__init__(**kwargs)

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














