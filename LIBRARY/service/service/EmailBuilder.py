from LIBRARY.settings import EMAIL_HOST_USER,BASE_DIR
from string import Template

class EmailBuilder:
    template_dir = BASE_DIR + "/" + "service/template/"

    @staticmethod
    def sign_up(params):
        msg = ""
        msg+="<HTML><BODY>"
        msg+="registration is Successul for LMS project"
        msg+="<H1>Hi! Greetings from LMS!</H1>"
        msg+="<P>Congratulations for registering on LMS! You can now access your LMS account online - anywhere, anytime and enjoy the flexibility to check the Books Details.</P>"
        msg+="<p><b> Login Id: "+params["login"] +"<br>"+ " Password: "+params["password"]+ "</b></p>"
        msg+="<P> As a security measure, we recommended that you should change your password after you first log in.</p>"
        msg+="<p>We assure you the best service at all times and look forward to a warm and long-standing association with you.</p>"
        msg+="</BODY></HTML>"

        return msg

    @staticmethod
    def change_password(params):
        msg = ""
        msg += "<HTML><BODY>"
        msg+="<h2>"+"Your Password has been changed successfully!! "+params.firstName+" "+params.lastName+"<h1>"
        msg+="<p><b>"+"To access account user login id: "+params.login_id+" Password : "+params.password+"</b><b>"
        msg+="</BODY></HTML>"

        return msg

    @staticmethod
    def forgot_password(params):
        print("000000000009--",params)
        print("-------------->",params.firstName)
        msg = ""
        msg+= "<HTML><BODY>"
        msg += "<H1>"+"YOUR PASSWORD HAS BEEN RECOVERED "+params.firstName+" "+params.lastName+"</H1>"
        msg += "<P><B>"+"To access account user login id: "+params.login_id+"<br>"+" password: "+params.password
        msg+= "</BODY></HTML>"

        return msg
        