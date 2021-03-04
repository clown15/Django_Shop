from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView
from .forms import CreateForm
from .models import Product
from user.models import User
# Create your views here.

class Product_List(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'product_list'

class Product_Detail(DetailView):
    template_name = 'detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

class Product_Create(FormView):
    template_name = 'create.html'
    form_class = CreateForm
    success_url = '/product'

    def form_valid(self,form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            stock = form.data.get('stock'),
            info = form.data.get('info'),
            creator = User.objects.get(email=self.request.session.get("user")),
        )
        product.save()

        return super().form_valid(form)