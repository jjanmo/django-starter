from django.shortcuts import render
from django.http import HttpResponseRedirect
from model_app.models import Post
from .forms import PostForm


def print_list(request):
    context = {
        'list': Post.objects.all()
    }
    return render(request, 'model_app/list.html', context)


# def create_form(request):
#     form = PostForm()
#     return render(request, 'model_app/form.html', {'form': form})


# def confirm(request):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         return render(request, 'model_app/confirm.html', {'form': form})
#     return HttpResponseRedirect('/model_app/form/')


def form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/model_app/list/')

    form = PostForm()
    return render(request, 'model_app/form.html', {'form': form})
