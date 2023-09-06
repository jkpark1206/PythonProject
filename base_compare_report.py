#获取基准测试报告数据，写入表格中，方便与旧报告中的数据进行对比，仅作为初步对比，还需进入页面确认报告内容

from conn_database import OperationpostgresBase
from sql import Handle_sql
from config import *
import json
from File_path import traverse_folder
from Save_Excel import *

class Base_Compare_Data:
    def __init__(self):
        self.cur = OperationpostgresBase(database).conn.cursor()  # 连接数据库


    def get_file_type_datas(self):
        try:
            for i in traverse_folder(filepath):
                firmname = i.split('\\')[-1]
                self.cur.execute(Handle_sql().get_plugin_sql(firmname, plugin))
                firmware = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_base_data_sql(firmname, plugin))
                base_datas = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_cve_sql(firmname, plugin))
                All_cve = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_cwe_sql(firmname, plugin))
                All_cwe = self.cur.fetchall()

                if bool(firmware) is True or bool(base_datas) is True:   #任务存在
                    #提取file_type
                    # All_file_type = json.loads(firmware[0][0])['file_type']['summary']
                    # file_type = str(All_file_type)[1:-1]

                    #提取CPU信息
                    All_cpu = json.loads(firmware[0][0])['cpu_architecture']['summary']
                    cpu = str(All_cpu)[1:-1]

                    #提取安全风险数据
                    All_elf_checksec = json.loads(firmware[0][0])['elf_checksec']['count']

                    #提取文件成分数量
                    All_software_components = len(json.loads(firmware[0][0])['software_components']['summary'])

                    #提取敏感信息数据（ip插件+user插件的数量总和）
                    a = json.loads(firmware[0][0])['ip_and_uri_finder']['summary']
                    b = json.loads(firmware[0][0])['users_and_passwords']['summary']
                    if bool(a) is True and bool(b) is True:
                        All_ip_count = len(list(a.values())[0]['plugin_res'])
                        All_users_count = len(list(b.values())[0]['plugin_res'])
                        All_sensetive = All_ip_count+All_users_count
                    elif bool(a) is True and bool(b) is False:
                        All_sensetive = len(list(a.values())[0]['plugin_res'])
                    elif bool(a) is False and bool(b) is True:
                        All_sensetive =len(list(b.values())[0]['plugin_res'])
                    else:
                        All_sensetive = 0

                    # 提取文件解包数量
                    file_type_count = json.loads(base_datas[0][0])['total_files_count']

                    #提取cve和cwe
                    if bool(json.loads(All_cve[0][0]))  is True:
                        cve = json.loads(All_cve[0][0])['all']
                    else:
                        cve = 0
                    if bool(json.loads(All_cwe[0][0])) is True:
                        cwe = json.loads(All_cwe[0][0])['all']
                    else:
                        cwe = 0
                    #把所有数据放进一个列表中
                    a = (firmname,cpu,file_type_count,cwe,cve,All_sensetive,All_software_components,All_elf_checksec)
                    data = list(a)
                    datas.append(data)
                else:
                    continue
            #把列表的数据加到excel表格中
            Excel_Create(datas)


        except Exception as e:
            print('固件提取数据失败,失败原因：{}'.format(e))


if __name__ == '__main__':
    Base_Compare_Data().get_file_type_datas()
