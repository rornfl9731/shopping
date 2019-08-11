from django import forms
from django.contrib.auth.hashers import check_password,make_password
from .models import Suser


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required':'비번을 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'

    )
    re_password = forms.CharField(
        error_messages={
            'required':'비번을 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'

    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('re_password','비밀번호가 다릅니다.')
            else:
                user = Suser(
                    email = email,
                    password = make_password(password)
                )
                user.save()


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required':'비번을 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'

    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = Suser.objects.get(email=email)
            except Suser.DoesNotExist:
                self.add_error('email','아이디가 없습니다.')
                return

            if not check_password(password,user.password):
                self.add_error('password','비밀번호가 틀렸습니다')
            else:
                self.email = user.email



