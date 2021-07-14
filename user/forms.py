from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class SignUpForm(forms.Form):
    email = forms.EmailField(
        error_messages = {
            'required':'이메일을 입력하세요.'
        },
        label = "이메일",
    )
    password = forms.CharField(
        error_messages = {
            'required':'비밀번호를 입력하세요.'
        },
        widget = forms.PasswordInput,
        label = "비밀번호",
    )
    re_password = forms.CharField(
        error_messages = {
            'required':'비밀번호를 입력하세요.'
        },
        widget = forms.PasswordInput,
        label = "비밀번호 확인",
    )
    level = forms.ChoiceField(
        error_messages = {
            'required':'등급을 선택하세요.'
        },
        choices = (
            # (실제 값, 보여지는 값)
            ("admin","관리자"),
            ("user","고객"),
        ),
        # 초기값 설정
        initial = "user",
        label = "등급",
    )
    # level = forms.CharField(
    #     widget=forms.Select(choices=(
            # ("admin","관리자"),
            # ("user","고객"),
        # )),
    # )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        level = cleaned_data.get('level')

        # 두 값이 있는지 확인 후 값이 같은지 확인
        if password and re_password:
            if password != re_password:
                self.add_error('password','비밀번호가 다릅니다.')
                self.add_error('re_password','비밀번호가 다릅니다.')

class SignInForm(forms.Form):
    email = forms.EmailField(
        error_messages = {
            'required':'이메일을 입력하세요.'
        },
        label = "이메일",
    )
    password = forms.CharField(
        error_messages = {
            'required':'비밀번호를 입력하세요.'
        },
        widget = forms.PasswordInput,
        label = "비밀번호",
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)

            if not check_password(password,user.password):
                self.add_error('password','비밀번호가 다릅니다.')
        
        except Fcuser.DoesNotExist:
            self.add_error("email","아이디가 존재하지 않습니다.")