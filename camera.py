from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty
)
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
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
    # score = NumericProperty(0)
    

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
        
 
class NeckScreen(Screen):
    
    score = NumericProperty(0)
    score1 = NumericProperty(0)
    score2 = NumericProperty(0)
    score3 = NumericProperty(0)

    def __init__(self, **kwargs):
        super(NeckScreen, self).__init__(**kwargs)
        self.materials = []
        with open('materials.csv', newline = '', encoding = 'utf-8')  as f:
           reader = csv.reader(f)
           for row in reader:
              print(row)
              material = Material(row[0],row[1],row[2])
              self.materials.append(material)
              
    
    def ling(self):
        mingcheng = self.ids['ming-cheng']
        

        print(mingcheng)
        with open('materials.csv','r', newline = '', encoding = 'utf-8')  as f:
           row1 = csv.reader(f)
           for row in row1:
               if mingcheng.text==row[0]:
                   self.score = float(row[1])
                   self.score1 = float(row[2])
                   #####



                   #####
    
    #  def menu(self):
    #     print('欢迎来到材料管理系统，数据很重要，请谨慎操作。\n')
    #     while True:
    #         print('1.显示所有材料\n2.领料\n3.入库\n4.退出系统\n')
    #         choice = int(input('请输入数字选择对应的功能：'))
    #         if choice == 1:
    #             self.show_all_materials()
    #         elif choice == 2:
    #             self.lend_materials()
    #         elif choice == 3:
    #             self.but_materials()
    #         elif choice == 4:
    #            print('感谢您认真的工作，很荣幸再次给您带来服务')
    #            break
    #  def show_all_materials(self):
    #     print('材料信息如下：')
    #     for book in self.materials:
    #         print(book)
    def check_book(self,name):
        print('111',name)
        for book in self.materials:
            if book.name == name:
                return book
    def delete(self):
        
        ls3 = []
        for book in self.materials:
           book2 = [book.name,book.amount,book.cylinder]
           ls3.append(book2)
        a = ['材料名称','材料重量','材料卷数','材料用途']
        with open('materials.csv','w', newline = '', encoding = 'utf-8')  as f:
           writer = csv.writer(f)
           writer.writerow(a)
        ls4 = ls3
        for ls5 in ls4:
           with open('materials.csv','a',newline = '', encoding = 'utf-8')  as f:
              writer = csv.writer(f)
              writer.writerow(ls5)
              
    def lend_materials(self):
        name = self.ids['ming-cheng'].text
        lingliao = self.ids['ling-liao'].text
        # name = input('请输入材料的名称：')
        # cylinder =input('请输入所领卷数：')
        res = self.check_book(name)
        print('领取的材料是：', res)
        requisition =float(res.amount)/float(res.cylinder)
        univolume1 =float(requisition)*int(lingliao)
        univolume2 =int(univolume1)
        print('领取材料重量：', univolume2)
        self.score3 = int(univolume2)
        res.amount=float(res.amount)-univolume2

        cylinder=float(res.cylinder)-float(lingliao)
        res.cylinder=round(cylinder,0)
        # res.cylinder=int(cylinder)
        print('领取后，材料剩余是：',res)
        self.delete()
        
              
    # def but_materials(self):
    #     name = input('请输入材料的名称：')
    #     amount = input('请输入入库数量：')
    #     cylinder =input('请输入要入库卷数：')
    #     res = self.check_book(name)
    #     print('入库的材料是：', res)
    #     res.amount =int(res.amount)+int(amount)
    #     res.cylinder =int(res.cylinder)+int(cylinder)
    #     print('入库后材料的重量：', res.amount)
    #     print('入库后材料的卷数：', res.cylinder)
    #     self.delete()



        #####
    # def liao(self):
    #     mingcheng = self.ids['ming-cheng']
    #     lingliao = self.ids['ling-liao']
       
    #     print(mingcheng)
    #     with open('materials.csv','r', newline = '', encoding = 'utf-8')  as f:
    #        row2 = csv.reader(f)
    #        for row in row2:
    #            if mingcheng.text==row[0]:
    #                univolume = float(row[1])/float(row[2])
    #                univolume1 = univolume*float(lingliao.text)
    #                print(univolume1)
    #                self.score3 = int(univolume1)

                   
                                
class ScreenApp(App): 

    def load_kv(self, filename=None):
        with open('Screen.kv', encoding='utf-8') as f:
            Builder.load_string(f.read())
    
    def build(self):
        
        sm = ScreenManager()
        scm = MainScreen(name="main")
        scs = SubScreen(name="sub")
        scn = NeckScreen(name="neck")
        sm.add_widget(scm)
        sm.add_widget(scs)
        sm.add_widget(scn)
        
        return sm
ScreenApp().run()