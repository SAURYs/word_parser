import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from yml_format2 import *

import os
import yaml


class settings_Ui(QWidget):#,over
    def __init__(self,path):#
        super().__init__()
        self.path=path
        self.setWindowTitle("配置")        
        self.resize(300, 90)
        layout_settings = QGridLayout()
        self.cb_standard = QComboBox()

        self.files = os.listdir(self.path)
        self.files_yml = [i for i in self.files if i.endswith('.yml')]
        self.files_yml.remove('cfg0.yml')

        self.name={}
        for i in self.files_yml:
            self.file_path=self.path+'\\'+i
            f = open(self.file_path,'r',encoding='utf-8')
            self.context = yaml.load(f,Loader=yaml.FullLoader)
            self.name[i]=self.context['NAME']
        self.cb_standard.addItems(self.name.values())

        self.cb_standard.currentIndexChanged.connect(self.selectionchange)
        layout_settings.addWidget(self.cb_standard)

        self.btn1 = QPushButton("查看")
        self.btn1.clicked.connect(self.view)
        layout_settings.addWidget(self.btn1)

        self.btn2 = QPushButton('新建')
        self.btn2.clicked.connect(self.new)
        layout_settings.addWidget(self.btn2)
        
        self.setLayout(layout_settings)

    """  def file_name(self):
        self.name={}
        for i in self.files_yml:
            self.file_path=self.path+'\\'+i
            f = open(self.file_path,'r',encoding='utf-8')
            self.context = yaml.load(f,Loader=yaml.FullLoader)
            self.name[i]=self.context['NAME']
        #print(name)
        #print(name.values())
        return self.name """


    """ def selectionchange(self):
        print(self.cb_standard.currentText())

    def view(self):
        for key,val in self.name.items():
            if self.name[key]==self.cb_standard.currentText():
                file=key
        f_path=self.path+'\\'+file
        #print(f_path)
        self.tab=Tab(f_path)
        self.tab.show()

    def new(self):
        desktop_path = self.path+'\\'  # 新创建的yml文件的存放路径
        f_new_path = desktop_path + 'cfg' +str(len(self.files_yml)+1) + '.yml'
        self.tab_new=Tab_new(f_new_path)
        self.tab_new.show()
        # self.cb_standard.addItems(self.tab_new.save(f_new_path)[1])
        self.currentText()
    
    def currentText(self):
        self.files = os.listdir(self.path)
        self.files_yml = [i for i in self.files if i.endswith('.yml')]
        self.cb_standard.clear()
        self.cb_standard.addItems(self.file_name().values())   """


""" class settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("配置")        
        self.resize(300, 90)                       
        
        self.setLayout(settings_options().widget())"""

if __name__ == '__main__':

    app = QApplication(sys.argv)
    path = os.getcwd()
    settings = settings_Ui(path)
    settings.show()
    sys.exit(app.exec_())


""" path = 'D:\Project\pyqt' 
files = os.listdir(path)
files_yml = [i for i in files if i.endswith('.yml')]
print(files_yml)
print(len(files_yml))
name={}
for i in files_yml:
    file_path=f'D:\Project\pyqt\{i}'
    f = open(file_path,'r',encoding='utf-8')
    context = yaml.load(f,Loader=yaml.FullLoader)
    name[i]=context['NAME']
print(name)
print(name.values()) """