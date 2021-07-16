from django import forms
from .models import Product
from user.models import User

class Product_Register(forms.Form):
    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request

    name = forms.CharField(
        error_messages = {
            'required':'상품명을 입력하세요.'
        },max_length=256,
        label = "상품명"
    )
    price = forms.IntegerField(
        error_messages = {
            'required':'가격을 입력하세요.'
        },
        label = "가격"
    )
    stock = forms.IntegerField(
        error_messages = {
            'required':'수량을 입력하세요.'
        },
        label = '수량'
    )
    info = forms.CharField(
        widget=forms.Textarea,
        label = "상품설명",
        required = False,
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        stock = cleaned_data.get('stock')
        info = cleaned_data.get('info')

        # if not name:
        #     self.add_error('name','상품명을 입력하세요.')
        # if not price:
        #     self.add_error('price','상품가격을 입력하세요.')
        # if not stock:
        #     self.add_error('stock','수량을 입력하세요.')
            