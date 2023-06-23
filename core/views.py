from django.shortcuts import render
from django.views import View
from product.models import Product, Category, Variation
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Cart, CartItem
from django.core.paginator import Paginator
# Create your views here.


class HomeView(LoginRequiredMixin, View):
    login_url = 'CustomerUser:login'

    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        count = 0
        variation_list = Variation.objects.all()
        # for variation in variation_list:
        #     variation.sale_price = variation.sale_price/23000
        #     variation.save()
        paginator = Paginator(variation_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if cart_item.exists():
            for item in cart_item:
                count = count + item.quantity
        context = {
            'page_obj': page_obj,
            'numberInCart': count
        }
        return render(request, 'home-page.html', context)

    def post(self, request):
        searchTxt = request.POST.get('searchText')
        variation_list = Variation.objects.filter(product__title__contains=searchTxt)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        count = 0
        paginator = Paginator(variation_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if cart_item.exists():
            for item in cart_item:
                count = count + item.quantity
        context = {
            'page_obj': page_obj,
            'numberInCart': count
        }
        return render(request, 'home-page.html', context)


class CategoryView(HomeView):

    def get(self, request, idCategory):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        count = 0
        variation_list = Variation.objects.filter(product__category__pk=idCategory)
        paginator = Paginator(variation_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if cart_item.exists():
            for item in cart_item:
                count = count + item.quantity
        context = {
            'page_obj': page_obj,
            'numberInCart': count,
            'CategoryID': idCategory
        }
        return render(request, 'home-page.html', context)

    def post(self, request, idCategory):
        searchTxt = request.POST.get('searchText')
        variation_list = Variation.objects.filter(product__title__contains=searchTxt, product__category__pk=idCategory)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart)
        count = 0
        paginator = Paginator(variation_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if cart_item.exists():
            for item in cart_item:
                count = count + item.quantity
        context = {
            'page_obj': page_obj,
            'numberInCart': count,
            'CategoryID': idCategory
        }
        return render(request, 'home-page.html', context)

