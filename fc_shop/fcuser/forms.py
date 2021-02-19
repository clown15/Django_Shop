from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages = {
            'required':"이메일을 입력하세요."
        },
        max_length=64,
        label="이메일"
    )
    password = forms.CharField(
        error_messages = {
            'required':"비밀번호 입력"
        },
        widget=forms.PasswordInput,
        label="비밀번호"
    )
    re_password = forms.CharField(
        error_messages = {
            'required':"비밀번호 입력"
        },
        widget=forms.PasswordInput,
        label="비밀번호 확인"
    )

    level = forms.ChoiceField(
        choices=(
            ("user","고객"),
            ("admin","관리자")
        ),
        required=True,
        label="등급"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")
        level = cleaned_data.get("level")

        try:
            fcuser = Fcuser.objects.get(email=email)
            self.add_error("email","이미 가입된 이메일 입니다.")
        except Fcuser.DoesNotExist:
            if password and re_password:
                if password != re_password:
                    self.add_error("password","비민번호가 서로 다릅니다.")
                    self.add_error("re_password","비민번호가 서로 다릅니다.")

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages = {
            'required':"이메일을 입력하세요."
        },
        max_length=64,
        label="이메일"
    )
    password = forms.CharField(
        error_messages = {
            'required':"비밀번호 입력"
        },
        widget=forms.PasswordInput,
        label="비밀번호"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)

                if not check_password(password ,fcuser.password):
                    self.add_error("password","비밀번호가 틀립나디.")
            except Fcuser.DoesNotExist:
                self.add_error("email","아이디가 존재하지 않습니다.")