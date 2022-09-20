from django.shortcuts import render
from lib.utility.DataValidator import DataValidator
from .BaseCtl import BaseCtl
from service.models import Book
from service.service.BookService import BookService

class BookCtl(BaseCtl):

    # Populate Form from http request
    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['bookName'] = requestForm['bookName']
        self.form['bookDescription'] = requestForm['bookDescription']
        self.form['bookStatus'] = requestForm['bookStatus']

    # Populate Form from model
    def model_to_form(self, obj):
        if (obj==None):
            return
        self.form['id'] = obj.id
        self.form['bookName'] = obj.bookName
        self.form['bookDescription'] = obj.bookDescription
        self.form['bookStatus'] = obj.status

    # Convert Form into model
    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if (pk>0):
            obj.id = pk
        obj.bookName = self.form['bookName']
        obj.bookDescription = self.form['bookDescription']
        obj.status = self.form['bookStatus']
        return obj

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']
        if (DataValidator.isNull(self.form['bookName'])):
            inputError['bookName'] = "book Name can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['bookName'])):
                inputError['bookName'] = "Name contains only letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['bookDescription'])):
            inputError['bookDescription'] = "book Description can not be null"
            self.form['error'] = True
        if (DataValidator.isNull(self.form['bookStatus'])):
            inputError['bookStatus'] = "book Status can not be null"
            self.form['error'] = True

        return self.form['error']

    # Display Book Page
    def display(self, request, params={}):
        if (params['id']>0):
            id = params['id']
            r = self.get_service().get(id)
            self.model_to_form(r)
        res = render(request,self.get_template(),{'form':self.form})
        return res

    # Submit Book Page
    def submit(self, request, params={}):
        if (params['id']>0):
            pk = params['id']
            dup = self.get_service().get_model().objects.exclude(id=pk).filter(bookName = self.form['bookName'])
            if dup.count()>0:
                self.form['error'] = True
                self.form['messege'] = "book Name already exists"
                res = render(request,self.get_template(),{'form':self.form})
            else:
                r = self.form_to_model(Book())
                self.get_service().save(r)
                self.form['id'] = r.id

                self.form['error'] = False
                self.form['messege'] = "DATA HAS BEEN UPDATED SUCCESSFULLY"
                res = render(request,self.get_template(),{'form':self.form})
        else:
            duplicate = self.get_service().get_model().objects.filter(bookName = self.form['bookName'])
            if duplicate.count()>0:
                self.form['error'] = True
                self.form['messege'] = "book Name already exists"
                res = render(request,self.get_template(),{'form':self.form})
            else:
                r = self.form_to_model(Book())
                self.get_service().save(r)
                self.form['id'] = r.id

                self.form['error'] = False
                self.form['messege'] = "DATA HAS BEEN SAVED SUCCESSFULLY"
                res = render(request,self.get_template(),{'form':self.form})
        return res


    # Template html of book Page
    def get_template(self):
        return "Book.html"

    # Service for Book
    def get_service(self):
        return BookService()
