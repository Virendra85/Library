from service.models import Book
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains book business logics
'''
class BookService(BaseService):
    def get_model(self):
        return Book

    def search(self,params):
        print("Page No------->",params['pageNo'])
        pageNo = (params['pageNo']-1) * self.pageSize
        sql = "select * from lms_book where 1=1"
        val  = params.get("bookName", None)
        if (DataValidator.isNotNull(val)):
            sql += " and bookName = '"+val+"' "
        sql += " limit %s,%s"
        cursor = connection.cursor()
        print("------------------>",sql,pageNo,self.pageSize)
        params['index'] = ((params['pageNo'] - 1) * self.pageSize)+1
        cursor.execute(sql,[pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('id','bookName','bookDescription','bookStatus')
        res = {
            'data': [],
        }
        res["index"] = params["index"]
        for x in result:
            print({columnName[i]: x[i] for i,_ in enumerate(x)})
            res["MaxId"] =  params['MaxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i,_ in enumerate(x)})
        return res



