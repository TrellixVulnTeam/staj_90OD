from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("test.kv")


class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefas(text=tarefa))

    def addWidget(self):
        texto = self.ids.text.text_input
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""


class Tarefa(BoxLayout):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text


class Test(App):
    def build(self):
        return Tarefas(["asdas"])


Test().run()
