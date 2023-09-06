import psycopg2


class OperationpostgresBase:

    def __init__(self,database):
        try:
            self.conn = psycopg2.connect(
                database=database[0],host=database[1],port=database[2],user=database[3],password=database[4])
        except Exception as e:
            print('ERROR','数据库连接出错，错误原因{}'.format(e))
            raise Exception('数据库连接出错！！')


