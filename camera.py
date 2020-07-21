from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty,ListProperty
)
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen#屏幕管理器
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
import os
import csv
import sqlite3
from kivy.config import Config
Config.set('graphics', 'fullscreen', 1)

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
 
class SubScreen(Screen):
    pass

class Material:
    def __init__(self,name,amount,cylinder):
        self.name = name
        self.amount = amount
        self.cylinder = cylinder
        
class ChunChu:
    score = NumericProperty(0)
    score1 = NumericProperty(0)
    def __init__(self):
        
        self.materials = []
        with open('materials.csv', newline = '', encoding = 'utf-8')  as f:
           reader = csv.reader(f)
           for row in reader:
              
              material = Material(row[0],row[1],row[2])
              self.materials.append(material)
    
    def ling(self,mingcheng):
        
        with open('materials.csv','r', newline = '', encoding = 'utf-8')  as f:
           row1 = csv.reader(f)
           for row in row1:
               if mingcheng==row[0]:
                   return row
    def check_book(self,name):
        
        for book in self.materials:
            if book.name == name:
                return book
    
    def delete(self,name1,BUS):
        print(BUS)
        print('------------------------------')
        print(name1)
        ls3 = []
        for book in self.materials:
            book2 = [book.name,book.amount,book.cylinder]
            if book.name != name1:
                ls3.append(book2)
        
        
        a = BUS
        with open('materials.csv','w', newline = '', encoding = 'utf-8')  as f:
           writer = csv.writer(f)
           writer.writerow(a)
        ls4 = ls3
        for ls5 in ls4:
           with open('materials.csv','a',newline = '', encoding = 'utf-8')  as f:
              writer = csv.writer(f)
              writer.writerow(ls5)
        # for ls5 in ls4:  
        #     with open('materials.csv','w', newline = '', encoding = 'utf-8')  as f:
        #         writer = csv.writer(f)
        #         writer.writerow(ls5)
        print('-----------------------')
        print(ls4)        
 
class NeckScreen(Screen,ChunChu):
    
    score = NumericProperty(0)
    score1 = NumericProperty(0)
    score2 = NumericProperty(0)
    score3 = NumericProperty(0)

   
              
    def lin(self):
        mingcheng = self.ids['ming-cheng'].text
        a = ChunChu()
        
        res = a.ling(mingcheng)
        print(res)
        self.score = float(res[1])
        self.score1 = float(res[2])
    
    
    
    def lend_materials(self):
        name1 = self.ids['ming-cheng'].text
        lingliao = self.ids['ling-liao'].text
        manager = ChunChu()
        
        res = manager.check_book(name1)
        print(name1)
        print('领取的材料是：', res)
        requisition =float(res.amount)/float(res.cylinder)
        univolume1 =float(requisition)*int(lingliao)
        univolume2 =int(univolume1)
        print('领取材料重量：', univolume2)
        self.score3 = int(univolume2)
        res.amount=float(res.amount)-univolume2

        cylinder=float(res.cylinder)-float(lingliao)
        res.cylinder=round(cylinder,0)
        BUS = [res.name,res.amount,res.cylinder]
        print(BUS)
        print('-----------------------------')
        manager = ChunChu()
        manager.delete(name1,BUS)
        
        
class butScreen(Screen):
    scor = NumericProperty(0)
    scor1 = NumericProperty(0)
    
    def ling(self):
        mingcheng = self.ids['ming-cheng'].text
        print(mingcheng)
        a = ChunChu()
        
        res = a.ling(mingcheng)
        self.scor = float(res[1])
        self.scor1 = float(res[2])
    
    def lend_material(self):
        name = self.ids['ming-cheng'].text
        name1 = self.ids['shu-liang'].text
        lingliao = self.ids['juan-shu'].text
        
        manager = ChunChu()
        
        res = manager.check_book(name)
        print('领取的材料是：', res)
        res.amount =float(res.amount)+float(name1)
        
        res.cylinder=float(res.cylinder)+float(lingliao)

        BUS = [res.name,res.amount,res.cylinder]
        print(BUS)
        print('-----------------------------')
        manager = ChunChu()
        manager.delete(name,BUS)
class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
     ''' Add selection support to the Button '''
     
     selected = BooleanProperty(False)

class RV(BoxLayout,Screen):
    materials1 =[]
    with open('materials.csv', newline = '', encoding = 'utf-8')  as f:
           reader = csv.reader(f)
           for row in reader:
               for row1 in row:
                   materials1.append(row1)
    data_items = ListProperty(materials1)
class BANScreen(Screen):
    scor = NumericProperty(0)
    scor1 = NumericProperty(0)
    
    def ling(self):
        mingcheng = self.ids['ming-cheng'].text
        print(mingcheng)
        a = ChunChu()
        
        res = a.ling(mingcheng)
        self.scor = float(res[1])
        self.scor1 = float(res[2])
    
    def lend_material(self):
        name = self.ids['ming-cheng'].text
        name1 = self.ids['shu-liang'].text
        lingliao = self.ids['juan-shu'].text
        
        manager = ChunChu()
        
        res = manager.check_book(name)
        print('领取的材料是：', res)
        res.amount =float(name1)
        
        res.cylinder=float(lingliao)

        BUS = [res.name,res.amount,res.cylinder]
        print(BUS)
        print('-----------------------------')
        manager = ChunChu()
        manager.delete(name,BUS)
     


           
    

class ScreenApp(App): 
    title = "Kivy RecycleView & SQLite3 Demo"

    def load_kv(self, filename=None):
        with open('Screen.kv', encoding='utf-8') as f:
            Builder.load_string(f.read())
    
    def build(self):
        
        sm = ScreenManager()
        scm = MainScreen(name="main")
        scs = SubScreen(name="sub")
        scn = NeckScreen(name="neck")
        scb = butScreen(name="but")
        sds = RV(name="rvs")
        spd = BANScreen(name="rbd")
        sm.add_widget(scm)
        sm.add_widget(scs)
        sm.add_widget(scn)
        sm.add_widget(scb)
        sm.add_widget(sds)
        sm.add_widget(spd)
        
        return sm
ScreenApp().run()