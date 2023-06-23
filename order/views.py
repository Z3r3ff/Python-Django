from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Category, Variation
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Cart, CartItem
from .models import Oder
# Create your views here.


class CheckoutView(LoginRequiredMixin, View):
    login_url = 'CustomerUser:login'

    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        count = 0
        totalCost = 0
        if cart_item.exists():
            for item in cart_item:
                count = count + item.quantity
                totalCost = totalCost + item.item.sale_price*item.quantity
        return render(request, 'checkout-page.html', {'cartItem': cart_item, 'numberInCart': count, 'cart': cart, 'totalCost':totalCost})

    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        payment_method = str(request.POST.get('paymentMethod'))
        ship_address = str(request.POST.get('address'))
        order = Oder.objects.create(user=request.user, cart=cart, order_description=payment_method, shipping_address=ship_address)
        order.save()
        return redirect('core:checkout')
