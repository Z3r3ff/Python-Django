from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Variation
from cart.models import Cart, CartItem
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductView(LoginRequiredMixin, View):
    login_url = 'CustomerUser:login'

    def get(self, request, id):
        variation = Variation.objects.get(product__pk=id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        count = 0

        if cart_item.exists():
            for item in cart_item:
                count = count + item.quantity
        return render(request, 'detailProduct.html', {'item': variation, 'cart': cart, 'numberInCart': count})

