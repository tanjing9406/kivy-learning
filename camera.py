from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen#屏幕管理器
import os
# 引入资源目录,如res目录位于项目根目录下，写相对路径(不要写绝对路径)相当于告诉kivy　DroidSansFallback.ttf 字体位于res目录中
from kivy.resources import resource_add_path, resource_find
resource_add_path(os.path.abspath('./data/fonts'))
# 替换kivy中的默认字体，使用我们的新字体
from kivy.core.text import LabelBase
LabelBase.register('Roboto', 'weiruanyahei.ttf')

class MainScreen(Screen):
    isPassword = BooleanProperty(True)
    pass
 
class SubScreen(Screen):
    pass
 
 
class ScreenApp(App): 
    def load_kv(self, filename=None):
        with open('Screen.kv', encoding='utf-8') as f:
            Builder.load_string(f.read())
    
    def build(self):
        sm = ScreenManager()
        scm = MainScreen(name="main")
        scs = SubScreen(name="sub")
        sm.add_widget(scm)
        sm.add_widget(scs)
        return sm
 
ScreenApp().run()
