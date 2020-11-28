#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from Ui_main_v1 import Ui_MainWindow
#from Ui_input import Ui_MainWindow as Ui_Child
from Ui_help import Ui_MainWindow as Ui_Child_help
from Ui_check_options import Ui_MainWindow as Ui_Child_options
from settings import settings_Ui as Ui_Child_settings
from openUI import *
from yml_dump_format2 import *
from yml_format2 import *
import sys
import os
import yaml
import word_parser
from PyQt5.QtCore import QStringListModel



class Main( QMainWindow,Ui_MainWindow):
    """
    主界面
    """
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        #setting是文件的配置子界面
        self.configuration = setting(path)
        self.open_files = Open()
        self.file_list = self.open_files.fnames
        self.ch_help = Child_help()
        #self.ch_options = Child_options()
        self.pushButton_7.clicked.connect(self.open_files.OPEN)
        self.pushButton_3.clicked.connect(self.ch_help.OPEN)
        self.pushButton_5.clicked.connect(self.begin_check)
        #self.pushButton_6.clicked.connect(self.ch_options.OPEN)
        self.initial_setting_yml = open(path+'\cfg0.yml','r',encoding='utf-8')
        self.initial_setting = yaml.load(self.initial_setting_yml,Loader=yaml.FullLoader)['LASTSET']
        self.initial_setting_yml.close()
        # 路径变量
        self.standard_path = None

        self.label_6.setText(self.initial_setting)
        self.docx_files_path = None
        self.standard_config = None
        self.format_font_size_pt = {'八号': 5, '七号': 5.5, '小六': 6.5, '六号': 7.5, '小五': 9, '五号': 10.5,
                           '小四': 12, '四号': 14, '小三': 15, '三号': 16, '小二': 18, '二号': 22, '一号': 26, '小初': 36}
        # 正文错误
        self.TEXT_font_size_error = []
        self.TEXT_font_name_error = []
        self.TEXT_alignment_error = []
        self.TEXT_space_before_error = []
        self.TEXT_space_after_error = []
        self.TEXT_left_indent_error = []
        self.TEXT_right_indent_error = []
        self.TEXT_first_line_indent_error = []
        
        # 标题错误
        self.title_font_size_error = []
        self.title_font_name_error = []
        self.title_alignment_error = []
        self.title_space_before_error = []
        self.title_space_after_error = []
        self.title_left_indent_error = []
        self.title_right_indent_error = []
        self.title_first_line_indent_error = []
        # 思考题错误
        self.sikaoti_title_error = []
        self.sikaoti_content_error = []
        self.sikaoti_index = []
        # 前言部分格式错误
        self.preface_font_name_error = []
        self.preface_font_size_error = []
        self.preface_alignment_error = []
        # 附录错误
        self.POSTSCRIPT_font_name_error = []
        self.POSTSCRIPT_font_size_error = []
        self.POSTSCRIPT_alignment_error = []
        # 封面页错误：
        self.cover_font_size_error = []
        self.cover_font_name_error = []
        self.cover_alignment_error = []
        self.cover_space_before_error = []
        self.cover_space_after_error = []
        self.cover_left_indent_error = []
        self.cover_right_indent_error = []
        self.cover_first_line_indent_error = []
        # 内容提要错误
        self.abstract_font_size_error = []
        self.abstract_font_name_error = []
        self.abstract_alignment_error = []
        self.abstract_space_before_error = []
        self.abstract_space_after_error = []
        self.abstract_left_indent_error = []
        self.abstract_right_indent_error = []
        self.abstract_first_line_indent_error = []
        # 编审组错误
        self.BSZ_font_size_error = []
        self.BSZ_font_name_error = []
        self.BSZ_alignment_error = []
        self.BSZ_space_before_error = []
        self.BSZ_space_after_error = []
        self.BSZ_left_indent_error = []
        self.BSZ_right_indent_error = []
        self.BSZ_first_line_indent_error = []
        # 参考文献错误
        self.reference_font_size_error = []
        self.reference_font_size_error = []
        self.reference_font_name_error = []
        self.reference_alignment_error = []
        self.reference_space_before_error = []
        self.reference_space_after_error = []
        self.reference_left_indent_error = []
        self.reference_right_indent_error = []
        self.reference_first_line_indent_error = []



    def get_standard(self, path):
        '''
        :param path: 标准文件的路径
        '''
        f = open(path,'r',encoding='utf-8')
        standard = yaml.load(f, Loader = yaml.FullLoader)

        return standard


    def setting(self):
        '''
        显示设置子界面的类函数
        :return:
        '''
        self.configuration.cb_standard.setCurrentText(self.initial_setting)
        self.configuration.show()


    def begin_check(self):
        '''
        检测文件的函数
        :param path: 需要检测的文件路径
        :return: 暂无
        '''
        path = self.docx_files_path
        if path == None:
            QMessageBox.warning(self, "错误", "未选择任何待检测文件!", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        '''
        输出log文件
        '''
        print('要检测的文件名： '+ path)
        diary_log_path = os.path.join(os.getcwd(),r'content.log')
        outputfile = open(diary_log_path,'w',encoding='UTF-8')
        sys.stdout = outputfile

        try:
            QApplication.processEvents()
            self.textBrowser.clear()
            QApplication.processEvents()
            # for index, file_path in enumerate(self.docx_files_path):
            file_path = path
            print(file_path)
            file_name = os.path.basename(file_path)
            self.textBrowser.append(file_name+'检测结果...')
            self.textBrowser.append(' ')
            QApplication.processEvents()
            """
            以下是变量名
            """
            standrad_configration = self.get_standard(r'cfg1.yml')

            # 判断封面页
            print('处理封面页中')
            fmt = word_parser.get_cover_fmt(file_path)
            if fmt != None:
                details = ['内部发行号','系列','机型','书名','分册','适用训练类别','主编','出版社','版次']
                if len(details) == len(fmt):
                    for index, fmt_elem in enumerate(fmt):
                        tmp = word_parser.error_process_unit('COVER',details[index],fmt_elem,standrad_configration)
                        self.cover_font_size_error.append(tmp[0])
                        self.cover_font_name_error.append(tmp[1])
                        self.cover_alignment_error.append(tmp[2])
                else:
                    print('封面页信息不完整无法判断！提示：应包含以下信息：内部发行号,系列,机型,书名,分册,适用训练类别,主编,出版社,版次')
            else:
                pass

            for preface_size_error in self.cover_font_size_error:
                print(preface_size_error)
            for preface_name_error in self.cover_font_name_error:
                print(preface_name_error)
            for preface_alignment_error in self.cover_alignment_error:
                print(preface_alignment_error)

            # 判断摘要页
            print('处理摘要页中...')
            fmt = word_parser.get_informative_abstract_fmt(path)
            if fmt !=None:
                fmt_len = len(fmt)
                details = ['正文']*fmt_len
                details[0] = '内容提要'
                details[-1] = '内部发行'

                if len(details) == len(fmt):
                    for index, fmt_elem in enumerate(fmt):
                        if fmt_elem[0].replace(' ','') == '内容提要':
                            tmp = word_parser.error_process_unit_for_each_para(fmt_elem,standrad_configration['ABSTRACT']['内容提要'].split(),'内容提要' )
                            self.abstract_font_size_error.append(tmp[0])
                            self.abstract_font_name_error.append(tmp[1])
                            self.abstract_alignment_error.append(tmp[2])
                        elif fmt_elem[0].replace(' ','') == '（内部发行）':
                            tmp = word_parser.error_process_unit_for_each_para(fmt_elem, standrad_configration['ABSTRACT']['内部发行'].split(),'内容提要')
                            self.abstract_font_size_error.append(tmp[0])
                            self.abstract_font_name_error.append(tmp[1])
                            self.abstract_alignment_error.append(tmp[2])
                        else:
                            tmp = word_parser.error_process_unit_for_each_para(fmt_elem,standrad_configration['ABSTRACT']['正文'].split(),'内容提要' )
                            self.abstract_font_size_error.append(tmp[0])
                            self.abstract_font_name_error.append(tmp[1])
                            self.abstract_alignment_error.append(tmp[2])

                else:
                    print('封面页信息不完整无法判断！提示：应包含以下信息：内部发行号,系列,机型,书名,分册,适用训练类别,主编,出版社,版次')
            else:
                pass

            for preface_size_error in self.abstract_font_size_error:
                print(preface_size_error)
            for preface_name_error in self.abstract_font_name_error:
                print(preface_name_error)
            for preface_alignment_error in self.abstract_alignment_error:
                print(preface_alignment_error)
            # 判断编审组页
            print('处理编审组页中...')
            # 编审组不调用函数
            fmt = word_parser.get_BSZ_fmt(path)
            standrad_BSZ = standrad_configration['AUTHOR']['编审组'].split()
            standrad_ZUZHANG = standrad_configration['AUTHOR']['组长标题'].split()
            standrad_ZUYUAN = standrad_configration['AUTHOR']['组员'].split()

            for index, content in enumerate(fmt):
                if content[0].endswith('工程') or content[0].endswith('编审组'):
                    res = word_parser.error_process_unit_for_each_para(content,standrad_BSZ,'AUTHOR')
                    self.BSZ_font_size_error.append(res[0])
                    self.BSZ_font_name_error.append(res[1])
                    self.BSZ_alignment_error.append(res[2])
                    self.BSZ_space_before_error.append(res[3])
                    self.BSZ_space_after_error.append(res[4])
                    self.BSZ_left_indent_error.append(res[5])
                    self.BSZ_right_indent_error.append(res[6])
                    self.BSZ_first_line_indent_error.append(res[7])

                elif content[0].replace(' ','')[:2] =='组长':
                    res = word_parser.error_process_unit_two_parts('组长',content,'BSZ',standrad_ZUZHANG,standrad_ZUYUAN)
                    self.BSZ_font_size_error.append(res[0])
                    self.BSZ_font_name_error.append(res[1])
                    # 判断居中方式
                    # 段前距
                    # 段后距
                    # 左缩进
                    # 右缩进
                    # 首行缩进

                elif content[0].replace(' ','')[:3] =='副组长':
                    res = word_parser.error_process_unit_two_parts('副组长', content, 'BSZ', standrad_ZUZHANG, standrad_ZUYUAN)
                    self.BSZ_font_size_error.append(res[0])
                    self.BSZ_font_name_error.append(res[1])

                elif content[0].replace(' ','')[:2] =='组员':
                    res = word_parser.error_process_unit_two_parts('组员', content, 'BSZ', standrad_ZUZHANG, standrad_ZUYUAN)
                    self.BSZ_font_size_error.append(res[0])
                    self.BSZ_font_name_error.append(res[1])

            for preface_size_error in self.BSZ_font_size_error:
                print(preface_size_error)
            for preface_name_error in self.BSZ_font_name_error:
                print(preface_name_error)
            for preface_alignment_error in self.BSZ_alignment_error:
                print(preface_alignment_error)
            for i in self.BSZ_space_before_error:
                print(i)
            for i in self.BSZ_space_after_error:
                print(i)
            for i in self.BSZ_left_indent_error:
                print(i)
            for i in self.BSZ_right_indent_error:
                print(i)
            for i in self.BSZ_first_line_indent_error:
                print(i)
            # 判断前言
            print('处理前言页中...')
            fmt = word_parser.get_preface_fmt(path)
            preface_error = word_parser.process_preface(fmt,standrad_configration,'前言')
            self.preface_font_size_error.append(preface_error[0])
            self.preface_font_name_error.append(preface_error[1])
            self.preface_alignment_error.append(preface_error[2])


            # 处理思考题格式
            '''判断格式之前首先应该判断get_SIKAOTI_fmt返回的结果是否为空'''
            res = word_parser.get_SIKAOTI_fmt(path)
            sikaoti_title_standard = standrad_configration['TEXT']['思考题'].split()
            sikaoti_content_standard = standrad_configration['TEXT'][ '思考题'].split()
            if res[0] != None:
                sikaoti_title = res[0]
                for title in sikaoti_title:
                    self.sikaoti_title_error.append(
                        word_parser.error_process_unit_for_each_para(title, sikaoti_title_standard, '复习思考题标题'))
            if res[1] != None:
                sikaoti_content = res[1]
                for content in sikaoti_content:
                    self.sikaoti_content_error.append(
                        word_parser.error_process_unit_for_each_para(content, sikaoti_content_standard, '复习思考题题目'))
            if res[2] != None:
                self.sikaoti_index = res[2]






            # 判断目录
            # 判断正文
            """
            该正文已经去除了各级标题、图表标题、思考题，剩下得是需要判别的正文
            """
            standard_main_body = standrad_configration['TEXT']['正文']
            title_index = word_parser.get_title_index(path)
            title_index = title_index+self.sikaoti_index
            main_part_error = word_parser.process_main_body(path,standard_main_body,title_index)
            self.TEXT_font_size_error.append(main_part_error[0])
            self.TEXT_font_name_error.append(main_part_error[1])
            self.TEXT_alignment_error.append(main_part_error[2])
            self.TEXT_space_before_error.append(main_part_error[3])
            self.TEXT_space_after_error.append(main_part_error[4])
            self.TEXT_left_indent_error.append(main_part_error[5])
            self.TEXT_right_indent_error.append(main_part_error[6])
            self.TEXT_first_line_indent_error.append(main_part_error[7])
            for i in self.TEXT_font_size_error:
                print(i)
            for i in self.TEXT_font_name_error:
                print(i)
            for i in self.TEXT_alignment_error:
                print(i)
            for i in self.TEXT_space_before_error:
                print(i)
            for i in self.TEXT_space_after_error:
                print(i)
            for i in self.TEXT_left_indent_error:
                print(i)
            for i in self.TEXT_right_indent_error:
                print(i)
            # 首行缩进没写

            # 判断标题信息
            ''''暂时不包含篇的检测'''
            print('开始处理判断标题格式正确性...')
            title_standard_temp =standrad_configration['TEXT']
            title_type = ['章标题','节标题','条标题','款标题']
            #title_standard = title_standard[1:5]
            title_standard = []
            # title_standard[0] = title_standard_temp['TEXT']['篇']
            title_standard.append(title_standard_temp['章'])
            title_standard.append(title_standard_temp['节'])

            title_standard.append(title_standard_temp['条'])

            title_standard.append(title_standard_temp['款'])


            title_set = word_parser.get_numbered_title(path)
            titile_type_size = len(title_set)
            for type_index, each_type_set in enumerate(title_set[:4]):
                for each_title in each_type_set:
                    error_res = word_parser.error_process_unit_for_each_para(each_title,title_standard[type_index].split(), title_type[type_index])
                    print(error_res[0])
                    print(error_res[1])
                    print(error_res[2])
                    print(error_res[3])
                    print(error_res[4])
                    print(error_res[5])
                    print(error_res[6])
                    print(error_res[7])
                    self.title_font_size_error.append(error_res[0])
                    self.title_font_name_error.append(error_res[1])
                    self.title_alignment_error.append(error_res[2])
                    self.title_space_before_error.append(error_res[3])
                    self.title_space_after_error.append(error_res[4])
                    #self.title_alignment_error.append(error_res[5])
                    self.title_left_indent_error.append(error_res[5])
                    self.title_right_indent_error.append(error_res[6])
                    self.title_first_line_indent_error.append(error_res[7])


            # 判断附录页
            fmt, sec_fmt = word_parser.get_appendix_format(path)
            if fmt != None and len(fmt) == 1:
                tmp = word_parser.error_process_unit('POSTSCRIPT', '附录', fmt, standrad_configration)
                self.font_size_error.append(tmp[0])
                self.font_name_error.append(tmp[1])
                self.alignment_error.append(tmp[2])
            else:
                print('附录页信息不完整无法判断！提示：有且仅有一个大附录标题')
            if sec_fmt != None:
                sec_fmt_len = len(sec_fmt)
                details = ['标题下附录'] * sec_fmt_len
                if len(details) == sec_fmt_len:
                    for index, sec_fmt_elem in enumerate(sec_fmt):
                        tmp = word_parser.error_process_unit('POSTSCRIPT', details[index], sec_fmt_elem,
                                                 standrad_configration)
                        print(tmp[0])
                        print(tmp[1])
                        print(tmp[2])
                        self.POSTSCRIPT_font_size_error.append(tmp[0])
                        self.POSTSCRIPT_font_name_error.append(tmp[1])
                        self.POSTSCRIPT_alignment_error.append(tmp[2])
                else:
                    pass
            else:
                pass  # 二级附录可无
            for i in self.POSTSCRIPT_font_size_error:
                print(i)
            for i in self.POSTSCRIPT_font_size_error:
                print(i)
            # 判断文献页
            print('开始处理文献页...')
            fmt = word_parser.get_reference_format(path)

            if fmt != None:
                fmt_len = len(fmt)
                details = ['文献'] * fmt_len
                details[0] = '参考文献'
                if len(details) == len(fmt):
                    for index, fmt_elem in enumerate(fmt):
                        tmp = word_parser.error_process_unit('LITERATURE', details[index], fmt_elem, standrad_configration)
                        self.reference_font_size_error.append(tmp[0])
                        self.reference_font_name_error.append(tmp[1])
                        self.reference_alignment_error.append(tmp[2])
                else:
                    print('参考文献页信息不完整无法判断！提示：应包含以下信息：参考文献，文献')
            else:
                pass
            for i in self.reference_font_size_error:
                print(i)
            for i in self.reference_font_name_error:
                print(i)
            for i in self.reference_alignment_error:
                print(i)
        except IOError:
            print('IOError')







class Child_help(QMainWindow, Ui_Child_help):
    '''
    帮助子界面
    '''
    def __init__(self):
        super(Child_help, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.msg)
    #  def msg(self):
    #     reply = QMessageBox.about(self,"检查更新","当前是最新版本！")
    #     print( reply ) 
    def OPEN(self):
        self.show()


'''class Child_options(QMainWindow,Ui_Child_options):
    def __init__(self):
        super(Child_options,self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()'''

class Open(QMainWindow,Ui_Form):
    """
    这是打开文件的子界面
    """
    def __init__(self):
        super().__init__()
        self.fnames = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getfiles)

    def getfiles(self):
        '''
        获取文件路径（可多选）
        :return:
        '''
        dlg = QFileDialog()
        self.fnames,_ = dlg.getOpenFileName(None, '请选择要添加的文件', r'C:\\', "Text Files(*.docx);;All Files(*)")
        # 只支持一次添加
        main.docx_files_path = self.fnames

        _, names = os.path.split(self.fnames)
        main.listWidget.addItem(names)
        self.close()

    def OPEN(self):
        '''
        子界面的展示函数
        :return:
        '''
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
            name='配置'+str(len(main.configuration.files_yml)+1)
        else:name=cover_new.save(self,save=1)[1]
        standard={"NAME":name,"COVER":cover_new.save(self,save=1)[0],"ABSTRACT":abstract_new.save(self,save=1),"AUTHOR":author_new.save(self,save=1),"PREFACE":preface_new.save(self,save=1),
        "CATALOG":catalog_new.save(self,save=1),"TEXT":text_new.save(self,save=1),"POSTSCRIPT":postscript_new.save(self,save=1),"LITERATURE":literature_new.save(self,save=1),"CHECK":check_box_new.save(self,save=1)}
        #print(standard)
        f = open(self.file_path, "w", encoding="utf-8")
        yaml.dump(standard, f,  allow_unicode=True)
        main.configuration.cb_standard.addItems([cover_new.save(self,save=1)[1]])
        #self.cb_standard.addItems([cover.save(self,save=1)[1]])
        f.close()
        return standard  

if __name__ =="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    path = os.getcwd()
    main = Main()
    main.show()
    sys.exit(app.exec_())