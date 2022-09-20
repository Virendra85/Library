from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.sessions.models import Session

from .ctl.LoginCtl import LoginCtl
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.ForgetPasswordCtl import  ForgetPasswordCtl
from .ctl.ChangePasswordCtl import ChangePasswordCtl
from .ctl.UserCtl import UserCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.MyProfileCtl import MyProfileCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.RoleListCtl import RoleListCtl
from .ctl.BookCtl import BookCtl
from .ctl.BookListCtl import BookListCtl
from .ctl.BooksListCtl import BooksListCtl


'''
Calls respective controller with id
'''

@csrf_exempt
def actionId(request, page="", operation="", id=0):
    """
    Arguments--
        request: HTTP Request is responsible to send/recieve the data from browser to server.

        page: This argument stores the page name which user wants to see.

        operation: This argument stores the operation name which user wants to perform.

        id: This argument stores the id by which we can get the data of user.

    Attributes--
        path:  It stores the URI from the requested URL.

        ctlObj: It is object of controller(ctlName) class.

        res: It nothing just a response from execute method of respective controller which return a template with data. 
    """

    path = request.META.get('PATH_INFO')
    print("VVVVVVVVVVVVVVVV", path)
    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        res = ctlObj.execute(request, {"id": id})
    elif page == "Registration":
        ctlName = "Registration" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Login":
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        print("MMMMMMMMMMM", request.session.get('msg'))
        res = ctlObj.execute(request, {"id": id, })

    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = "Your Session has been Expired, Please Login again"
        res = ctlObj.execute(request, {"id": id, 'path': path})
    return res


@csrf_exempt
def auth(request, page="", operation="", id=0):
    """
     Arguments--
        request: HTTP Request is responsible to send/recieve the data from browser to server.

        page: This argument stores the page name which user wants to see.

        operation: This argument stores the operation name which user wants to perform.

        id: This argument stores the id by which we can get the data of user.

    Attributes--
        ctlObj: It is object of controller(ctlName) class.

        out: It is logout message.

        res: It nothing just a response from execute method of respective controller which return a template with data. 
    """
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        out = "LOGOUT SUCCESSFULL"
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation, 'out': out})

    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation})
    return res



def index(request):
    """ First page of the LMS Application   """

    res = render(request, 'project.html')
    return res

def GET(self):
    """ To remove Favicon error from   """

    return HttpResponse("Hello Guys")
