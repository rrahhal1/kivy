from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
class DynamicApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        return layout
if __name__ == '__main__':
    DynamicApp().run()
