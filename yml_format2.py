import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import yaml
""" file_path='D:\Project\pyqt\standard.yml'
f = open(file_path,'r',encoding='utf-8')
context = yaml.load(f,Loader=yaml.FullLoader)
cover = context["COVER"]
print(cover['内部发行号'].split(' '))
print(cover)
abstract = context["ABSTRACT"] """

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class format(QWidget):
    def __init__(self):
        super().__init__()

    def format_widget(self,list=[],alignenable=0,beforeenable=0,afterenable=0,leftenable=0,rightenable=0):
        '''传入参数依次为:当前字号(需为字号list中string)，当前字体(需为字体list中string)，当前对齐方式(需为对齐方式list中string)，
        当前段前距，当前段后距,左缩进当前值，右缩进当前值 对齐方式启动(1为启动,下同)，段前距启动，段后距启动，左缩进启动，右缩进启动，
        默认值为 宋体，五号，左对齐，所有控件关闭，数值为0，   所有参数需通过关键字参数传入'''
        layout=layout=QHBoxLayout()

        cb_fontsize= QComboBox()
        cb_fontsize.addItems(["五号","小五","四号","小四","三号","小三","二号","小二","小初"])
        cb_fontsize.setCurrentText(list[0])
        cb_fonts= QComboBox()
        cb_fonts.addItems(["宋体","楷体","黑体", "微软雅黑", "仿宋","方正北魏楷体","方正小标宋简","方正大标宋简"])
        cb_fonts.setCurrentText(list[1])
        layout.addWidget(cb_fontsize)
        layout.addWidget(cb_fonts)

        Lb_alignment = QLabel('对齐方式')
        cb_alignment= QComboBox()
        cb_alignment.addItems(["左对齐","居中","右对齐","两端对齐","分散对齐"])
        layout.addWidget(Lb_alignment)
        layout.addWidget(cb_alignment)
        cb_alignment.setEnabled(False)
        if alignenable==1:
            cb_alignment.setEnabled(True)
        cb_alignment.setCurrentIndex(int(list[2]))

        Lb_space_before = QLabel('段前距/行')
        sp_space_before=QDoubleSpinBox()
        sp_space_before.setDecimals(1)
        layout.addWidget(Lb_space_before)
        layout.addWidget(sp_space_before)
        sp_space_before.setEnabled(False)
        if beforeenable==1:
            sp_space_before.setEnabled(True)
        sp_space_before.setValue(float(list[3]))

        Lb_space_after = QLabel('段后距/行')
        sp_space_after=QDoubleSpinBox()
        sp_space_after.setDecimals(1)
        layout.addWidget(Lb_space_after)
        layout.addWidget(sp_space_after)
        sp_space_after.setEnabled(False)
        if afterenable==1:
            sp_space_after.setEnabled(True)
        sp_space_after.setValue(float(list[4]))

        Lb_indent_left= QLabel('左缩进/字符')
        sp_indent_left=QSpinBox()
        layout.addWidget(Lb_indent_left)
        layout.addWidget(sp_indent_left)
        sp_indent_left.setEnabled(False)
        if leftenable==1:
            sp_indent_left.setEnabled(True)
        sp_indent_left.setValue(int(list[5]))

        Lb_indent_right= QLabel('右缩进/字符')
        sp_indent_right=QSpinBox()
        layout.addWidget(Lb_indent_right)
        layout.addWidget(sp_indent_right)
        sp_indent_right.setEnabled(False)
        if rightenable==1:
            sp_indent_right.setEnabled(True)
        sp_indent_right.setValue(int(list[6]))
        
        layout_widget=QWidget()
        layout_widget.setLayout(layout)
        return layout_widget #返回横向布局的控件及保存值的列表

class cover(format):
    #返回封面页的控件
    def __init__(self):
        super().__init__()
        
    """  COVER: 
    #名称: 字号 字体 居中 段前 段后 左缩进 右缩进 对齐方式 
    内部发行号: 四号 黑体 None None   
    系列: 四号 方正北魏楷体 None None
    机型: 小二 方正小标宋简 居中 400 #段前距
    书名: 初号 方正大标宋简 居中 
    """
    def cover_widget(self,context):
        cover_text = context["COVER"]

        layout1 = QHBoxLayout()
        Lb_cover1 = QLabel('内部发行号')
        cover1_text=cover_text['内部发行号'].split(' ')
        Wgt1=self.format_widget(cover1_text)

        layout1.addWidget(Lb_cover1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        Lb_cover2 = QLabel('系      列')
        cover2_text=cover_text['系列'].split(' ')
        Wgt2=self.format_widget(cover2_text)
        layout2=QHBoxLayout()
        layout2.addWidget(Lb_cover2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        Lb_cover3 = QLabel('机      型')
        cover3_text=cover_text['机型'].split(' ')
        Wgt3=self.format_widget(cover3_text)
        layout3=QHBoxLayout()
        layout3.addWidget(Lb_cover3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        Lb_cover4 = QLabel('书      名')
        cover4_text=cover_text['书名'].split(' ')
        Wgt4=self.format_widget(cover4_text)
        layout4=QHBoxLayout()
        layout4.addWidget(Lb_cover4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)
        """分册: 小二 宋体 居中 100
        适用训练类别: 三号 仿宋 居中 100 #段前
        主编: 四号 黑体 居中 100
        出版社: 四号 黑体 居中 
        版次: 小四 宋体 居中 50 200  #段后"""
        Lb_cover5 = QLabel('分      册')
        cover5_text=cover_text['分册'].split(' ')
        Wgt5=self.format_widget(cover5_text)
        #Wgt5=self.format_widget(current_fontsize='小二',current_font='宋体', current_align="居中", current_before=1)
        layout5=QHBoxLayout()
        layout5.addWidget(Lb_cover5)
        layout5.addWidget(Wgt5)
        layout5_widget=QWidget()
        layout5_widget.setLayout(layout5)

        Lb_cover6 = QLabel('适用训练类别')
        cover6_text=cover_text['适用训练类别'].split(' ')
        Wgt6=self.format_widget(cover6_text)
        #Wgt6=self.format_widget(current_fontsize='三号',current_font='仿宋', current_align="居中", current_before=1)
        layout6=QHBoxLayout()
        layout6.addWidget(Lb_cover6)
        layout6.addWidget(Wgt6)
        layout6_widget=QWidget()
        layout6_widget.setLayout(layout6)

        Lb_cover7 = QLabel('主      编')
        cover7_text=cover_text['主编'].split(' ')
        Wgt7=self.format_widget(cover7_text)
        #Wgt7=self.format_widget(current_fontsize='四号',current_font='黑体', current_align="居中", current_before=1)
        layout7=QHBoxLayout()
        layout7.addWidget(Lb_cover7)
        layout7.addWidget(Wgt7)
        layout7_widget=QWidget()
        layout7_widget.setLayout(layout7)

        Lb_cover8 = QLabel('出  版  社')
        cover8_text=cover_text['出版社'].split(' ')
        Wgt8=self.format_widget(cover8_text)
        #Wgt8=self.format_widget(current_fontsize='四号',current_font='黑体', current_align="居中")
        layout8=QHBoxLayout()
        layout8.addWidget(Lb_cover8)
        layout8.addWidget(Wgt8)
        layout8_widget=QWidget()
        layout8_widget.setLayout(layout8)

        Lb_cover9 = QLabel('版      次')
        cover9_text=cover_text['版次'].split(' ')
        Wgt9=self.format_widget(cover9_text)
        #Wgt9=self.format_widget(current_fontsize='小四',current_font='宋体', current_align="居中", current_before=0.5,  current_after=2)
        layout9=QHBoxLayout()
        layout9.addWidget(Lb_cover9)
        layout9.addWidget(Wgt9)
        layout9_widget=QWidget()
        layout9_widget.setLayout(layout9)

        layout_cover =QVBoxLayout()
        layout_cover.addWidget(layout1_widget)
        layout_cover.addWidget(layout2_widget)
        layout_cover.addWidget(layout3_widget)
        layout_cover.addWidget(layout4_widget)
        layout_cover.addWidget(layout5_widget)
        layout_cover.addWidget(layout6_widget)
        layout_cover.addWidget(layout7_widget)
        layout_cover.addWidget(layout8_widget)
        layout_cover.addWidget(layout9_widget)
        
        cover_widget=QWidget()
        cover_widget.setLayout(layout_cover)

        return cover_widget 

class abstract(format):
    #返回内容提要页控件
    def __init__(self):
        super().__init__()
    
    def abstract_widget(self,context):
        '''ABSTRACT:
        内容提要: 五号 黑体 居中 
        正文: 小五 宋体
        内部发行: 小五 宋体 None 50 200 #段后'''

        abstract_text = context["ABSTRACT"]
        layout1 = QHBoxLayout()
        Lb_abstract1 = QLabel("内容提要")
        abstract1_text=abstract_text['内容提要'].split(' ')
        Wgt1=self.format_widget(abstract1_text)
        #Wgt1=self.format_widget(current_fontsize='五号',current_font='黑体',current_align='居中')
        layout1.addWidget(Lb_abstract1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        layout2 = QHBoxLayout()
        Lb_abstract2 = QLabel("正     文")
        abstract2_text=abstract_text['正文'].split(' ')
        Wgt2=self.format_widget(abstract2_text)
        layout2.addWidget(Lb_abstract2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_abstract3 = QLabel("内部发行")
        abstract3_text=abstract_text['内部发行'].split(' ')
        Wgt3=self.format_widget(abstract3_text)
        layout3.addWidget(Lb_abstract3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        layout_abstract =QVBoxLayout()
        layout_abstract.addWidget(layout1_widget)
        layout_abstract.addWidget(layout2_widget)
        layout_abstract.addWidget(layout3_widget)
        
        abstract_widget=QWidget()
        abstract_widget.setLayout(layout_abstract)

        return abstract_widget

class author(format):
    #返回作者页控件
    def __init__(self):
        super().__init__()
    
    def author_widget(self,context):
        '''AUTHOR:
        编审组: 小二 黑体 居中
        组长标题: 三号 黑体
        组员: 三号 楷体'''

        author_text=context["AUTHOR"]
        layout1 = QHBoxLayout()
        Lb_author1 = QLabel("编审组")
        author1_text=author_text['编审组'].split(' ')
        Wgt1=self.format_widget(author1_text)
        
        #Wgt1=self.format_widget(current_fontsize='小二',current_font='黑体', current_align='居中')
        layout1.addWidget(Lb_author1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        layout2 = QHBoxLayout()
        Lb_author2 = QLabel("组长标题")
        author2_text=author_text['组长标题'].split(' ')
        Wgt2=self.format_widget(author2_text)
        #Wgt2=self.format_widget(current_fontsize='三号',current_font='黑体')
        layout2.addWidget(Lb_author2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_author3 = QLabel("组员")
        author3_text=author_text['组员'].split(' ')
        Wgt3=self.format_widget(author3_text)
        
        #Wgt3=self.format_widget(current_fontsize='三号',current_font='楷体')
        layout3.addWidget(Lb_author3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        layout_author =QVBoxLayout()
        layout_author.addWidget(layout1_widget)
        layout_author.addWidget(layout2_widget)
        layout_author.addWidget(layout3_widget)
        
        author_widget=QWidget()
        author_widget.setLayout(layout_author)

        return author_widget

class preface(format):
    #返回前言页孔家
    def __init__(self):
        super().__init__()
    
    def preface_widget(self,context):
        '''PREFACE:
        前言: 小二 黑体 居中 300 200 #段后
        正文: 五号 宋体 
        编者: 四号 楷体 None 200 None None 400 right #对齐方式
        时间: 四号 宋体 None None None None 300 right #对齐方式'''
        preface_text=context["PREFACE"]
        layout1 = QHBoxLayout()
        Lb_preface1 = QLabel("前言")
        preface1_text=preface_text['前言'].split(' ')
        Wgt1=self.format_widget(preface1_text)
        
        #Wgt1=self.format_widget(current_fontsize='小二',current_font='黑体',current_align='居中',current_before=3,current_after=2)
        layout1.addWidget(Lb_preface1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_preface2 = QLabel("正文")
        preface2_text=preface_text['正文'].split(' ')
        Wgt2=self.format_widget(preface2_text)

        #Wgt2=self.format_widget(current_fontsize='五号',current_font='宋体')
        layout2.addWidget(Lb_preface2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_preface3 = QLabel("编者")
        preface3_text=preface_text['编者'].split(' ')
        Wgt3=self.format_widget(preface3_text)

        #Wgt3=self.format_widget(current_fontsize='四号',current_font='楷体',current_align='右对齐',current_before=2,current_right=4)
        layout3.addWidget(Lb_preface3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        layout4 = QHBoxLayout()
        Lb_preface4 = QLabel("时间")
        preface4_text=preface_text['时间'].split(' ')
        Wgt4=self.format_widget(preface4_text)

        #Wgt4=self.format_widget(current_fontsize='四号',current_font='宋体',current_align='右对齐',current_right=3)
        layout4.addWidget(Lb_preface4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)

        layout_preface =QVBoxLayout()
        layout_preface.addWidget(layout1_widget)
        layout_preface.addWidget(layout2_widget)
        layout_preface.addWidget(layout3_widget)
        layout_preface.addWidget(layout4_widget)

        preface_widget=QWidget()
        preface_widget.setLayout(layout_preface)

        return preface_widget
    
class catalog(format):
    #返回目录页控件
    def __init__(self):
        super().__init__()

    def catalog_widget(self,context):
        '''CATALOG:
        目录: 小二 黑体 居中 350 250 #段后
        篇: 四号 宋体 居中
        章: 五号 黑体 
        节: 五号 宋体 None None None 200 #左缩进
        条: 五号 宋体 None None None 400 #左缩进'''
        catalog_text=context["CATALOG"]
        layout1 = QHBoxLayout()
        Lb_catalog1 = QLabel("目录")
        catalog1_text=catalog_text['目录'].split(' ')
        Wgt1=self.format_widget(catalog1_text)

        #Wgt1=self.format_widget(current_fontsize='小二',current_font='黑体',current_align='居中',current_before=3.5,current_after=2.5)
        layout1.addWidget(Lb_catalog1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_catalog2 = QLabel("篇")
        catalog2_text=catalog_text['篇'].split(' ')
        Wgt2=self.format_widget(catalog2_text)

        #Wgt2=self.format_widget(current_fontsize='四号',current_font='宋体',current_align='居中')
        layout2.addWidget(Lb_catalog2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_catalog3 = QLabel("章")
        catalog3_text=catalog_text['章'].split(' ')
        Wgt3=self.format_widget(catalog3_text)

        #Wgt3=self.format_widget(current_font='黑体')
        layout3.addWidget(Lb_catalog3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        layout4 = QHBoxLayout()
        Lb_catalog4 = QLabel("节")
        catalog4_text=catalog_text['节'].split(' ')
        Wgt4=self.format_widget(catalog4_text)

        #Wgt4=self.format_widget(current_before=2)
        layout4.addWidget(Lb_catalog4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)

        layout5 = QHBoxLayout()
        Lb_catalog5 = QLabel("条")
        catalog5_text=catalog_text['条'].split(' ')
        Wgt5=self.format_widget(catalog5_text)

        #Wgt5=self.format_widget(current_before=4)
        layout5.addWidget(Lb_catalog5)
        layout5.addWidget(Wgt5)
        layout5_widget=QWidget()
        layout5_widget.setLayout(layout5)

        layout_catalog =QVBoxLayout()
        layout_catalog.addWidget(layout1_widget)
        layout_catalog.addWidget(layout2_widget)
        layout_catalog.addWidget(layout3_widget)
        layout_catalog.addWidget(layout4_widget)
        layout_catalog.addWidget(layout5_widget)

        catalog_widget=QWidget()
        catalog_widget.setLayout(layout_catalog)

        return catalog_widget

class text(format):
    #返回正文页控件
    def __init__(self):
        super().__init__()
        """TEXT:
        篇: 小初 黑体 居中 
        章: 二号 宋体 居中 300 200 
        节: 四号 仿宋 None 100 100
        条: 五号 黑体 """
        
    def text_widget(self,context):
        text_text=context["TEXT"]
        layout1 = QHBoxLayout()
        Lb_text1 = QLabel('篇')
        text1_text=text_text['篇'].split(' ')
        Wgt1=self.format_widget(text1_text)
        #Wgt1=self.format_widget(current_fontsize='小初', current_font='黑体', current_align='居中', )
        layout1.addWidget(Lb_text1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        Lb_text2 = QLabel('章')
        text2_text=text_text['章'].split(' ')
        Wgt2=self.format_widget(text2_text)
        #Wgt2=self.format_widget(current_fontsize='二号',current_align='居中',current_before=3, current_after=2)
        layout2=QHBoxLayout()
        layout2.addWidget(Lb_text2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        Lb_text3 = QLabel('节')
        text3_text=text_text['节'].split(' ')
        Wgt3=self.format_widget(text3_text)

        #Wgt3=self.format_widget(current_fontsize='四号',current_font='仿宋', current_before=1)
        layout3=QHBoxLayout()
        layout3.addWidget(Lb_text3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        Lb_text4 = QLabel('条')
        text4_text=text_text['条'].split(' ')
        Wgt4=self.format_widget(text4_text)

        #Wgt4=self.format_widget(current_font='黑体')
        layout4=QHBoxLayout()
        layout4.addWidget(Lb_text4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)
        """
        款: 五号 宋体 
        正文: 五号 宋体 
        正文首行缩进: 2.0
        思考题: 四号 仿宋 居中 100 100"""
        Lb_text5 = QLabel('款')
        text5_text=text_text['款'].split(' ')
        Wgt5=self.format_widget(text5_text)

        #Wgt5=self.format_widget()
        layout5=QHBoxLayout()
        layout5.addWidget(Lb_text5)
        layout5.addWidget(Wgt5)
        layout5_widget=QWidget()
        layout5_widget.setLayout(layout5)

        Lb_text6 = QLabel('正文')
        layout6=QHBoxLayout()
        layout6.addWidget(Lb_text6)

        Lb_FirstIndent = QLabel('首行缩进')
        sp_FirstIndent=QSpinBox()
        sp_FirstIndent.setEnabled(False)
        #if rightenable==1:
        #    sp_FirstIndent.setEnabled(True)
        sp_FirstIndent.setValue(int(text_text['正文首行缩进']))
        
        layout6.addWidget(Lb_FirstIndent)
        layout6.addWidget(sp_FirstIndent)
        
        text6_text=text_text['正文'].split(' ')
        Wgt6=self.format_widget(text6_text)

        #Wgt6=self.format_widget()
        layout6.addWidget(Wgt6)
        layout6_widget=QWidget()
        layout6_widget.setLayout(layout6)

        Lb_text7 = QLabel('思考题')
        text7_text=text_text['思考题'].split(' ')
        Wgt7=self.format_widget(text7_text)
        #Wgt7=self.format_widget(current_fontsize='四号',current_font='仿宋',current_align="居中", current_before=1)
        layout7=QHBoxLayout()
        layout7.addWidget(Lb_text7)
        layout7.addWidget(Wgt7)
        layout7_widget=QWidget()
        layout7_widget.setLayout(layout7)

        Lb_text8 = QLabel('图表')
        text8_text=text_text["图表"].split(' ')
        Wgt8=self.format_widget(text8_text)
        #Wgt7=self.format_widget(current_fontsize='四号',current_font='仿宋',current_align="居中", current_before=1)
        layout8=QHBoxLayout()
        layout8.addWidget(Lb_text8)
        layout8.addWidget(Wgt8)
        layout8_widget=QWidget()
        layout8_widget.setLayout(layout8)

        layout_text =QVBoxLayout()
        layout_text.addWidget(layout1_widget)
        layout_text.addWidget(layout2_widget)
        layout_text.addWidget(layout3_widget)
        layout_text.addWidget(layout4_widget)
        layout_text.addWidget(layout5_widget)
        layout_text.addWidget(layout6_widget)
        layout_text.addWidget(layout7_widget)
        layout_text.addWidget(layout8_widget)
        
        text_widget=QWidget()
        text_widget.setLayout(layout_text)

        return text_widget

class postscript(format):
    #返回附录页控件 
    def __init__(self):
        super().__init__()

    def postscript_widget(self,context):
        '''POSTSCRIPT:
        页码: 五号 
        附录: 二号 宋体 居中 300 200 
        标题下附录: 四号 仿宋 居中 100 100
        '''
        postscript_text=context["POSTSCRIPT"]
        layout1 = QHBoxLayout()
        Lb_postscript1 = QLabel("页码")
        postscript1_text=postscript_text['页码'].split(' ')
        Wgt1=self.format_widget(postscript1_text)

        #Wgt1=self.format_widget()
        layout1.addWidget(Lb_postscript1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_postscript2 = QLabel("附录")
        postscript2_text=postscript_text['附录'].split(' ')
        Wgt2=self.format_widget(postscript2_text)

        #Wgt2=self.format_widget(current_fontsize='二号',current_align='居中',current_before=3,current_after=2)
        layout2.addWidget(Lb_postscript2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_postscript3 = QLabel("标题下附录")
        postscript3_text=postscript_text['标题下附录'].split(' ')
        Wgt3=self.format_widget(postscript3_text)

        #Wgt3=self.format_widget(current_fontsize='四号',current_font='仿宋',current_align='居中',current_before=1,current_after=1)
        layout3.addWidget(Lb_postscript3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        

        layout_postscript =QVBoxLayout()
        layout_postscript.addWidget(layout1_widget)
        layout_postscript.addWidget(layout2_widget)
        layout_postscript.addWidget(layout3_widget)
        

        postscript_widget=QWidget()
        postscript_widget.setLayout(layout_postscript)

        return postscript_widget

class literature(format):
    #返回参考文献页控件
    def __init__(self):
        super().__init__()
    
    def literature_widget(self,context):
        """参考文献: 五号 黑体 居中 200 100 
        文献: 六号 宋体"""
        literature_text=context["LITERATURE"]
        layout1 = QHBoxLayout()
        Lb_literature1 = QLabel("参考文献")
        literature1_text=literature_text['参考文献'].split(' ')
        Wgt1=self.format_widget(literature1_text)
        #Wgt1=self.format_widget(current_font='黑体',current_align='居中',current_before=2,current_after=1)
        layout1.addWidget(Lb_literature1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_literature2 = QLabel("文献")
        literature2_text=literature_text['文献'].split(' ')
        Wgt2=self.format_widget(literature2_text)

        #Wgt2=self.format_widget(current_fontsize='六号')
        layout2.addWidget(Lb_literature2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout_literature =QVBoxLayout()
        layout_literature.addWidget(layout1_widget)
        layout_literature.addWidget(layout2_widget)

        literature_widget=QWidget()
        literature_widget.setLayout(layout_literature)
        return literature_widget
      
class check_box(QWidget):
    #返回其他项选择页控件
    def __init__(self):
        super().__init__()
    def check_widget(self):
        
        layout=QGridLayout()
        #book_title = QCheckBox("检测书名，主编，日期一致性")
        #book_title.setChecked(True)
        #layout.addWidget(book_title,0,0)

        title_continuous = QCheckBox("检测标题连续性")
        title_continuous.setChecked(True)
        pic_continuous = QCheckBox("检测图片标题连续性")
        pic_continuous.setChecked(True)
        #pagenum_continuous = QCheckBox("检测页码标题连续性")
        #pagenum_continuous.setChecked(True)
        layout.addWidget(title_continuous,1,0,Qt.AlignLeft)
        layout.addWidget(pic_continuous,1,1,Qt.AlignLeft)
        #layout.addWidget(pagenum_continuous,3,2)

        #formula_format = QCheckBox("检测公式符号格式正确性")
        #formula_format.setChecked(True)
        #formula_continuous =  QCheckBox("检测公式顺序连续性  ")
        #formula_continuous.setChecked(True)
        #layout.addWidget(formula_format,2,0,Qt.AlignLeft)
        #layout.addWidget(formula_continuous,2,0,Qt.AlignLeft)

        table_title = QCheckBox("检测表格标题       ")
        table_title.setChecked(True)
        measurement = QCheckBox("检测度量衡规范       ")
        measurement.setChecked(True)
        layout.addWidget(table_title,2,0,Qt.AlignLeft)
        layout.addWidget(measurement,2,1,Qt.AlignLeft)

        appendix_continuous = QCheckBox("检测附录编号顺序连续性")
        appendix_continuous.setChecked(True)
        references_continuous = QCheckBox("检测参考文献顺序连续性")
        references_continuous.setChecked(True)
        layout.addWidget(appendix_continuous,3,0,Qt.AlignLeft)
        layout.addWidget(references_continuous,3,1,Qt.AlignLeft)

        layout_widget=QWidget()
        layout_widget.setLayout(layout)
        return layout_widget

class Tab(QTabWidget):
    #返回Tab类控件
    def __init__(self,file_path):
        super().__init__()
        f = open(file_path,'r',encoding='utf-8')
        context = yaml.load(f,Loader=yaml.FullLoader)
 
        self.setGeometry(300, 100, 1000,750) # 
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()
        self.addTab(self.tab1,"Tab 1")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Tab 3")
        self.addTab(self.tab4,"Tab 4")
        self.addTab(self.tab5,"Tab 5")
        self.addTab(self.tab6,"Tab 6")
        self.addTab(self.tab7,"Tab 7")
        self.addTab(self.tab8,"Tab 8")
        self.addTab(self.tab9,"Tab 9")
        self.tab1UI(context)
        self.tab2UI(context)
        self.tab3UI(context)
        self.tab4UI(context)
        self.tab5UI(context)
        self.tab6UI(context)
        self.tab7UI(context)
        self.tab8UI(context)
        self.tab9UI()
        self.setWindowTitle("配置文件")
        #self.context=context
        
    def tab1UI(self,context):
        layout = QGridLayout()
        cover1=cover()
        layout.addWidget(cover1.cover_widget(context),0,0)
        
        self.setTabText(0,"封面")
        self.tab1.setLayout(layout)

        
    def tab2UI(self,context):
        layout = QGridLayout()
        abstract1 = abstract()
        layout.addWidget(abstract1.abstract_widget(context),0,0)
        self.setTabText(1,"内容提要")
        self.tab2.setLayout(layout)
        
    def tab3UI(self,context):
        layout = QGridLayout()
        author1 = author()
        layout.addWidget(author1.author_widget(context),0,0)
        
        self.setTabText(2,"作者")
        self.tab3.setLayout(layout)

    def tab4UI(self,context):
        layout = QGridLayout()
        preface1 = preface()
        layout.addWidget(preface1.preface_widget(context),0,0)
        
        self.setTabText(3,"前言")
        self.tab4.setLayout(layout)

    def tab5UI(self,context):
        layout = QGridLayout()
        catalog1 = catalog()
        layout.addWidget(catalog1.catalog_widget(context))
        
        self.setTabText(4,"目录")
        self.tab5.setLayout(layout)
    
    def tab6UI(self,context):
        layout = QGridLayout()
        text1 = text()
        layout.addWidget(text1.text_widget(context),0,0)
        
        self.setTabText(5,"正文")
        self.tab6.setLayout(layout)

    def tab7UI(self,context):
        layout = QGridLayout()
        postscript1 = postscript()
        layout.addWidget(postscript1.postscript_widget(context),0,0)
        
        self.setTabText(6,"附录")
        self.tab7.setLayout(layout)

    def tab8UI(self,context):
        layout = QGridLayout()
        literature1 = literature()
        layout.addWidget(literature1.literature_widget(context),0,0)
        
        self.setTabText(7,"参考文献")
        self.tab8.setLayout(layout)

    def tab9UI(self):
        layout = QGridLayout()
        check1 = check_box()
        layout.addWidget(check1.check_widget(),0,0)
        self.setTabText(8,"其它项选择")
        self.tab9.setLayout(layout)

'''
class TabWidget(QWidget):
    def __init__(self,file_path):
        super().__init__()
        QApplication.setStyle('Windows')
        f = open(file_path,'r',encoding='utf-8')
        context = yaml.load(f,Loader=yaml.FullLoader)
        demo = Tab(context)
        #sys.exit(app.exec_()) 
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_path=r'D:\Project\pyqt\main\v1-master\cfg1.yml'
    tabdemo=Tab(file_path)
    tabdemo.show()
    sys.exit(app.exec_()) 

"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_path='D:\Project\pyqt\配置三.yml'
    f = open(file_path,'r',encoding='utf-8')
    context = yaml.load(f,Loader=yaml.FullLoader)
    cover_text = context["COVER"]
    abstract_text = context["ABSTRACT"]
    author_text=context["AUTHOR"]
    preface_text=context["PREFACE"]
    catalog_text=context["CATALOG"]
    text_text=context["TEXT"]
    postscript_text=context["POSTSCRIPT"]
    literature_text=context["LITERATURE"]
    demo = Tab()
    demo.show()
    sys.exit(app.exec_()) 
"""
"""
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = format()
    widget=win.format_widget(current_fontsize='小三',current_align='居中',current_after=0.5)     
    widget.show()  
    sys.exit(app.exec_()) 
""" 
"""
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = catalog()
    widget=win.catalog_widget()
    widget.show()
    sys.exit(app.exec_()) 
"""
