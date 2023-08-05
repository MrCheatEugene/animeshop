"""animeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from animeshop.pages.index import index
from animeshop.pages.cart import cart
from animeshop.pages.category import category
from animeshop.pages.order import order
from animeshop.api.price import price
from animeshop.api.name import name
from animeshop.api.checkmember import checkmember
from animeshop.api.membership import membership
from django.urls import path

urlpatterns = [
    path('',  index, name="Home"),
    path('cart',  cart, name="Cart"),
    path('order',  order, name="Order"),
    path('api/price/<item>',  price),
    path('api/name/<item>',  name),
    path('api/membership/<card>',  membership),
    path('api/checkmember/<card>',  checkmember),
    path('c/<cid>',  category, name="Category"),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
