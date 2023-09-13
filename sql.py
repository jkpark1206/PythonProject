#sql查询语句
from conn_database import OperationpostgresBase
from config import *

class Handle_sql:
    def get_cve_sql(self,fw_name,plugin):   #查找cve和cwe总数
        cve_sql = "SELECT r.cve_count FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' ORDER BY t.end_time desc limit 1".format(
                        fw_name,plugin)
        return cve_sql

    def get_cwe_sql(self,fw_name,plugin):   #查找cve和cwe总数
        cwe_sql = "SELECT r.cwe_count FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' ORDER BY t.end_time desc limit 1".format(
                        fw_name,plugin)
        return cwe_sql


    def get_plugin_sql(self,filename,plugin):    #查找ys_firmware_scan_result表中的plugin字段，返回所有基本信息数据
        plugin_sql = "SELECT r.plugin FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}'  ORDER BY t.end_time desc limit 1".format(filename,plugin)
        return plugin_sql

    def get_base_data_sql(self,fw_name,plugin):
        base_data_sql = "SELECT r.meta FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' ORDER BY t.end_time desc limit 1".format(
                        fw_name,plugin)
        return base_data_sql

if __name__ == '__main__':
    print(Handle_sql().get_cve_sql('Aceex-NR22-webflash.bin',plugin))


