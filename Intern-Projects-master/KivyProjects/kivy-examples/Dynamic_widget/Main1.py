from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

Builder.load_file("Main.kv")


class Add(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for Remove in Add:
            self.ids.box.add_widget(Remove(text_input = Remove))
    def addWidget(self):
        text = self.ids.text.text_input
        self.ids.box.add_widget(Remove(text_input = text))

class Remove(BoxLayout):
    def __init__(se ="", **kwargs):
        super().__init__(**kwargs)
         self.ids.label.text = text_input


class Main(App):
    def built(self):
        return Add(["asdas"])


if __name__ == "__main__":
    Main().run()