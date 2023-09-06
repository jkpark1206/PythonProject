

#数据库信息
database = ['ys_yishi','192.168.1.208',25432,'postgres',123456]

#csv文件路径
# filename='C:\\Users\\Administrator\\Desktop\gujianhuizong\\jizhunceshi.csv'

#任务插件筛选
plugin = '["unpacker", "crypto_hints", "cve_lookup", "cwe_checker", "elf_analysis", "software_components", "elf_checksec", "ip_and_uri_finder", "users_and_passwords"]'
#plugin = '["software_components","cve_lookup","crypto_hints","elf_analysis","elf_checksec","sensitive_msg"]'

leak_name=['cve','cwe']

filepath = 'C:\\Users\\Administrator\\Desktop\\gujianhuizong\\jizhunceshi'

#新建表的title
title=['测试固件','CPU架构','文件数量','敏感信息','CWE缺陷','CVE漏洞','文件成分','许可证书','安全编译选项']

#缺陷表的文件路径
excel_path = 'C:/Users/anban/Desktop/PingCode.Project-易识开源软件供应链安全评估系统-缺陷-export20230212030907.xls'


datas = [['测试固件','CPU架构','文件数量','CWE缺陷','CVE漏洞','敏感信息','文件成分','安全编译选项']]

l = []