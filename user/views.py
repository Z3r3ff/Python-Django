from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from cart.models import Cart
from user.models import CustomerUser
# Create your views here.


class viewLogin(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        check_user = authenticate(username=username, password=password)
        if check_user is None:
            return HttpResponse('User khong ton tai')
        login(request, check_user)
        return redirect('core:homepage')


class viewLogout(View):

    def get(self, request):
        logout(request)
        return redirect('CustomerUser:login')

class viewSigup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenum = request.POST.get('phonenum')
        address = request.POST.get('address')
        if request.method == "POST":
            customer_user = CustomerUser()
            customer_user.first_name = firstname
            customer_user.last_name = lastname
            customer_user.username = username
            customer_user.email = email
            customer_user.set_password(password)
            customer_user.phone_number = phonenum
            customer_user.address = address
            customer_user.save()
            cart = Cart.objects.create(user=customer_user)
            cart.save()
            return redirect('CustomerUser:login')



