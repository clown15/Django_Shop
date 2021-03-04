from django import forms
from .models import Product

class CreateForm(forms.Form):
    name = forms.CharField(
        error_messages = {
            'required':'상품명을 입력해주세요.',
        },
        max_length = 256,
        label = '상품명'
    )
    price = forms.IntegerField(
        error_messages = {
            'required':'가격을 입력하세요.'
        },
        label = '가격'
    )
    stock = forms.IntegerField(
        error_messages = {
            'required':'수량을 입력하세요.'
        },
        label = '수량'
    )
    info = forms.CharField(
        error_messages = {
            'required':'상품정보를 입력하세요.'
        },
        label = '정보'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('name')
        stock = cleaned_data.get('name')
        info = cleaned_data.get('name')
        