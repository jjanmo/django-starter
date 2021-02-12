# from django import forms
#
#
# class PostForm(forms.Form):
#     title = forms.CharField(label="제목", max_length=20)
#     content = forms.CharField(label="내용", widget=forms.Textarea)

from django.forms import ModelForm
from model_app.models import Post
from django.utils.translation import gettext_lazy as _  # django 다국어 지원 관련


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용')
        }
        help_texts = {
            'title': _('제목을 입력해주세요'),
            'content': _('내용을 입력해주세요')
        }
        error_messages = {
            'name': {
                'max_length': _('제목을 20자 이내로 작성해주세요')
            }
        }
