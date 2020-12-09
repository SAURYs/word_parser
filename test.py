#!/usr/bin/python
import sys
import traceback
import os

diary_log_path = os.path.join(os.getcwd(), r'1111.log')
outputfile = open(diary_log_path, 'w', encoding='UTF-8')
sys.stdout = outputfile
c =3
d = 0

try:
    a = c/d
except Exception as e:
    #print('invoking division failed.')
    traceback.print_exc(file = outputfile)
print('jixu')