from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class SignUpForm(forms.Form):
    email = forms.EmailField(
        error_messages = {
            'required':'이메일을 입력하세요.'
        },
        max_length = 64,
        label = '이메일'
    )
    password = forms.CharField(
        error_messages = {
            'required':'비밀번호를 입력하세요.'
        },
        widget = forms.PasswordInput,
        label = '비밀번호'
    )
    re_password = forms.CharField(
        error_messages = {
            'required':'같은 비밀번호를 입력하세요.'
        },
        widget = forms.PasswordInput,
        label = '비밀번호 확인'
    )
    # level = forms.ChoiceField(
    #     choices = (
    #         ('user','고객'),
    #         ('admin','관리자')
    #     ),
    #     widget=forms.Select(),
    #     label = '등급'
    # )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if email and password and re_password:
            if password != re_password:
                self.add_error('password','비민번호가 서로 다릅니다.')
                self.add_error('re_password','비민번호가 서로 다릅니다.')

class SignInForm(forms.Form):
    email = forms.EmailField(
        error_messages = {
            'required':'이메일을 입력하세요.'
        },
        max_length = 64,
        label = '이메일'
    )
    password = forms.CharField(
        error_messages = {
            'required':'비밀번호를 입력하세요.'
        },
        widget = forms.PasswordInput,
        label = '비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email = email)
                if not check_password(password,user.password):
                    self.add_error('password','비밀번호가 다릅니다.')
            except User.DoseNotExist:
                self.add_error('email','가입된 이메일이 없습니다.')