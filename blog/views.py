from django.shortcuts import render, get_object_or_404
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


def update(request):
    if request.method == 'POST':
        print(request.POST.get('id'))
        # updating_item = Cafe.objects.get(pk=request.POST.get('id'))
        updating_item = get_object_or_404(Cafe, pk=request.POST.get('id'))
        form = PostForm(request.POST, instance=updating_item)  # instance를 넣어주면 해당 아이템를 폼에 업데이트 하게 된다
        if form.is_valid():
            updated_item = form.save()
    elif request.method == 'GET':
        # updating_item = Cafe.objects.get(pk=request.GET.get('id'))
        updating_item = get_object_or_404(Cafe, pk=request.GET.get('id'))
        form = PostForm(instance=updating_item)
        return render(request, 'blog/update.html', {'form': form})

    return HttpResponseRedirect('/blog/list/')


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Cafe, pk=request.GET.get('id'))
        context = {
            'cafe': item
        }
        return render(request, 'blog/detail.html', context)
    return HttpResponseRedirect('/blog/list')
