from django.shortcuts import render
from blog.models import Cafe
from django.core.paginator import Paginator


def list(request):
    cafes = Cafe.objects.all()
    paginator = Paginator(cafes, 5)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    print('items', items)
    context = {
        'cafes': items
    }
    return render(request, 'blog/list.html', context)
