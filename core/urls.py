from django.urls import path
from .views import HomeView, CategoryView
from django.conf import settings
from django.conf.urls.static import static
from cart.views import remove_from_cart
from order.views import CheckoutView

app_name = 'core'
urlpatterns = [
    path('homepage/', HomeView.as_view(), name='homepage'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('removeFromCart/<int:idItem> <int:idCart>/', remove_from_cart, name='removeFromCart'),
    path('homepage-Shirt/<int:idCategory>/', CategoryView.as_view(), name='homepage-Shirt'),
    path('homepage-SportWear/<int:idCategory>/', CategoryView.as_view(), name='homepage-SportWear'),
    path('homepage-OutWear/<int:idCategory>/', CategoryView.as_view(), name='homepage-OutWear'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
