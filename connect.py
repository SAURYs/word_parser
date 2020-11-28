#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from Ui_main_v1 import Ui_MainWindow
from Ui_help import Ui_MainWindow as Ui_Child_help
from Ui_check_options import Ui_MainWindow as Ui_Child_options
from settings import settings_Ui as Ui_Child_settings
from yml_dump_format2 import *
from yml_format2 import *
from openUI import *
import sys
#from yml_dump_format2 import *

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setting = setting(path)
        self.open_files = Open()
        self.flist = self.open_files.fnames
        #print(self.flist)
        self.ch_help = Child_help()
        #self.ch_options = Child_options()
        #self.main.show()
        self.pushButton_7.clicked.connect(self.open_files.OPEN)
        self.pushButton_3.clicked.connect(self.ch_help.OPEN)
        self.initial_setting_yml = open(path+'\cfg0.yml','r',encoding='utf-8')
        self.initial_setting = yaml.load(self.initial_setting_yml,Loader=yaml.FullLoader)['LASTSET']
        self.initial_setting_yml.close()
        #self.setting.cb_standard.setCurrentText(self.initial_setting)
        self.label_6.setText(self.initial_setting)
        
        #self.pushButton_6.clicked.connect(self.ch_options.OPEN)
        # listView = QListView()

    def setting(self):
        self.setting.show()

class Child_help(QMainWindow, Ui_Child_help):
    def __init__(self):
        super(Child_help, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.msg)
    def msg(self):
        reply = QMessageBox.about(self,"检查更新","当前是最新版本！")
        print( reply )
    def OPEN(self):
        self.show()

""" class Child_options(QMainWindow,Ui_Child_options):
    def __init__(self):
        super(Child_options,self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show() """

class Open(QMainWindow,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.fnames = []
        self.setupUi(self)
        is_textbook = self.radioButton.isChecked()
        if is_textbook:
            print('该用户选择的是教材')
        else:
            print('该用户选择的是论文')
        self.pushButton.clicked.connect(self.getfiles)
        #self.pushButton.clicked.connect(self.close)

    def getfiles(self):
        dlg = QFileDialog()
        self.fnames,_ = dlg.getOpenFileNames(None, '请选择要添加的文件', r'C:\\', "Text Files(*.docx);;All Files(*)")
        #print(self.fnames)
        for i,elem in enumerate(self.fnames):
            main.listWidget.addItem(self.fnames[i])
        self.close()
    def OPEN(self):
        self.show()

class setting(Ui_Child_settings):
    def __init__(self,path):
        super().__init__(path)
        #self.path=path
        
    def selectionchange(self):
        main.label_6.setText(self.cb_standard.currentText())
        self.initial_setting_yml = open(path+'\cfg0.yml','w',encoding='utf-8')
        yaml.dump({'LASTSET':self.cb_standard.currentText()}, self.initial_setting_yml,  allow_unicode=True)
        self.initial_setting_yml.close()

    def view(self):
        for key,val in self.name.items():
            if self.name[key]==self.cb_standard.currentText():
                file=key
        f_path=path+'\\'+file
        #print(f_path)
        self.tab=Tab(f_path)
        self.tab.show()

    def new(self):
        desktop_path =path+'\\'  # 新创建的yml文件的存放路径
        f_new_path = desktop_path + 'cfg' +str(len(self.files_yml)+1) + '.yml'
        self.tab_new=child_save(f_new_path)
        self.tab_new.show()
        # self.cb_standard.addItems(self.tab_new.save(f_new_path)[1])
        # self.currentText()
        # def currentText(self):
        # self.files = os.listdir(path)
        # self.files_yml = [i for i in self.files if i.endswith('.yml')]
        # self.cb_standard.clear()
        # self.cb_standard.addItems(self.file_name(path).values()) 

class child_save(Tab_new):
    def __init__(self,file_path):
        super().__init__()
        self.file_path=file_path

    def save(self,file_path):
        save=1
        if cover_new.save(self,save=1)[1]=='':
            name='配置'+str(len(main.setting.files_yml)+1)
        else:name=cover_new.save(self,save=1)[1]
        standard={"NAME":name,"COVER":cover_new.save(self,save=1)[0],"ABSTRACT":abstract_new.save(self,save=1),"AUTHOR":author_new.save(self,save=1),"PREFACE":preface_new.save(self,save=1),
        "CATALOG":catalog_new.save(self,save=1),"TEXT":text_new.save(self,save=1),"POSTSCRIPT":postscript_new.save(self,save=1),"LITERATURE":literature_new.save(self,save=1),"CHECK":check_box_new.save(self,save=1)}
        #print(standard)
        f = open(self.file_path, "w", encoding="utf-8")
        yaml.dump(standard, f,  allow_unicode=True)
        main.setting.cb_standard.addItems([cover_new.save(self,save=1)[1]])
        #self.cb_standard.addItems([cover.save(self,save=1)[1]])
        f.close()
        return standard  

#class Ui_main(Ui_MainWindow):
#    def __init__(self,file_path):
#        super().__init__()
#    def 

if __name__ =="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    path = os.getcwd()
    main = Main()
    print(main.flist)
    main.show()
    sys.exit(app.exec_())
