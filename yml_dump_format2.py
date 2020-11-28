import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from settings import *
import os
import yaml


class format_new(QWidget):
    def __init__(self):
        super().__init__()

    def format_new_widget(self,alignenable=1,beforeenable=1,afterenable=1,leftenable=1,rightenable=1,save=0):
        '''传入参数依次为:当前字号(需为字号list中string)，当前字体(需为字体list中string)，当前对齐方式(需为对齐方式list中string)，
        当前段前距，当前段后距,左缩进当前值，右缩进当前值 对齐方式启动(1为启动,下同)，段前距启动，段后距启动，左缩进启动，右缩进启动，
        默认值为 宋体，五号，左对齐，所有控件关闭，数值为0，   所有参数需通过关键字参数传入'''
        layout_format_new=QHBoxLayout()

        self.cb_fontsize= QComboBox()
        self.cb_fontsize.addItems(["五号","小五","四号","小四","三号","小三","二号","小二","小初"])
        self.cb_fonts= QComboBox()
        self.cb_fonts.addItems(["宋体","楷体","黑体", "微软雅黑", "仿宋","方正北魏楷体","方正小标宋简","方正大标宋简"])
        layout_format_new.addWidget(self.cb_fontsize)
        layout_format_new.addWidget(self.cb_fonts)


        Lb_alignment = QLabel('对齐方式')
        self.cb_alignment= QComboBox()
        self.cb_alignment.addItems(["左对齐","居中","右对齐","两端对齐","分散对齐"])
        layout_format_new.addWidget(Lb_alignment)
        layout_format_new.addWidget(self.cb_alignment)
        self.cb_alignment.setEnabled(False)
        if alignenable==1:
            self.cb_alignment.setEnabled(True)

        Lb_space_before = QLabel('段前距/行')
        self.sp_space_before=QDoubleSpinBox()
        self.sp_space_before.setDecimals(1)
        layout_format_new.addWidget(Lb_space_before)
        layout_format_new.addWidget(self.sp_space_before)
        self.sp_space_before.setEnabled(False)
        if beforeenable==1:
            self.sp_space_before.setEnabled(True)

        Lb_space_after = QLabel('段后距/行')
        self.sp_space_after=QDoubleSpinBox()
        self.sp_space_after.setDecimals(1)
        layout_format_new.addWidget(Lb_space_after)
        layout_format_new.addWidget(self.sp_space_after)
        self.sp_space_after.setEnabled(False)
        if afterenable==1:
            self.sp_space_after.setEnabled(True)


        Lb_indent_left= QLabel('左缩进/字符')
        self.sp_indent_left=QSpinBox()
        layout_format_new.addWidget(Lb_indent_left)
        layout_format_new.addWidget(self.sp_indent_left)
        self.sp_indent_left.setEnabled(False)
        if leftenable==1:
            self.sp_indent_left.setEnabled(True)


        Lb_indent_right= QLabel('右缩进/字符')
        self.sp_indent_right=QSpinBox()
        layout_format_new.addWidget(Lb_indent_right)
        layout_format_new.addWidget(self.sp_indent_right)
        self.sp_indent_right.setEnabled(False)
        if rightenable==1:
            self.sp_indent_right.setEnabled(True)
        

        layout_format_new_widget=QWidget()
        layout_format_new_widget.setLayout(layout_format_new)
        return layout_format_new_widget #返回横向布局的控件及保存值的列表
    
    def save(self,save=0):
        if save==1:
            save_list=[self.cb_fontsize.currentText(),self.cb_fonts.currentText(),self.cb_alignment.currentIndex(),
            self.sp_space_before.value(),self.sp_space_after.value(),self.sp_indent_left.value(),self.sp_indent_right.value()]
            savelist =" ".join(str(i) for i in save_list)
        return savelist

class cover_new(format_new):
    #返回封面页的控件
    def __init__(self):
        super().__init__()
    
    def cover_widget(self,save=0):
        
        layout0 = QHBoxLayout()
        Lb_name = QLabel('配置文件名称')
        self.Ed_name = QLineEdit()
        layout0.addWidget(Lb_name)
        layout0.addWidget(self.Ed_name)
        layout0_widget=QWidget()
        layout0_widget.setLayout(layout0)

        layout1 = QHBoxLayout()
        Lb_cover1 = QLabel('内部发行号')
        self.cover1=format_new()
        Wgt1=self.cover1.format_new_widget()
        layout1.addWidget(Lb_cover1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        Lb_cover2 = QLabel('系      列')
        self.cover2=format_new()
        Wgt2=self.cover2.format_new_widget()
        layout2=QHBoxLayout()
        layout2.addWidget(Lb_cover2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        Lb_cover3 = QLabel('机      型')
        self.cover3=format_new()
        Wgt3=self.cover3.format_new_widget()
        layout3=QHBoxLayout()
        layout3.addWidget(Lb_cover3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        Lb_cover4 = QLabel('书      名')
        self.cover4=format_new()
        Wgt4=self.cover4.format_new_widget()
        layout4=QHBoxLayout()
        layout4.addWidget(Lb_cover4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)
        
        Lb_cover5 = QLabel('分      册')
        self.cover5=format_new()
        Wgt5=self.cover5.format_new_widget()
        layout5=QHBoxLayout()
        layout5.addWidget(Lb_cover5)
        layout5.addWidget(Wgt5)
        layout5_widget=QWidget()
        layout5_widget.setLayout(layout5)

        Lb_cover6 = QLabel('适用训练类别')
        self.cover6=format_new()
        Wgt6=self.cover6.format_new_widget()
        layout6=QHBoxLayout()
        layout6.addWidget(Lb_cover6)
        layout6.addWidget(Wgt6)
        layout6_widget=QWidget()
        layout6_widget.setLayout(layout6)

        Lb_cover7 = QLabel('主      编')
        self.cover7=format_new()
        Wgt7=self.cover7.format_new_widget()
        layout7=QHBoxLayout()
        layout7.addWidget(Lb_cover7)
        layout7.addWidget(Wgt7)
        layout7_widget=QWidget()
        layout7_widget.setLayout(layout7)

        Lb_cover8 = QLabel('出  版  社')
        self.cover8=format_new()
        Wgt8=self.cover8.format_new_widget()
        layout8=QHBoxLayout()
        layout8.addWidget(Lb_cover8)
        layout8.addWidget(Wgt8)
        layout8_widget=QWidget()
        layout8_widget.setLayout(layout8)

        Lb_cover9 = QLabel('版      次')
        self.cover9=format_new()
        Wgt9=self.cover9.format_new_widget()
        layout9=QHBoxLayout()
        layout9.addWidget(Lb_cover9)
        layout9.addWidget(Wgt9)
        layout9_widget=QWidget()
        layout9_widget.setLayout(layout9)

        layout_cover =QVBoxLayout()
        layout_cover.addWidget(layout0_widget)
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

    def save(self,save=0):
        if save==1:
            name=self.Ed_name.text()
            savelist1=self.cover1.save(save=1)
            savelist2=self.cover2.save(save=1)
            savelist3=self.cover3.save(save=1)
            savelist4=self.cover4.save(save=1)
            savelist5=self.cover5.save(save=1)
            savelist6=self.cover6.save(save=1)
            savelist7=self.cover7.save(save=1)
            savelist8=self.cover8.save(save=1)
            savelist9=self.cover9.save(save=1)

            cover_savedict={"内部发行号":savelist1,"系列":savelist2,"机型":savelist3,"书名":savelist4,"分册":savelist5,
                    "适用训练类别":savelist6,"主编":savelist7,"出版社":savelist8,"版次":savelist9}
            return cover_savedict,name

class abstract_new(format_new):
    #返回内容提要页控件
    def __init__(self):
        super().__init__()
    
    def abstract_widget(self):

        layout1 = QHBoxLayout()
        Lb_abstract1 = QLabel("内容提要")
        self.abstract1=format_new()
        Wgt1=self.abstract1.format_new_widget()
        layout1.addWidget(Lb_abstract1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        layout2 = QHBoxLayout()
        Lb_abstract2 = QLabel("正     文")
        self.abstract2=format_new()
        Wgt2=self.abstract2.format_new_widget()
        layout2.addWidget(Lb_abstract2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_abstract3 = QLabel("内部发行")
        self.abstract3=format_new()
        Wgt3=self.abstract3.format_new_widget()
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

    def save(self,save=0):
        if save==1:
            savelist1=self.abstract1.save(save=1)
            savelist2=self.abstract2.save(save=1)
            savelist3=self.abstract3.save(save=1)
            
            abstract_savedict={"内容提要":savelist1,"正文":savelist2,"内部发行":savelist3}
            return abstract_savedict

class author_new(format_new):
    #返回作者页控件
    def __init__(self):
        super().__init__()
    
    def author_widget(self):
        '''AUTHOR:
        编审组: 小二 黑体 居中
        组长标题: 三号 黑体
        组员: 三号 楷体'''

        layout1 = QHBoxLayout()
        Lb_author1 = QLabel("编审组")
        self.author1=format_new()
        Wgt1=self.author1.format_new_widget()
        layout1.addWidget(Lb_author1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        layout2 = QHBoxLayout()
        Lb_author2 = QLabel("组长标题")
        self.author2=format_new()
        Wgt2=self.author2.format_new_widget()
        layout2.addWidget(Lb_author2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_author3 = QLabel("组员")
        self.author3=format_new()
        Wgt3=self.author3.format_new_widget()
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

    def save(self,save=0):
        if save==1:
            savelist1=self.author1.save(save=1)
            savelist2=self.author2.save(save=1)
            savelist3=self.author3.save(save=1)
            
            author_savedict={"编审组":savelist1,"组长标题":savelist2,"组员":savelist3}
            return author_savedict

class preface_new(format_new):
    #返回前言页孔家
    def __init__(self):
        super().__init__()
    
    def preface_widget(self):

        layout1 = QHBoxLayout()
        Lb_preface1 = QLabel("前言")
        self.preface1=format_new()
        Wgt1=self.preface1.format_new_widget()
        layout1.addWidget(Lb_preface1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_preface2 = QLabel("正文")
        self.preface2=format_new()
        Wgt2=self.preface2.format_new_widget()
        layout2.addWidget(Lb_preface2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_preface3 = QLabel("编者")
        self.preface3=format_new()
        Wgt3=self.preface3.format_new_widget()
        layout3.addWidget(Lb_preface3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        layout4 = QHBoxLayout()
        Lb_preface4 = QLabel("时间")
        self.preface4=format_new()
        Wgt4=self.preface4.format_new_widget()
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

    def save(self,save=0):
        if save==1:
            savelist1=self.preface1.save(save=1)
            savelist2=self.preface2.save(save=1)
            savelist3=self.preface3.save(save=1)
            savelist4=self.preface4.save(save=1)

            preface_savedict={"前言":savelist1,"正文":savelist2,"编者":savelist3,"时间":savelist4}
            return preface_savedict
    
class catalog_new(format_new):
    #返回目录页控件
    def __init__(self):
        super().__init__()

    def catalog_widget(self):
        layout1 = QHBoxLayout()
        Lb_catalog1 = QLabel("目录")
        self.catalog1=format_new()
        Wgt1=self.catalog1.format_new_widget()
        layout1.addWidget(Lb_catalog1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_catalog2 = QLabel("篇")
        self.catalog2=format_new()
        Wgt2=self.catalog2.format_new_widget()
        layout2.addWidget(Lb_catalog2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_catalog3 = QLabel("章")
        self.catalog3=format_new()
        Wgt3=self.catalog3.format_new_widget()
        layout3.addWidget(Lb_catalog3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        layout4 = QHBoxLayout()
        Lb_catalog4 = QLabel("节")
        self.catalog4=format_new()
        Wgt4=self.catalog4.format_new_widget()
        layout4.addWidget(Lb_catalog4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)

        layout5 = QHBoxLayout()
        Lb_catalog5 = QLabel("条")
        self.catalog5=format_new()
        Wgt5=self.catalog5.format_new_widget()
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

    def save(self,save=0):
        if save==1:
            savelist1=self.catalog1.save(save=1)
            savelist2=self.catalog2.save(save=1)
            savelist3=self.catalog3.save(save=1)
            savelist4=self.catalog4.save(save=1)
            savelist5=self.catalog5.save(save=1)
            
            catalog_savedict={"目录":savelist1,"篇":savelist2,"章":savelist3,"节":savelist4,"条":savelist5}
            return catalog_savedict

class text_new(format_new):
    #返回正文页控件
    def __init__(self):
        super().__init__()
        
    def text_widget(self,rightenable):

        layout1 = QHBoxLayout()
        Lb_text1 = QLabel('篇')
        self.text1=format_new()
        Wgt1=self.text1.format_new_widget()
        layout1.addWidget(Lb_text1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)
        
        Lb_text2 = QLabel('章')
        self.text2=format_new()
        Wgt2=self.text2.format_new_widget()
        layout2=QHBoxLayout()
        layout2.addWidget(Lb_text2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        Lb_text3 = QLabel('节')
        self.text3=format_new()
        Wgt3=self.text3.format_new_widget()
        layout3=QHBoxLayout()
        layout3.addWidget(Lb_text3)
        layout3.addWidget(Wgt3)
        layout3_widget=QWidget()
        layout3_widget.setLayout(layout3)

        Lb_text4 = QLabel('条')
        self.text4=format_new()
        Wgt4=self.text4.format_new_widget()
        layout4=QHBoxLayout()
        layout4.addWidget(Lb_text4)
        layout4.addWidget(Wgt4)
        layout4_widget=QWidget()
        layout4_widget.setLayout(layout4)

        Lb_text5 = QLabel('款')
        self.text5=format_new()
        Wgt5=self.text5.format_new_widget()
        layout5=QHBoxLayout()
        layout5.addWidget(Lb_text5)
        layout5.addWidget(Wgt5)
        layout5_widget=QWidget()
        layout5_widget.setLayout(layout5)

        Lb_text6 = QLabel('正文')
        layout6=QHBoxLayout()
        layout6.addWidget(Lb_text6)

        Lb_FirstIndent = QLabel('首行缩进')
        self.sp_FirstIndent=QSpinBox()
        self.sp_FirstIndent.setEnabled(False)
        if rightenable==1:
            self.sp_FirstIndent.setEnabled(True)
        layout6.addWidget(Lb_FirstIndent)
        layout6.addWidget(self.sp_FirstIndent)

        self.text6=format_new()
        Wgt6=self.text6.format_new_widget()
        layout6.addWidget(Wgt6)
        layout6_widget=QWidget()
        layout6_widget.setLayout(layout6)

        Lb_text7 = QLabel('思考题')
        self.text7=format_new()
        Wgt7=self.text7.format_new_widget()
        layout7=QHBoxLayout()
        layout7.addWidget(Lb_text7)
        layout7.addWidget(Wgt7)
        layout7_widget=QWidget()
        layout7_widget.setLayout(layout7)

        Lb_text8 = QLabel('图表')
        self.text8=format_new()
        Wgt8=self.text8.format_new_widget()
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

    def save(self,save=0):
        if save==1:
            savelist1=self.text1.save(save=1)
            savelist2=self.text2.save(save=1)
            savelist3=self.text3.save(save=1)
            savelist4=self.text4.save(save=1)
            findent=self.sp_FirstIndent.value()
            savelist5=self.text5.save(save=1)
            savelist6=self.text6.save(save=1)
            savelist7=self.text7.save(save=1)
            savelist8=self.text8.save(save=1)
            text_savedict={"篇":savelist1,"章":savelist2,"节":savelist3,"条":savelist4,"款":savelist5,"正文首行缩进":findent,"正文":savelist6,"思考题":savelist7,"图表":savelist8}
            return text_savedict

class postscript_new(format_new):
    #返回附录页控件 
    def __init__(self):
        super().__init__()

    def postscript_widget(self):

        layout1 = QHBoxLayout()
        Lb_postscript1 = QLabel("页码")
        self.postscript1=format_new()
        Wgt1=self.postscript1.format_new_widget()
        layout1.addWidget(Lb_postscript1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_postscript2 = QLabel("附录")
        self.postscript2=format_new()
        Wgt2=self.postscript2.format_new_widget()
        layout2.addWidget(Lb_postscript2)
        layout2.addWidget(Wgt2)
        layout2_widget=QWidget()
        layout2_widget.setLayout(layout2)

        layout3 = QHBoxLayout()
        Lb_postscript3 = QLabel("标题下附录")
        self.postscript3=format_new()
        Wgt3=self.postscript3.format_new_widget()
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

    def save(self,save=0):
        if save==1:
            savelist1=self.postscript1.save(save=1)
            savelist2=self.postscript2.save(save=1)
            savelist3=self.postscript3.save(save=1)
            postscript_savedict={"页码":savelist1,"附录":savelist2,"标题下附录":savelist3}
            return postscript_savedict

class literature_new(format_new):
    #返回参考文献页控件
    def __init__(self):
        super().__init__()
    
    def literature_widget(self):
   
        layout1 = QHBoxLayout()
        Lb_literature1 = QLabel("参考文献")
        self.literature1=format_new()
        Wgt1=self.literature1.format_new_widget()
        layout1.addWidget(Lb_literature1)
        layout1.addWidget(Wgt1)
        layout1_widget=QWidget()
        layout1_widget.setLayout(layout1)

        layout2 = QHBoxLayout()
        Lb_literature2 = QLabel("文献")
        self.literature2=format_new()
        Wgt2=self.literature2.format_new_widget()
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
    
    def save(self,save=0):
        if save==1:
            savelist1=self.literature1.save(save=1)
            savelist2=self.literature2.save(save=1)
            literature_savedict={"参考文献":savelist1,"文献":savelist2}
            return literature_savedict

class check_box_new(QWidget):
    #返回其他项选择页控件
    def __init__(self):
        super().__init__()

    def check_widget(self):
        layout=QGridLayout()
        self.book_title = QCheckBox("检测书名，主编，日期一致性")
        self.book_title.setChecked(True)
        layout.addWidget(self.book_title,0,0)

        self.title_continuous = QCheckBox("检测标题连续性    ")
        self.title_continuous.setChecked(True)
        self.pic_continuous = QCheckBox("检测图片标题连续性  ")
        self.pic_continuous.setChecked(True)
        #pagenum_continuous = QCheckBox("检测页码标题连续性")
        #pagenum_continuous.setChecked(True)
        layout.addWidget(self.title_continuous,1,0,Qt.AlignLeft)
        layout.addWidget(self.pic_continuous,1,1,Qt.AlignLeft)
        #layout.addWidget(pagenum_continuous,3,2)

        self.formula_format = QCheckBox("检测公式符号格式正确性")
        self.formula_format.setChecked(True)
        self.formula_continuous =  QCheckBox("检测公式顺序连续性  ")
        self.formula_continuous.setChecked(True)
        layout.addWidget(self.formula_format,2,0,Qt.AlignLeft)
        layout.addWidget(self.formula_continuous,2,1,Qt.AlignLeft)

        self.table_title = QCheckBox("检测表格标题       ")
        self.table_title.setChecked(True)
        self.measurement = QCheckBox("检测度量衡规范       ")
        self.measurement.setChecked(True)
        layout.addWidget(self.table_title,3,0,Qt.AlignLeft)
        layout.addWidget(self.measurement,3,1,Qt.AlignLeft)

        self.appendix_continuous = QCheckBox("检测附录编号顺序连续性")
        self.appendix_continuous.setChecked(True)
        self.references_continuous = QCheckBox("检测参考文献顺序连续性")
        self.references_continuous.setChecked(True)
        layout.addWidget(self.appendix_continuous,4,0,Qt.AlignLeft)
        layout.addWidget(self.references_continuous,4,1,Qt.AlignLeft)

        layout_widget=QWidget()
        layout_widget.setLayout(layout)
        return layout_widget
    
    def save(self,save=0):
        if save==1:
            check1=self.book_title.isChecked()
            check2=self.title_continuous.isChecked()
            check3=self.pic_continuous.isChecked()
            check4=self.formula_format.isChecked()
            check5=self.formula_continuous.isChecked()
            check6=self.table_title.isChecked()
            check7=self.measurement.isChecked()
            check8=self.appendix_continuous.isChecked()
            check9=self.references_continuous.isChecked()

            check_savedict={"检测书名，主编，日期一致性":check1,"检测标题连续性":check2,"检测图片标题连续性":check3,"检测公式符号格式正确性":check4,
            "检测公式顺序连续性":check5,"检测表格标题":check6,"检测度量衡规范":check7,"检测附录编号顺序连续性":check8,"检测参考文献顺序连续性":check9}

            return check_savedict

class Tab_new(QTabWidget,cover_new,abstract_new,author_new,preface_new,catalog_new,text_new,postscript_new,literature_new,check_box_new):#,settings_options
    #返回Tab类控件
    def __init__(self):#
        super().__init__()   
        self.setGeometry(300, 100, 1000,750) 
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
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()
        self.tab7UI()
        self.tab8UI()
        self.tab9UI()
        self.setWindowTitle("配置文件")

        
    def tab1UI(self):
        layout_tab1 = QGridLayout()
        #cover1=cover()
        layout_tab1.addWidget(cover_new.cover_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout_tab1.addWidget(Button,1,0,Qt.AlignRight)  #,Qt.AllButtons
        self.setTabText(0,"封面")
        self.tab1.setLayout(layout_tab1)

    def tab2UI(self):
        layout_tab2 = QGridLayout()
        #abstract1 = abstract()
        layout_tab2.addWidget(abstract_new.abstract_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout_tab2.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(1,"内容提要")
        self.tab2.setLayout(layout_tab2)
        
    def tab3UI(self):
        layout_tab3 = QGridLayout()
        #author1 = author()
        layout_tab3.addWidget(author_new.author_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout_tab3.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(2,"作者")
        self.tab3.setLayout(layout_tab3)

    def tab4UI(self):
        layout = QGridLayout()
        #preface1 = preface()
        layout.addWidget(preface_new.preface_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(3,"前言")
        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QGridLayout()
        #catalog1 = catalog()
        layout.addWidget(catalog_new.catalog_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(4,"目录")
        self.tab5.setLayout(layout)
    
    def tab6UI(self):
        layout = QGridLayout()
        #text1 = text()
        layout.addWidget(text_new.text_widget(self,rightenable=1),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(5,"正文")
        self.tab6.setLayout(layout)

    def tab7UI(self):
        layout = QGridLayout()
        #postscript1 = postscript()
        layout.addWidget(postscript_new.postscript_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(6,"附录")
        self.tab7.setLayout(layout)

    def tab8UI(self):
        layout = QGridLayout()
        #literature1 = literature()
        layout.addWidget(literature_new.literature_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(7,"参考文献")
        self.tab8.setLayout(layout)

    def tab9UI(self):
        layout = QGridLayout()
        #check1 = check_box()
        layout.addWidget(check_box_new.check_widget(self),0,0)
        Button=QPushButton('保  存')
        Button.setFixedSize(80,50)
        Button.clicked.connect(self.save)
        layout.addWidget(Button,1,0,Qt.AlignRight)
        self.setTabText(8,"其它项选择")
        self.tab9.setLayout(layout)
    
    '''def save(self,file_path):
        save=1
        standard={"NAME":cover_new.save(self,save=1)[1],"COVER":cover_new.save(self,save=1)[0],"ABSTRACT":abstract_new.save(self,save=1),"AUTHOR":author_new.save(self,save=1),"PREFACE":preface_new.save(self,save=1),
        "CATALOG":catalog_new.save(self,save=1),"TEXT":text_new.save(self,save=1),"POSTSCRIPT":postscript_new.save(self,save=1),"LITERATURE":literature_new.save(self,save=1),"CHECK":check_box_new.save(self,save=1)}
        #print(standard)
        f = open(self.file_path, "w", encoding="utf-8")
        yaml.dump(standard, f,  allow_unicode=True)
        f.close()
        # self.files = os.listdir(self.path)
        # self.files_yml = [i for i in self.files if i.endswith('.yml')]
        # self.cb_standard.clear()
        # self.file_name()
        # standard_list=self.file_name().values()
        #standard_list.addItems(self.file_name().values())
        return standard#,standard_list '''
""" 
def yml_create(name):
    desktop_path = self.path+'\'  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.yml'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    return full_path  """

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    f_new_path=yml_create('cfg2')
    win = Tab_new(f_new_path)
    win.show()
    sys.exit(app.exec_()) 





"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_path='D:\Project\pyqt\standard1.yml'
    
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_()) 
"""
"""
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = format_new()
    widget=win.format_new_widget(current_fontsize='小三',current_align='居中',current_after=0.5)     
    widget.show()  
    sys.exit(app.exec_()) 
""" 

