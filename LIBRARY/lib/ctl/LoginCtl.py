
from .BaseCtl import BaseCtl
from django.shortcuts import render, redirect
from lib.utility.DataValidator import DataValidator
from service.service.UserService import UserService


class LoginCtl(BaseCtl):

     # Populate Form from http request
    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]
        self.form["password"] = requestForm["password"]

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if (DataValidator.isNull(self.form["login_id"])):
            inputError["login_id"] = "Login can not be null"
            self.form["error"] = True
        else:
            if (DataValidator.isemail(self.form['login_id'])):
                inputError['login_id'] = "Login Id must be email"
                self.form['error'] = True

        if(DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password can not be null"
            self.form["error"] = True

        return self.form["error"]

    # Display Login Page
    def display(self, request, params={}):
        self.form['out'] = params.get("out")
        res = render(request, self.get_template(), {'form': self.form})
        return res

    # Submit the Login Page
    def submit(self, request, params={}):
        PATH = params.get('path')
        user = self.get_service().authenticate(self.form)
        if(user is None):
            self.form['error'] = True
            self.form["messege"] = "Invalid ID or Password"
            res = render(request, self.get_template(), {"form": self.form})
        else:
            print("LLLLLLLLLLLLL", PATH)
            request.session["user"] = user
            request.session['name'] = user.role_Name
            if PATH is None:
                res = redirect('/lib/Welcome/')
            else:
                res = redirect(PATH)
        return res

    # Template html of Login page
    def get_template(self):
        return "Login.html"

    # Service of User
    def get_service(self):
        return UserService()
