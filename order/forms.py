from django import forms

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
        
        if not quantity:
            # views.py 에서 product값을 사용해 redirect하기위함
            self.product = product
            self.add_error('quantity','수량이 입력되지 않았습니다.')

        