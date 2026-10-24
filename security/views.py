from django.shortcuts import render, redirect, HttpResponse #type:ignore
from django.contrib.auth.models import User #type:ignore
from django.contrib import messages #type:ignore
from django.template.loader import render_to_string #type: ignore
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from estore import settings #type: ignore 
from django.views import View
from .utils import TokenGenerator,generate_token #type: ignore 
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError   #type: ignore 
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate,login as auth_login,logout as userlogout
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check if passwords match
        if (pass1 != pass2):
             messages.warning(request,"Password do not match")
            #  HttpResponse("Passwords do not match.")
             return render(request, "signup.html")  # Stop execution and return

        # Check if email is already taken
        if User.objects.filter(email=email).exists():
            messages.warning(request,"Email is Already Exist")
            return render(request, "signup.html")  # Stop execution and return

        # Create the user
        user=User.objects.create_user(username=email, email=email, password=pass1, first_name=name)
        user.is_active=False
        user.save()
        user.is_active=True
        user.save()
#         subject="Account Activation"
#         msg=render_to_string('activate.html',{
#             'user':user,
#             'domain':'127.0.0.1:8000',
#             'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#             'token':generate_token.make_token(user)
#         })

        
#         email = EmailMessage(
#             subject,
#             msg,
#             settings.EMAIL_HOST_USER,
#             [email]
#         )
#         email.send()
#         messages.success(request,f"Activation link is forward to {email}")
        return redirect("/auth/login")
    return render(request, "signup.html")  

# class ActivateAccountView(View):
#     def get(self,request,uidb64,token):
#         try:
#             uid=force_str(urlsafe_base64_decode(uidb64))
#             user=User.objects.get(pk=uid)
#         except Exception as identifier:
#             user=None
#         if user is not None and generate_token.check_token(user,token):
#             user.is_active=True
#             user.save()
#             messages.info(request,"Your Account has been Successfully Activated!")
#             return redirect ("/security/login/")
#         return render(request,"fail.html")



def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass1']
        userauth=authenticate(username=username,password=password)
        if userauth is not None:
            auth_login(request,userauth)
            messages.success(request,"Login Success")
            return render(request,"index.html")
        else:
            messages.error(request,"Invalid username/password")
            return render(request, "login.html")
    return render(request, "login.html")

def logout(request):
    userlogout(request)
    messages.info(request,"Logout Success")
    return render(request,"login.html")
