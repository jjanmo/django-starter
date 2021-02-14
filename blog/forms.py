from django.forms import ModelForm
from blog.models import Cafe
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'address']
        labels = {
            'name': _('카페 이름'),
            'address': _('카페 주소')
        }
        help_texts: {
            'name': _('카페 이름을 입력하세요'),
            'address': _('카페 주소를 입력하세요')
        }
        error_messages: {
            'name': {
                'max_length': _('카페 이름은 최대 20자 이내로 작성해주세요')
            }
        }
