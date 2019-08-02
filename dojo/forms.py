from django import forms
from django.forms import models


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')



class PostForm(forms.Form):
    #입력 폼 값 검증 : validators
    #validators에 함수이름을 넣는다. 함수를 호출하는 것이 아니다.
    title = forms.CharField(validators=[min_length_3_validator])
    #widget을 지정해주면 입력을 여러줄 할 수 있다.
    content = forms.CharField(widget=forms.Textarea)

