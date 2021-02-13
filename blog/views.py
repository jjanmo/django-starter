from django.shortcuts import render
from blog.models import Cafe


def list(request):
    context = {
        'cafes': Cafe.objects.all()
    }
    return render(request, 'blog/list.html', context)
