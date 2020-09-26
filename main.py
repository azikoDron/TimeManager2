import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class TopNavBar(FloatLayout):
    pass


class Controller(FloatLayout):
    pass


class ControllerApp(App):                                                           

    def build(self):
        return Controller()


if __name__ == '__main__':
    ControllerApp().run()