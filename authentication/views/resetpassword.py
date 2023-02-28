from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpRequest
from user.models import User
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages

class Resetpassword(View):
    def get(self,request):
        return render(request,'authentication/resetpassword.html')
    def post(self,request):
        password = request.POST.get('currentpassword')
        newpassword = request.POST.get('newpassword')
        confirmpassword = request.POST.get('confirmpassword')
        user = request.user
        if(check_password(password,user.password)):
            l, u, p, d = 0, 0, 0, 0
            if (len(newpassword) >= 8):
                for i in newpassword:

                    # counting lowercase alphabets
                    if (i.islower()):
                        l += 1

                    # counting uppercase alphabets
                    if (i.isupper()):
                        u += 1

                    # counting digits
                    if (i.isdigit()):
                        d += 1

                    # counting the mentioned special characters
                    if (i == '@' or i == '$' or i == '_'):
                        p += 1
                if (l < 1 or u < 1 or p < 1 or d < 1 or l+p+u+d != len(newpassword)):
                    messages.info(request,'password must be strong')
                else:
                    if(newpassword==confirmpassword):
                        user.password = make_password(confirmpassword)
                        return redirect('profile')
                    else:
                        messages.info(request,'New password and confirm password should be same')
                    
            else:
                messages.info(request,'password is short')
                    
        else:
            messages.info(request,'Current passowrd is wrong')        

        return render(request,'authentication/resetpassword.html')