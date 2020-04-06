from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen#屏幕管理器
import os

class MainScreen(Screen,GridLayout):


   
    pass
 
class SubScreen(Screen):
    pass
 
 
class ScreenApp(App): 
    
    def build(self):
        sm = ScreenManager()
        scm = MainScreen(name="main")
        scs = SubScreen(name="sub")
        sm.add_widget(scm)
        sm.add_widget(scs)
        return sm
 
ScreenApp().run()
