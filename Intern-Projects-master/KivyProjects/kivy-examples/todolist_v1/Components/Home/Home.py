from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
import json
import time,datetime
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label


file = open("data.json")
file_read = file.read()
file_data = json.loads(file_read)
data = []
for x in file_data:
    data.append(x)
file.close()




class Home(Screen):


    def __init__(self,**kwargs):
        super(Home,self).__init__(**kwargs)
        EachTask.Remove_widget = self.remove_widget

        for tasks in data:
            #print(tasks["control"])
            if tasks["control"] == True:
                newListItem = EachTask( rgba= [0,.7,.3,1],
                                       text= tasks["task"]+ "    time:    " + tasks["time"],
                                       id=str((len(self.ids.add_field.children))))

                self.ids.add_field.add_widget(newListItem)
            else:

                    newListItem = EachTask(text=tasks["task"] + "    time:    " + tasks["time"],
                                           id=str((len(self.ids.add_field.children))))

                    self.ids.add_field.add_widget(newListItem)


        Clock.schedule_interval(self.ClockFunction,10)
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
        #print(instant)
        content = Label(text = "Delete Task or Sign as Done")



        for current in data:
            if current["time"] == instant:
                if current["control"] == False:
                    print("smth")
                    the_popup = Popup(title="Time out", content= content, size_hint=(None, None),
                                      size=(500, 250)  )

                    the_popup.open()

                    break




        EachTask.RemoveWidget = self.removeWidget

    def removeWidget(self, instance):
        self.ids.add_field.remove_widget(instance.parent.parent)

    def addWidget(self):

        task_input = self.ids.task_input.text
        time_input = self.ids.time_input.text

        #print(type(time_input))
        #print(type(task_input))


        newListItem = EachTask(text= task_input + "    time:    " + time_input  , id=str((len(self.ids.add_field.children))))
        #print(newListItem.id)
        self.ids.add_field.add_widget(newListItem)

        data.append({"task": task_input,
                     "time": time_input,
                     "control" : False,
                     "id" : str((len(self.ids.add_field.children))-1)
                          })
        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)


    def remove_widget(self, instance):
        #print(self.ids.add_field.parent)
        label_text = instance.parent.parent.ids.label.text
        self.ids.add_field.remove_widget(instance.parent.parent)


        for current in data:
            task = current.get("task")
            time = current.get("time")
            if (label_text == task+ "    time:    " + time  ):
                #print(current.get("task"))

                data.remove(current)
                #print(data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, ensure_ascii=False)





class EachTask(BoxLayout):

    rgba = ListProperty([1, .5, .5, 1])
    def __init__(self, text= "", **kwargs):
        super(EachTask,self).__init__(**kwargs)
        input = self.ids.input.text
        newListItem = EachTask(text=input, id=str((len(self.ids.add_field.children))))
        self.ids.add_field.add_widget(newListItem)



    def __init__(self, text="", **kwargs):
        super(EachTask, self).__init__(**kwargs)
        self.ids.label.text = text

    """"
    def find_id(lst,key,val):
        for i,dic in enumerate(lst):
            if dic[key] == val:
                return i
        return -1
    """
    def Do_Task(self,instance):
        id = str(instance.parent.parent.id)

        if (self.rgba == [1, .5, .5, 1]):
            self.rgba = [0,.7,.3,1]
            for current in data:
                if current["id"] == id:
                    current["control"] = True
        else:
            self.rgba = [1, .5, .5, 1]
            for current in data:
                if current["id"] == id:
                    current["control"] = False

        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)


    def Remove_widget(self, instance):
       pass
















