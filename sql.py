#sql查询语句
from conn_database import OperationpostgresBase
from config import *

class Handle_sql:
    def get_cve_sql(self,fw_name,plugin,create_time):   #查找cve和cwe总数
        cve_sql = "SELECT r.cve_count FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' and DATE(t.create_time)='{}' ORDER BY t.end_time desc limit 1".format(fw_name,plugin,create_time)
        return cve_sql

    def get_cwe_sql(self,fw_name,plugin,create_time):   #查找cve和cwe总数
        cwe_sql = "SELECT r.cwe_count FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' and DATE(t.create_time)='{}' ORDER BY t.end_time desc limit 1".format(
                        fw_name,plugin,create_time)
        return cwe_sql


    def get_plugin_sql(self,filename,plugin,create_time):    #查找ys_firmware_scan_result表中的plugin字段，返回所有基本信息数据
        plugin_sql = "SELECT r.plugin FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' and DATE(t.create_time)='{}' ORDER BY t.end_time desc limit 1".format(filename,plugin,create_time)
        return plugin_sql

    def get_base_data_sql(self,fw_name,plugin,create_time):  #查找基本信息中的数据
        base_data_sql = "SELECT r.meta FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' and DATE(t.create_time)='{}' ORDER BY t.end_time desc limit 1".format(
                        fw_name,plugin,create_time)
        return base_data_sql

    def get_create_time_sql(self,filename,plugin,create_time):    #查找任务开始时间
        c_time = "SELECT t.start_time FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' and DATE(t.create_time)='{}' ORDER BY t.end_time desc limit 1".format(filename,plugin,create_time)
        return c_time

    def get_end_time_sql(self,filename,plugin,create_time):    #查找任务结束时间
        e_time = "SELECT t.end_time FROM ys_firmware_scan_result r , ys_firmware_scan_task t where r.task_id=t.id and t.is_delete='f' and t.task_name='{}' and t.plugin='{}' and DATE(t.create_time)='{}' ORDER BY t.end_time desc limit 1".format(filename,plugin,create_time)
        return e_time

# if __name__ == '__main__':
#     print(Handle_sql().get_cve_sql('Aceex-NR22-webflash.bin',plugin,create_time))
#     print(Handle_sql().get_create_time_sql('Aceex-NR22-webflash.bin', plugin,create_time))

