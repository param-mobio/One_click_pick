from user.models import User
from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages
# from register import val

class Otp(View):
    def get(self,request):
        
        return render(request,'authentication/otp.html')
    
    def post(self,request):
        otp = request.POST.get('otp')
        realotp = request.POST.get('realotp')
        email = request.POST.get('email')
        print(email)
        # print(email)
        # realotp = val()
        print(otp)
        print(realotp)
        print(type(otp))
        print(type(realotp))
        # email = request.POST.get('email')
        if(otp==realotp):
            print('*******')
            user = User.objects.get(otp=otp)
            user.is_active = True
            user.save()
            return redirect('customer_login')
        print('********')
        error_message = 'Otp is wrong please try again'
        context = {
            'error_message' : error_message,    
            'otp' : realotp,
            'email' : email,
        }
        return render(request,'authentication/otp.html',context)
        

