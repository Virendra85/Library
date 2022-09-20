from django.shortcuts import render
from lib.utility.DataValidator import DataValidator
from service.models import Book
from .BaseCtl import BaseCtl
from service.service.BookService import BookService

class BookListCtl(BaseCtl):
    count = 1

    # Populate Form from http request
    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id',None)
        self.form['bookName'] = requestForm.get('bookName',None)
        self.form['bookDescription'] = requestForm.get('bookDescription',None)
        self.form['ids'] = requestForm.getlist('ids', None)

    # Display Book List Page
    def display(self, request, params={}):
        BookListCtl.count = self.form['pageNo']
        record = self.get_service().search(self.form)
        self.page_list = record['data']
        self.form['LastId'] = Book.objects.last().id
        res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        return res

    # Display the next Page
    def next(self, request,params={}):
        BookListCtl.count += 1
        self.form['pageNo'] = BookListCtl.count
        record = self.get_service().search(self.form)
        self.page_list = record['data']
        if self.page_list==[]:
            self.form['mesg'] = "No record found"
        self.form['LastId'] = Book.objects.last().id
        res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        return res

    # Display the previous Page
    def previous(self, request,params={}):
        BookListCtl.count -= 1
        self.form['pageNo'] = BookListCtl.count
        record = self.get_service().search(self.form)
        self.page_list = record['data']
        res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        return res

    # Display the search Result
    def submit(self, request,params={}):
        BookListCtl.count = 1
        record = self.get_service().search(self.form)
        self.page_list = record['data']
        if self.page_list==[]:
            self.form['mesg'] = "No record found"
        res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        return res

    # Delete the Book
    def deleteRecord(self, request, params={}):
        self.form['pageNo'] = BookListCtl.count
        if (bool(self.form['ids'])==False):
            self.form['error'] = True
            self.form['messege'] = "Please Select at least one Checkbox"
            record = self.get_service().search(self.form)
            self.page_list = record['data']
            res =  render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        else:
            for ids in self.form['ids']:
                record = self.get_service().search(self.form)
                self.page_list = record['data']

                id = int(ids)
                if id>0 :
                    r = self.get_service().get(id)
                    if r is not None:
                        self.get_service().delete(r.id)
                        self.form['pageNo'] = 1
                        record = self.get_service().search(self.form)
                        self.page_list = record['data']
                        self.form['LastId'] = Book.objects.last().id                        
                        BookListCtl.count = 1
                        
                        self.form['error'] = False
                        self.form['messege'] = "DATA HAS BEEN DELETED SUCCESSFULLY"
                        res =  render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
                    else:
                        self.form['error'] = True
                        self.form['messege'] = "DATA WAS NOT DELETED"
                        res =  render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        return res

    # Template html of BookList page
    def get_template(self):
        return "BookList.html"

    # Service class of Book
    def get_service(self):
        return BookService()


