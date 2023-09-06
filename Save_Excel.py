from openpyxl import Workbook
import openpyxl
import datetime
from config import *
import time

# date = time.strftime("%Y%m%d-%H%M%S",time.localtime())
# print(date)
# 写入数据
def Excel_Create(data):
    # 创建一个叫wk的excel表格
    wk = Workbook()
    # 选择第一个工作表
    sheet = wk.active
    date = time.strftime("%Y%m%d-%H%M%S",time.localtime())
    for row in data:
        sheet.append(row)
        wk.save('C:\\Users\\Administrator\\Desktop\\基准测试数据记录{}.xlsx'.format(date))

if __name__ == '__main__':
    data =[['学号', '姓名', '成绩']]
    Excel_Create(data)

