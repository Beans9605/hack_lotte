from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    '''이미지 모델을 위한 폼'''
    class Meta:
        model = Image
        fields = ('title', 'image')
