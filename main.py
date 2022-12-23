from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
Builder.load_file('app.kv')

class MainApp(Widget):
    pass





class NICEWHITE(App):
    def build(self):
        return MainApp()


if __name__ == '__main__':
    NICEWHITE().run()