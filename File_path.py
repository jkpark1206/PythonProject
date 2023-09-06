import os
from  config import *

def traverse_folder(path) :
    for file_name in os.listdir(path):#获取当前目录下所有文件和文件夹的名称
        file_path=os.path.join(path,file_name)#将文件名和路径连接起来
        if os.path.isdir(file_path):#判断该路径是否为文件夹
            traverse_folder(file_path)#如果是文件夹,则递归调用该函数
        else:
            l.append(file_path)
    return l

# if __name__ == '__main__':
#    for i in traverse_folder(filepath):
#        firmname = i.split('\\')[-1]
#        print(firmname)