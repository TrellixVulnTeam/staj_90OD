from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from Components.SM import SM




class Home(Screen):
    def __init__(self,**kwargs):
        super(Home,self).__init__(**kwargs)
        EachTask.RemoveWidget = self.removeWidget


    def removeWidget(self, instance):
        self.ids.add_field.remove_widget(instance.parent.parent)

    def addWidget(self):
        input = self.ids.input.text
        newListItem = EachTask(text=input, id=str((len(self.ids.add_field.children))))
        self.ids.add_field.add_widget(newListItem)

class EachTask(BoxLayout):

    def __init__(self, text="", **kwargs):
        super(EachTask, self).__init__(**kwargs)
        self.ids.label.text = text


    def RemoveWidget(self,instance):
        pass


















