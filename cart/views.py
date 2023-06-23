from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from user.models import CustomerUser
from product.models import Variation
from django.contrib import messages
# Create your views here.


def add_to_cart(request, idItem, idCart):

    if request.method=="POST":
        item = get_object_or_404(Variation, product__pk=idItem) #item can them
        cart = get_object_or_404(Cart, pk=idCart, user=request.user) #gio hang cua nguoi dung
        cart_item_old = CartItem.objects.filter(cart=cart, item=item)
        input_quantity = int(request.POST.get('quantity'))
        if cart_item_old.exists():
            check = False
            for cart_item in cart_item_old:
                if cart_item.item.product.pk==item.product.pk:
                    cart_item.quantity = cart_item.quantity + input_quantity
                    cart_item.save()
                    check = True
                    break
            if check==False:
                cart_item_new = CartItem.objects.create(item=item, cart=cart, quantity=input_quantity)
                messages.info(request, "Product was added to your cart", fail_silently=True)
                cart_item_new.save()
        else:
            cart_item_new = CartItem.objects.create(item=item, cart=cart, quantity=input_quantity)
            messages.info(request, "Product was added to your cart", fail_silently=True)
            cart_item_new.save()
        return redirect("product:detailProduct", id=idItem)


def remove_from_cart(request, idItem, idCart):
    item = get_object_or_404(Variation, product__pk=idItem) #item can xoa
    cart = get_object_or_404(Cart, pk=idCart, user=request.user) #gio hang cua nguoi dung
    cart_item = CartItem.objects.filter(cart=cart, item=item)

    if cart_item.exists():
        for item_in_cart in cart_item:
            if item_in_cart.item.product.pk==item.product.pk:
                if item_in_cart.quantity > 1:
                    item_in_cart.quantity = item_in_cart.quantity - 1
                    item_in_cart.save()
                    messages.info(request, "Product was removed to your cart", fail_silently=True)
                    break
                elif item_in_cart.quantity == 1:
                    CartItem.objects.filter(cart=cart, item=item_in_cart.item).delete()
                    messages.info(request, "Product was removed to your cart", fail_silently=True)
                    break
    return redirect("core:checkout")
