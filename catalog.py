import os
import re
from io import open
from string import digits
from docx import Document
from docx.shared import Cm, Pt,Emu
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn


path =r'D:\Project\Word_xml_check\目录.docx'
doc = Document(path)
para=doc.paragraphs
#print(para[2].text)

Node=[]
para_Node=[]
for child in doc.element.body.iter():
    Node.append(child)

for i in range(len(Node)):
    if Node[i].tag.endswith('}p'):
        para_Node.append(i)
#print(para_Node)
text_list=[]
for i in range(len(para_Node)):
    text=''
    for j in range(para_Node[i-1],para_Node[i]):
        if Node[j].tag.endswith('}r'):
            text=text+Node[j].text
    text_list.append(text)
text_list.pop(0)

def get_title(para_text,mainbody_index):
    '''去掉标点及空格干扰'''
    r=' '
    for i in range(len(para_text)):
        para_text[i]=re.sub(r,'',para_text[i])
    b='\t'
    for i in range(len(para_text)):
        para_text[i]=re.sub(b,'',para_text[i])
    title_index=[]
    title0_index=[]
    title1_index=[]
    title2_index=[]
    title3_index=[]
    '''正则式筛选标题'''
    #print(para_text)
    for i in range(mainbody_index,len(para_text)):
        if re.match(r'^目录', para_text[i]):
            title_index.append(i)
        elif re.match(r'^\w{1}?篇', para_text[i]):
            title0_index.append(i)
        elif re.match(r'^第\w{1,2}?章', para_text[i]):
            title1_index.append(i)
        elif re.match(r'^\d{1}?.\d{1}?\w{0,10}$', para_text[i]):
            title2_index.append(i)
        elif re.match(r'^\d{1}?.\d{1}?.\d{1}?\w{0,15}$', para_text[i]):
            title3_index.append(i)
        elif re.match(r'附录\w{1}$', para_text[i]):
            title1_index.append(i)
        elif re.match(r'参考文献\w{1,5}$', para_text[i]):
            title1_index.append(i)
        elif re.match(r'附录\w{1,10}$', para_text[i]):
            title2_index.append(i)
        elif re.match(r'小结\w{1,5}$', para_text[i]):
            title2_index.append(i)
        elif re.match(r'复习思考题\w{1,5}$', para_text[i]):
            title2_index.append(i)
        else: continue
    return [title_index,title0_index,title1_index,title2_index, title3_index]

titleindex=get_title(text_list,0)
#print(len(titleindex))

#print(para_Node[title1_index[0]])
pt2charnum={5:'八号',5.5:'七号',6.5:'小六',7.5:'六号',9:'小五',10.5:'五号',12:'小四',14:'四号',
        15:'小三',16:'三号',18:'小二',22:'二号',24:'小一',26:'一号',36:'小初',42:'初号'}
for level in range(len(titleindex)):
    for x in range(len(titleindex[level])):
        format=[]
        font=[]
        font_sz=10.5
        jc=0
        beforeLines=0
        afterLines=0
        ind_left=0
        ind_right=0
        for i in range(para_Node[titleindex[level][x]],para_Node[titleindex[level][x]+1]):
            if Node[i].tag.endswith('}r'): 
                for j in range(i,para_Node[titleindex[level][x]+1]):
                    if Node[j].tag.endswith('}rFonts'):
                        #if hasattr(Node[j],'ascii'):
                        if Node[j].ascii!=None:
                            font.append(Node[j].ascii)#字体
                            #elif hasattr(Node[j],'eastAsia'):
                        elif Node[j].eastAsia!=None:
                            font.append(Node[j].eastAsia)
                    if Node[j].tag.endswith('}sz'):
                        font_sz=Node[j].val/6350/2#字号
            if Node[i].tag.endswith('}jc'):
                jc=Node[i].val#对齐方式
            if Node[i].tag.endswith('}spacing'):
                beforeLines=Node[i].beforeLines/63500#段前距
                afterLines=Node[i].afterLines/63500#段后距
            if Node[i].tag.endswith('}ind'):
                if hasattr(Node[i],'left'):
                    if Node[i].left!=None:
                        ind_left=Node[i].left/6350/21#左缩进
                    #else:print('左缩进为0')
                if hasattr(Node[i],'right'):
                    if  Node[i].right!=None:
                        ind_right=Node[i].right/210#右缩进
                    #else:print('右缩进为0')
        font_sz_char=pt2charnum[font_sz]
        font=list(set(font))
        format=[level,text_list[titleindex[level][x]],font,font_sz,jc,beforeLines,afterLines,ind_left,ind_right]
        print(format)
    





'''
#核对目录属性
for i in range(para_Node[title_index[0]],para_Node[title_index[0]+1]):
    #print(i)
    if Node[i].tag.endswith('}r'): 
        #print(i)
        for j in range(i,para_Node[title0_index[0]]):
            if Node[j].tag.endswith('}rFonts'):
                if hasattr(Node[j],'ascii'):
                    print(Node[j].ascii)#字体
                elif hasattr(Node[j],'eastAsia'):
                    print(Node[j].eastAsia)
            if Node[j].tag.endswith('}sz'):
                print(Node[j].val/6350)#字号
    if Node[i].tag.endswith('}jc'):
        print(Node[i].val)#对齐方式
    if Node[i].tag.endswith('}spacing'):
        print(Node[i].beforeLines/63500)#段前距
        print(Node[i].afterLines/63500)#段后距
    if Node[i].tag.endswith('}ind'):
        print(Node[i].left/210)#左缩进
        print(Node[i].right/210)#右缩进
'''    







