"""django_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from user.views import index,SignUpView,SignInView
from product.views import productList,ProductRegister,ProductDetail
from order.views import OrderCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('signup/',SignUpView.as_view()),
    path('signin/',SignInView.as_view()),
    path('product/',productList.as_view()),
    path('product/register/',ProductRegister.as_view()),
    path('product/<int:pk>/',ProductDetail.as_view()),
    path('order/create/',OrderCreate.as_view()),
]
