from django.shortcuts import render,redirect
from lib.utility.DataValidator import DataValidator
from service.models import Book,User
from .BaseCtl import BaseCtl
from service.service.BooksService import BooksService
from django.contrib.sessions.models import Session

class BooksListCtl(BaseCtl):
    count = 1

    # Populate Form from http request
    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]

    # Display the Book List Page
    def display(self, request, params={}):
        BooksListCtl.count = self.form['pageNo']
        record = self.get_service().search(self.form)
        self.page_list = record['data']
        self.form['LastId'] = Book.objects.last().id
        res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
        return res

    def deleteRecord(self, request,params={}):
        id = self.form['id']
        print(f"Iddddddddddddddd {id}")
        obj = User.objects.get(id=id)
        obj.delete()
        request.session['user'] = None
        request.session['name'] = None
        self.form["error"] = True
        self.form["messege"] = "Your account has been deleted successfully"
        return render(request,"Login.html", {'form':self.form})


    def submit(self, request, params={}):
        pass

    # Template html of BooksList page
    def get_template(self):
        return "BooksList.html"

    # Service class of Book
    def get_service(self):
        return BooksService()
