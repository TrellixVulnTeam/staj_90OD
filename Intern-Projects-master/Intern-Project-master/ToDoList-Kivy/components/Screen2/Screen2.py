from kivy.uix.screenmanager import ScreenManager,Screen
import json
import datetime
from kivy.clock import Clock
from kivy.lang import Builder

from kivy.uix.button import Button

from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput




class Screen2(Screen):
    Screen1=ObjectProperty()
    def __init__(self,**kwargs):
        super(Screen2,self).__init__(**kwargs)



    def on_enter(self, *args):
        self.Screen1 = self.manager.get_screen('Screen1')

    def add_event(self):
        temp = []
        file = open('C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json')
        file_read = file.read()
        file_data = json.loads(file_read)
        for x in file_data:
            temp.append(x)
        name = str(self.ids.input1.text)
        date=self.ids.input2.text

        try:

            date=int(date)

            an = datetime.datetime.now()

            local_date = int(date) + an.hour

            if int(local_date) > 24:
                self.local = int(local_date) % 24
            if self.local<10:
                self.local="0"+str(self.local)
            print(self.local)
            if an.minute<10:
                dakika="0" + str(an.minute)
            else:
                dakika=str(an.minute)
            local_time = str(self.local) +":"+ dakika

            x = {'Name': name,

                 "Date": local_time,
                 "State" : False
                 }

            temp.append(x)
            with open('C:\\Users\\Dora\\PycharmProjects\\ToDoList-Kivy\\data.json', 'w') as file_data:
                json.dump(temp, file_data)
            file.close()
        except ValueError:
            the_popup = popupcls()
            the_popup.open()



class popupcls(Popup):
    pass












