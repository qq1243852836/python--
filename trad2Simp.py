import os
from langconv import *
import numpy as np
def Traditional2Simplified(self):
    self = Converter('zh-hans').convert(self)
    return self


def file_conv(self):				
    fd = open(self,'r+',encoding='utf-8',errors='ignore')
    #print(fd.read())
    buff = Traditional2Simplified(fd.read())
    
    fd.seek(0,0)
    fd.write(buff)
    fd.close()

	


def file_dir_path(path):
    list = []  
    for roots,dirs,files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                list.append(os.path.join(roots,file))
    return list

if __name__=="__main__":
    path = r'C:\Users\huangyj\Desktop\help document - Copy\第四階段\HT67F2362-1015\help document\help-document繁體中文\help-document繁體中文\example code'
    file_path_list = file_dir_path(path)
    for list in file_path_list:
        file_conv(list)
