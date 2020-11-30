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
        self.text_error = []
        
        # 标题错误
        self.title_error = []

        # 思考题错误
        self.sikaoti_title_error = []
        self.sikaoti_content_error = []
        self.sikaoti_index = []
        # 前言部分格式错误
        self.preface_error = []
        # 附录错误
        self.postscript_error = []

        # 封面页错误：
        self.cover_error = []

        # 内容提要错误
        self.abstract_error = []
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
        self.reference_error = []
        # 缺少的标题
        self.title_absence = None
        # 标题顺序错误
        self.title_wrong_order = None
        # 图表序号与标题正文之间空一字 ie. 图2-2 流畅的python
        self.title_space_error =[]

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
            #print(main.configuration.name)
            #current_name=main.label_6.text()
            #current_file= k for (k,v) in main.configuration.name.items() if v == current_name
            #print(main.configuration.name)
            current_name=main.label_6.text()
            def get_key2(dct, value):
                return [k for (k,v) in dct.items() if v == value]
            current_file=get_key2(main.configuration.name,current_name)
            standrad_configration = self.get_standard(current_file[0])
            print(current_file[0],current_name)
            self.textBrowser.append(f'当前检测配置名称{current_name}')
            QApplication.processEvents()

            """
            其他检测选项
            """
            title_check = standrad_configration['CHECK']['检测标题连续性']
            image_title_continue_check = standrad_configration['CHECK']['检测图片标题连续性']
            table_title_continue_check = standrad_configration['CHECK']['检测表格标题']
            postscript_title_continue_check = standrad_configration['CHECK']['检测附录编号顺序连续性']
            reference_title_continue_check = standrad_configration['CHECK']['检测参考文献顺序连续性']

            """===================================================================================="""
            # 输出文章所有能用python.docx提取出来的内容
            # word_parser.show_all_content_fmt(path)
            # 处理正文Normal样式
            word_parser.normal_font_name, word_parser.normal_Chinese_font_name = word_parser.decide_style_normal(path)
            # 处理正文标题连续性
            res, all_title_fmt = word_parser.title_continuity(path)
            if title_check:
                self.title_absence = res[0]
                self.title_wrong_order = res[1]
            # 处理图标题连续性
            if image_title_continue_check:
                pass
            # 处理表标题连续性
            if table_title_continue_check:
                pass
            # 检测附录编号顺序连续性
            if postscript_title_continue_check:
                pass
            # 检测参考文献顺序连续性
            if reference_title_continue_check:
                pass

            # 表标题/图表题是否序号与标题内容之间空一字
            image_title_fmt = all_title_fmt[5]
            if len(image_title_fmt):
                for elem in image_title_fmt:
                    image_title = elem[0]
                    if word_parser.table_title_has_space(image_title):
                        self.title_space_error.append(image_title)
            figure_title_fmt = all_title_fmt[6]
            if len(figure_title_fmt):
                for elem in figure_title_fmt:
                    table_title = elem[0]
                    if word_parser.table_title_has_space(table_title):
                        self.title_space_error.append(table_title)

            print('本文中图/表标题序号与图名之间没有空一字的有：'+str(len(self.title_space_error))+'个：')
            print(self.title_space_error)

            # 判断封面页
            print('处理封面页中')
            fmt = word_parser.get_cover_fmt(file_path)
            if fmt != None:
                details = ['内部发行号','系列','机型','书名','分册','适用训练类别','主编','出版社','版次']
                if len(details) == len(fmt):
                    for index, fmt_elem in enumerate(fmt):
                        tmp = word_parser.error_process_unit('COVER',details[index],fmt_elem,standrad_configration)
                        self.cover_error.append(tmp)
                else:
                    print('封面页信息不完整无法判断！提示：应包含以下信息：内部发行号,系列,机型,书名,分册,适用训练类别,主编,出版社,版次')
            else:
                pass
            for i in self.cover_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
                sys.stdout.flush()

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
                            self.abstract_error.append(word_parser.error_process_unit_for_each_para(fmt_elem,standrad_configration['ABSTRACT']['内容提要'].split(),'内容提要' ))
                        elif fmt_elem[0].replace(' ','') == '（内部发行）':
                            self.abstract_error.append(word_parser.error_process_unit_for_each_para(fmt_elem, standrad_configration['ABSTRACT']['内部发行'].split(),'内容提要'))
                        else:
                            self.abstract_error.append(word_parser.error_process_unit_for_each_para(fmt_elem,standrad_configration['ABSTRACT']['正文'].split(),'内容提要' ))

                else:
                    print('封面页信息不完整无法判断！提示：应包含以下信息：内部发行号,系列,机型,书名,分册,适用训练类别,主编,出版社,版次')
            else:
                pass
            for i in self.abstract_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
            # 判断编审组页
            print('处理编审组页中...')
            # 编审组不调用函数
            fmt = word_parser.get_BSZ_fmt(path)
            if fmt == None:
                print('没有找到编审组页！！！')
            else:
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
                    self.textBrowser.append(str(i))
                    QApplication.processEvents()
                for i in self.BSZ_space_after_error:
                    print(i)
                    self.textBrowser.append(str(i))
                    QApplication.processEvents()
                for i in self.BSZ_left_indent_error:
                    print(i)
                    self.textBrowser.append(str(i))
                    QApplication.processEvents()
                for i in self.BSZ_right_indent_error:
                    print(i)
                    self.textBrowser.append(str(i))
                    QApplication.processEvents()
                for i in self.BSZ_first_line_indent_error:
                    print(i)
                    self.textBrowser.append(str(i))
                    QApplication.processEvents()

            # 判断前言
            print('处理前言页中...')
            fmt = word_parser.get_preface_fmt(path)
            self.preface_error = word_parser.process_preface(fmt,standrad_configration,'前言')
            for i in self.preface_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
            sys.stdout.flush()



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
            print('思考题标题错误...')
            for index,content in enumerate(self.sikaoti_title_error):
                print("第%d章复习思考题标题错误:"% (index+1))
                print(content)
            print('处理思考题内容...')
            for index,content in enumerate(self.sikaoti_content_error):
                """
                未定位具体位置
                """
                print(content)






            # 判断目录
            # 判断正文
            """
            该正文已经去除了各级标题、图表标题、思考题，剩下得是需要判别的正文
            """
            print('处理正文中...')
            standard_main_body = standrad_configration['TEXT']['正文']
            title_index = word_parser.get_title_index(path)
            title_index = title_index+self.sikaoti_index
            main_part_error = word_parser.process_main_body(path,standard_main_body,title_index)
            for i in main_part_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
            sys.stdout.flush()
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
                    self.text_error.append(error_res)
            for i in self.text_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
            # 处理表格、图像标题

            # 判断附录页
            print('开始处理附录页...')
            fmt, sec_fmt = word_parser.get_appendix_format(path)
            if fmt != None and len(fmt) == 1:
                self.postscript_error.append(word_parser.error_process_unit('POSTSCRIPT', '附录', fmt, standrad_configration))
            else:
                print('附录页信息不完整无法判断！提示：有且仅有一个大附录标题')
            if sec_fmt != None:
                sec_fmt_len = len(sec_fmt)
                details = ['标题下附录'] * sec_fmt_len
                if len(details) == sec_fmt_len:
                    for index, sec_fmt_elem in enumerate(sec_fmt):
                        self.postscript_error.append(word_parser.error_process_unit('POSTSCRIPT', details[index], sec_fmt_elem, standrad_configration))

                else:
                    pass
            else:
                pass  # 二级附录可无
            for i in self.postscript_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
                sys.stdout.flush()
            # 判断文献页
            print('开始处理文献页...')
            fmt = word_parser.get_reference_format(path)

            if fmt != None:
                fmt_len = len(fmt)
                details = ['文献'] * fmt_len
                details[0] = '参考文献'
                if len(details) == len(fmt):
                    for index, fmt_elem in enumerate(fmt):
                        self.reference_error.append(word_parser.error_process_unit('LITERATURE', details[index], fmt_elem, standrad_configration))

                else:
                    print('参考文献页信息不完整无法判断！提示：应包含以下信息：参考文献，文献')
            else:
                pass
            for i in self.reference_error:
                print(i)
                self.textBrowser.append(str(i))
                QApplication.processEvents()
            self.textBrowser.append('检测完成！')
            self.textBrowser.append(' ')

            QApplication.processEvents()
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
