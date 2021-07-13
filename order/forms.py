from django import forms
from .models import Order
from user.models import User
from product.models import Product
from django.db import transaction,IntegrityError

class RegisterForm(forms.Form):
    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages = {
            'required':'수량을 입력하세요.'
        },label = '수량'
    )
    product = forms.IntegerField(
        label = '상품',
        widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = User.objects.get(email=self.request.session.get('user'))

        product = Product.objects.get(pk=product)
        
        if quantity and product and user:
            try:
                with transaction.atomic():
                    order = Order(
                        quantity = quantity,
                        product = product,
                        orderer = user,
                        total_price = product.price * quantity,
                    )

                    order.save()
                    product.stock -= quantity
                    product.save()
            except IntegrityError:
                # views.py 에서 product값을 사용해 redirect하기위함
                self.product = product.id
                self.add_error('quantity','남은 수량보다 많이 주문할 수 없습니다.')
        else:
            self.product = product.id
            self.add_error('quantity','수량이 입력되지 않았습니다.')

        