from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen





class Login (BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        uname = user.text
        passw = pwd.text
        info = self.ids.info
        if uname == "" or passw == "":
            info.text= "[color=#FF0000]username or password required[/color]" #red
        else:
            if uname == "admin" and passw == "admin":
                info.text = "[color=#00FF00] Logged In Successfully[/color]" #green



            else:
                info.text = "[color=#FF0000]Invalid username or password[/color]"  # red




