

#数据库信息
database = ['ys_yishi','192.168.5.242',25432,'postgres',123456]

#csv文件路径
# filename='C:\\Users\\Administrator\\Desktop\gujianhuizong\\jizhunceshi.csv'

#任务插件筛选
plugin = '["unpacker", "crypto_hints", "cve_lookup", "cwe_checker", "elf_analysis", "software_components", "elf_checksec", "ip_and_uri_finder", "users_and_passwords"]'
#plugin = '["software_components","cve_lookup","crypto_hints","elf_analysis","elf_checksec","sensitive_msg", "cwe_checker"]'

leak_name=['cve','cwe']

filepath = 'C:\\Users\\anban\\Desktop\\gujianhuizong\\jizhunceshi'

filename = 'C:\\Users\\anban\\Desktop\\gujianhuizong\\jizhunceshi.csv'

excel_filepath = 'C:\\Users\\anban\\Desktop\\基准测试数据记录'
#新建表的title
datas = [['测试固件','CPU架构','文件数量','CWE缺陷','CVE漏洞','敏感信息','文件成分','安全编译选项']]

l = []