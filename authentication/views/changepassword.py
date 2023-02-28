from user.models import User
from django.shortcuts import redirect, render
from django.views import View
import uuid
from django.contrib import messages
from authentication.helpers import send_forget_password_email

class Changepassword(View):
    def get(self, request, token):
        profile_obj = User.objects.filter(
            forget_password_token=token).first()
        context = {
            'profile_obj': profile_obj.id
        }
        return render(request, 'account/changepassword.html', context)

    def post(self, request, token):
        profile_obj = User.objects.filter(
            forget_password_token=token).first()
        context = {
            'profile_obj': profile_obj.id
        }
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmpassword')
        user_id = request.POST.get('user_id')

        if user_id is None:
            messages.success(request, 'No user id found')
            return render(request, 'account/changepassword.html', context)

        l, u, p, d = 0, 0, 0, 0
        if (len(new_password) >= 8):
            for i in new_password:

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
            if (l < 1 or u < 1 or p < 1 or d < 1 or l+p+u+d != len(new_password)):
                messages.success(request, "password is not valid")
                return render(request, 'account/changepassword.html', context)
        else:
            messages.success(request, "password is short")
            return render(request, 'account/changepassword.html', context)

        if new_password != confirm_password:
            messages.success(request, "both password should be same")
            return render(request, 'account/changepassword.html', context)

        user_obj = User.objects.get(id=user_id)
        user_obj.set_password(new_password)
        user_obj.save()
        return redirect('customer_login')