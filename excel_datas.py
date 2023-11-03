import csv
from config import *

class Handle_openpyxl:
    def __init__(self):

        try:
            self.wb = open(filename, encoding = 'utf-8')
        except:
            print('打开文件失败，请检查')

    def Read_csv(self):
        self.reader = csv.reader(self.wb)
        fw_names = []

        # for row in self.reader:
        #     fw_names = [row[0]][0]
        #     # return fw_names
        #     print(fw_names)

        try:
            for i in self.reader:
                fw_names.append(i[0])
            return fw_names
        except Exception as e:
            print('提取cve数据失败,失败原因：{}'.format(e))

# if __name__ == '__main__':
#     print(Handle_openpyxl().Read_csv())

