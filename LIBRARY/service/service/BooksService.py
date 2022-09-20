from service.models import Book
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains book business logics
'''
class BooksService(BaseService):
    def get_model(self):
        return Book

    def search(self,params):
        sql = "select * from lms_book"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        params['index'] = ((params['pageNo'] - 1) * self.pageSize)+1
        columnName = ('id','bookName','bookDescription','bookStatus')
        res = {
            'data': [],
        }
        for x in result:
            res['data'].append({columnName[i]: x[i] for i,_ in enumerate(x)})
        return res



