from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open('users.json', 'r') as f:
            user_data = json.load(f)
        if username in user_data and password == user_data[username]["password"]:
            self.manager.current = "log_in_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong Username or Password!"


class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open('users.json', 'r') as f:
            user_data = json.load(f)

        user_data.update({
            username: {
                "username": username,
                "password": password,
                "created_at": str(datetime.now()).split('.')[0]
            }
        })

        with open('users.json', 'w') as f:
            json.dump(user_data, f, indent=2)

        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LogInScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings_file_path = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings_file_path]

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", 'r', encoding='utf-8') as f:
                quotes = f.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
