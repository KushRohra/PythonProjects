from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"


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



class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()