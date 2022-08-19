from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['area', 'location', 'item', 'price', 'head', 'photo']

        widgets = {
            'location': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 453px; height: 44.5px; margin-top:-11px; margin-left:-15px;',
                'placeholder': '매장 이름을 입력해주세요'
                }),
            'item': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 453px; height: 44.5px; margin-top:-11px; margin-left:-15px;',
                'placeholder': '상품명을 입력해주세요'
            }),
            'price': NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 453px; height: 44.5px; margin-top:-11px; margin-left:-15px;',
                'placeholder': '상품 가격을 입력해주세요'
            }),
            'head': NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 453px; height: 44.5px; margin-top:-11px; margin-left:-15px;',
                'placeholder': '구매 인원을 입력해주세요'
            }),
        }
