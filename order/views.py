from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm,CancelForm
from user.models import User
from django.utils.decorators import method_decorator
from user.decorators import login_required
from .models import Order
from product.models import Product
from django.db import transaction,IntegrityError
from django.contrib import messages

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

    # 값이 성공적으로 들어오면 실행되는 함수
    def form_valid(self,form):
        product = form.product
        quantity = int(form.data.get('quantity'))

        if product.stock < quantity:
            form.add_error('quantity','남은 수량보다 많이 주문할 수 없습니다.')
            
            return render(self.request, 'detail.html', {'form': form, 'product':product})
            # return redirect('/product/'+str(product.id))
        
        else:
            with transaction.atomic():
                
                order = Order(
                    quantity = quantity,
                    product = product,
                    orderer = User.objects.get(email=self.request.session.get('user')),
                    total_price = product.price * quantity,
                )

                order.save()
                product.stock -= quantity
                product.save()
            
        return super().form_valid(form)

    # 값이 제대로 안들어 왔을때
    def form_invalid(self,form):
        return render(self.request, 'detail.html', {'form': form, 'product':form.product})

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

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CancelForm()
        
        return context

@method_decorator(login_required,name="dispatch")
class OrderCancel(FormView):
    form_class = CancelForm
    success_url = '/order'

    def form_valid(self,form):
        with transaction.atomic():    
            order = Order.objects.get(pk=form.data.get('cancel'))
            product = Product.objects.get(pk=order.product.id)
            
            order.delete()
            product.stock += order.quantity
            product.save()

        return redirect('/order/')

    def form_invalid(self,form):
        return redirect('/order/')