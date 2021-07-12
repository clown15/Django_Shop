from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from user.models import User
from django.utils.decorators import method_decorator
from user.decorators import login_required
from .models import Order

# Create your views here.

@method_decorator(login_required,name="dispatch")
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product'

    # form을 생성할때 사용할 인자값을 정하는? 함수
    def get_form_kwargs(self,**kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            "request":self.request,
        })
        return kw

    # 주문 실패시
    def form_invalid(self,form):
        return redirect('/product/'+str(form.product))

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
    template_name="order_list.html"
    context_object_name="order_list"

    def get_queryset(self,**kwargs):
        queryset=Order.objects.filter(orderer=self.request.session.get('user')).order_by('pk')

        return queryset