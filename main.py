import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class SideBar(GridLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('inside side')
        else:
            print('outside side')
            self.size_hint = (0, .93)


class TopNavBar(FloatLayout):
    def menu_action(self):
        self.add_widget(SideBar())

    def hide_menu_action(self):             # FIX ME ! NOT WORKING
        self.remove_widget(SideBar())


class TaskMenu(GridLayout):
    # layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    # # Make sure the height is such that there is something to scroll.
    # layout.bind(minimum_height=layout.setter('height'))
    # for i in range(15):
    #     btn = Button(text=str(i), size_hint_y=None, height=40)
    #     layout.add_widget(btn)
    # root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    # root.add_widget(layout)
    #
    # runTouchApp(root)
    pass


class Controller(FloatLayout):
    pass


class ControllerApp(App):
    def build(self):
        return Controller()


if __name__ == '__main__':
    ControllerApp().run()
