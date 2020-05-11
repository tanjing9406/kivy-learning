from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen#屏幕管理器
import os
import csv
# 引入资源目录,如res目录位于项目根目录下，写相对路径(不要写绝对路径)相当于告诉kivy　DroidSansFallback.ttf 字体位于res目录中
from kivy.resources import resource_add_path, resource_find
resource_add_path(os.path.abspath('./data/fonts'))
# 替换kivy中的默认字体，使用我们的新字体
from kivy.core.text import LabelBase
LabelBase.register('Roboto', 'weiruanyahei.ttf')

class MainScreen(Screen,Widget):

    def user(self):
        username = self.ids['user_name']
        password = self.ids['pass_word']

        with open('username.csv','r', newline = '', encoding = 'utf-8')  as f:
           row1 = csv.reader(f)
           for row in row1:
               print(row[0],row[1])
               if row[0]==username.text:
                   if row[1]==password.text:
                       self.manager.current="sub"
                       
               else:
                   print('账户名或密码错误')
 
class SubScreen(Screen,Widget):
    pass
 
class NeckScreen(Screen):
    pass
class ScreenApp(App): 
    def load_kv(self, filename=None):
        with open('Screen.kv', encoding='utf-8') as f:
            Builder.load_string(f.read())
    
    def build(self):
        
        sm = ScreenManager()
        scm = MainScreen(name="main")
        scs = SubScreen(name="sub")
        # scn = NeckScreen(name="neck")
        sm.add_widget(scm)
        sm.add_widget(scs)
        # sm.add_widget(scn)
        return sm
ScreenApp().run()
