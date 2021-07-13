from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import Product_Register
from order.forms import RegisterForm as OrderForm
from django.utils.decorators import method_decorator
from user.decorators import admin_required

# Create your views here.

class productList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"

@method_decorator(admin_required,name="dispatch")
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = Product_Register
    success_url = '/product'

    # Product_Register로 form의 값이 넘어 가기 전에 실행되는 함수로 forms.py 에서 request.session를 사용하기 위함.(이걸 사용하지 않으면 forms.py에서 request를 사용할 수 없음)
    def get_form_kwargs(self,**kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            "request":self.request,
        })
        return kw

class ProductDetail(DetailView):
    template_name = 'detail.html'
    queryset = Product.objects.all()
    # html에서 사용할 변수명
    context_object_name = "product"

    # 생성된 forms.py를 기반으로 생성된 form에 원하는 form을 추가하기위함
    def get_context_data(self,**kwargs):
        # 기본 구현을 호출해 context를 가져온다
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        
        return context