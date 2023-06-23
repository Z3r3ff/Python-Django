from django.urls import path

import cart.views
from .views import ProductView
from cart.views import add_to_cart

app_name = 'product'
urlpatterns = [
    path('detailProduct/<int:id>/', ProductView.as_view(), name='detailProduct'),
    path('addToCart/<int:idItem> <int:idCart>/', cart.views.add_to_cart, name='addToCart'),
]