

#数据库信息
database = ['ys_yishi','192.168.5.250',25432,'postgres',123456]

#csv文件路径
# filename='C:\\Users\\Administrator\\Desktop\gujianhuizong\\jizhunceshi.csv'

#任务插件筛选
#plugin = '["unpacker", "crypto_hints", "cve_lookup", "elf_analysis", "ip_and_uri_finder", "software_components", "users_and_passwords", "elf_checksec"]'
#plugin = '["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]'
plugin = '[["unpacker", "crypto_hints", "cve_lookup", "elf_analysis", "ip_and_uri_finder", "software_components", "users_and_passwords", "elf_checksec"]]'
#plugin = '["unpacker", "elf_analysis"]'
#plugin = '["unpacker", "software_components"]'
#plugin = '["unpacker", "crypto_hints", "cve_lookup", "cwe_checker", "elf_analysis", "software_components", "elf_checksec", "ip_and_uri_finder", "users_and_passwords"]'

leak_name=['cve','cwe']

create_time ='2023-10-31'

#读取csv文件数据
import csv

csv_filepath = 'C:\\Users\\anban\\Desktop\\marketing\\firmware_1.csv'
def csv_firm_name(file_path):
    fw_names = []
    with open(file_path, 'r' ,encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 0:
                firmname = row[0].split('\\')[-1]
                fw_names.append(firmname)
        return fw_names


filepath = 'C:\\Users\\anban\\Desktop\\gujianhuizong\\qnx_test_cases'

filename = 'C:\\Users\\anban\\Desktop\\marketing\\firmware_1.csv'

excel_filepath = 'C:\\Users\\anban\\Desktop\\基准测试数据记录'
#新建表的title
datas = [['测试固件','文件数量','cpu架构','CWE缺陷','CVE漏洞','文件成分数量','组件及版本','敏感信息','安全编译选项','运行时间']]
#,'CPU架构','安全编译选项','敏感信息','文件类型'

l = []

# a = "{\"unpacker\": null, \"software_components\": {\"summary\": [], \"file_data\": {}}, \"file_type\": {}, \"cpu_architecture\": {}}"
# print(bool(a))