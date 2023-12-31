#获取基准测试报告数据，写入表格中，方便与旧报告中的数据进行对比，仅作为初步对比，还需进入页面确认报告内容

from conn_database import OperationpostgresBase
from sql import Handle_sql
from config import *
import json
import datetime
from File_path import traverse_folder
from Save_Excel import *
from excel_datas import Handle_openpyxl

class Base_Compare_Data:
    def __init__(self):
        self.cur = OperationpostgresBase(database).conn.cursor()  # 连接数据库


    def get_file_type_datas(self):
        try:
            #方法1：读取文件夹下的所有文件
            for i in traverse_folder(filepath):
                firmname = i.split('\\')[-1]

            #方法2：读取CSV文件中的固件名  此处传的必须是固件名，不能是固件路径，因为sql语句中是通过固件名查找的
            # for firmname in csv_firm_name(csv_filepath):

            #sql语句查询相应结果
                self.cur.execute(Handle_sql().get_plugin_sql(firmname, plugin,create_time))
                firmware = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_base_data_sql(firmname, plugin,create_time))
                base_datas = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_cve_sql(firmname, plugin,create_time))
                All_cve = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_cwe_sql(firmname, plugin,create_time))
                All_cwe = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_create_time_sql(firmname, plugin, create_time))
                start_date = self.cur.fetchall()
                self.cur.execute(Handle_sql().get_end_time_sql(firmname, plugin, create_time))
                end_date = self.cur.fetchall()

                soft_list = list()
                if bool(firmware) is True or bool(base_datas) is True:   #任务存在
                    #提取file_type
                    All_file_type = json.loads(firmware[0][0])['file_type']['summary']
                    file_type = str(All_file_type)[1:-1]

                    #提取CPU信息
                    All_cpu = json.loads(firmware[0][0])['cpu_architecture']['summary']
                    cpu = str(All_cpu)[1:-1]

                    #提取安全风险数据
                    All_elf_checksec = json.loads(firmware[0][0])['elf_checksec']['count']

                    #提取文件成分数量
                    software_components_count = len(json.loads(firmware[0][0])['software_components']['summary'])


                    #提取敏感信息数据（ip插件+user插件的数量总和）
                    # 获取ip插件中的敏感信息数据
                    ip_uri = json.loads(firmware[0][0])['ip_and_uri_finder']['summary']
                    ip_uri_len = len(list(ip_uri.values()))
                    ip_uri_datas = []
                    if len(ip_uri) > 0:
                        for i in range(0, ip_uri_len):
                            ip_uri_s = list(ip_uri.values())[i]["plugin_res"]
                            ip_uri_data = len(ip_uri_s)
                            ip_uri_datas.append(ip_uri_data)
                    else:
                        ip_uri_datas = [0]
                    All_ip_uri = sum(ip_uri_datas)
                    #获取user插件中的敏感信息数据
                    user_passwd = json.loads(firmware[0][0])['users_and_passwords']['summary']
                    user_passwd_len = len(list(user_passwd.values()))
                    user_passwd_datas = []
                    if len(user_passwd) > 0:
                        for i in range(0, user_passwd_len):
                            user_passwd_s = list(user_passwd.values())[i]["plugin_res"]
                            user_passwd_data = len(user_passwd_s)
                            user_passwd_datas.append(user_passwd_data)
                    else:
                        user_passwd_datas = [0]
                    All_user_passwd = sum(user_passwd_datas)
                    #敏感信息数据由ip和user插件的数据相加
                    All_sensetive = All_ip_uri + All_user_passwd



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

                    #文件成分（组件及其版本）
                    software_components = json.loads(firmware[0][0])['software_components']['summary']
                    for software in software_components:
                        software_components_name = software[0] + software[1]
                        soft_list.append(software_components_name)
                    all_software_components = str(soft_list)[1:-1]

                    #计算任务运行的时间
                    t1 = start_date[0][0]
                    t2 = end_date[0][0]
                    use_time = t2-t1


                    #把所有数据放进一个列表中
                    ll = (firmname,file_type_count,cpu,cwe,cve,software_components_count,all_software_components,All_sensetive,All_elf_checksec,use_time)
                    data = list(ll)
                    datas.append(data)
                    #,cpu,All_elf_checksec,All_sensetive,file_type


                else:
                    ll = (firmname, '任务不存在', '/', '/', '/', '/', '/', '/', '/', '/')
                    data = list(ll)
                    datas.append(data)


            #把列表的数据加到excel表格中
            Excel_Create(datas)


        except Exception as e:
            print('固件提取数据失败,失败原因：{}'.format(e))


if __name__ == '__main__':
    Base_Compare_Data().get_file_type_datas()



