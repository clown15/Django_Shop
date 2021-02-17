from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .forms import RegisterForm
from fcuser.decorators import login_required
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction

# Create your views here.

@method_decorator(login_required,name="dispatch")
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    
    # 주문 성공시
    def form_valid(self,form):
        # db와 동시 처리를 위함
        # ex) 재고 관리
        with transaction.atomic():
            product=Product.objects.get(pk=form.data.get("product"))
            order = Order(
                quantity = form.data.get("quantity"),
                product = product,
                fcuser = Fcuser.objects.get(email=self.request.session.get("user"))
            )
            order.save()
            product.stock -= int(form.data.get("quantity"))
            product.save()

        return super().form_valid(form)

    # 주문 실패시
    def form_invalid(self,form):
        return redirect('/product/'+str(form.product))

    def get_form_kwargs(self,**kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            "request":self.request,
        })
        return kw

# decorator호출
# class view로 접근시 dispatch함수 호출
# 원칙은 decorator사용시 method에 사용해야 하나 아래 방식처럼 하면 클래스에 사용가능
# from django.utils.decorators import method_decorator를 통해 사용가능
# @method_decorator(decorator_name,method_name)
# 어떤 method 에 어떤 decorator를 적용할지 작성
# 일반적으로 사용할시 
# @login_required
# def dispatch(request,*args,**kwargs)
# 이런식으로 사용가능
@method_decorator(login_required,name="dispatch")
class OrderList(ListView):
    template_name="order.html"
    context_object_name="order_list"

    def get_queryset(self,**kwargs):
        queryset=Order.objects.filter(fcuser__email=self.request.session.get('user'))

        return queryset