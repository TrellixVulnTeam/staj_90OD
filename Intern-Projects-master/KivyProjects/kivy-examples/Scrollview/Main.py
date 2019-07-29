from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.properties import ListProperty

from kivy.utils import get_color_from_hex

class Tasks(BoxLayout):



    def __init__(self, tasks, **kwargs):
        super(Tasks,self).__init__(**kwargs)
        #self.NewDoTask=Task.DoTask

        for task in tasks:
            self.ids.box.add_widget(Task (text= task))

    def NewDoTask(self,instance):
        print(str(instance)+" ilk")
        with self.ids.box.children[instance].canvas.before:
            Color(rgba=get_color_from_hex("#42a4f5"))
            Rectangle(pos=self.pos, size=self.size)

    def addWidget(self):
        input = self.ids.input.text
        newListItem=Task(text = input,id=str((len(self.ids.box.children))))
        self.ids.box.add_widget(newListItem)
        """
        with self.ids.box.children[0].canvas.before:
            Color(rgba=[1, 3, 2, 0.005])
            Rectangle(pos=self.pos, size=self.size)

        """

        self.NewDoTask((len(self.ids.box.children)-1))








class Task(BoxLayout):


    def __init__(self, text= "", **kwargs):
        super(Task,self).__init__(**kwargs)
        self.ids.label.text = text

    def DoTask(self):
        print(str(self.id) + " after do it")
        with self.canvas.before:
            Color(rgba=get_color_from_hex("#72f542"))
            Rectangle(pos=self.pos, size=self.size)


class Main(App):

    def build(self):
        return Tasks([])


Main().run()