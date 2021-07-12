from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.

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