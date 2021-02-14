from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Cafe
from django.core.paginator import Paginator
from blog.forms import PostForm


def list(request):
    cafes = Cafe.objects.all().order_by('-created_at')
    paginator = Paginator(cafes, 4)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'cafes': items
    }
    return render(request, 'blog/list.html', context)


def form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/blog/list/')

    form = PostForm()
    return render(request, 'blog/form.html', {'form': form})
