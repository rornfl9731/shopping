from django import forms
from .models import Order
from product.models import Product
from user.models import Suser
from django.db import transaction
from product.models import Product
from user.models import Suser


class RegisterForm(forms.Form):
    # 세션을 이용하려고 한건데 정확히 이해는 못했어
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if not (quantity and product):
            self.add_error('quantity', 'no quantit')
            self.add_error('product', 'no quantit')




