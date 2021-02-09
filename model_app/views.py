from django.shortcuts import render
from model_app.models import Post
from .forms import PostForm


def print_list(request):
    context = {
        'list': Post.objects.all()
    }
    return render(request, 'model_app/list.html', context)


def create_form(request):
    form = PostForm()
    return render(request, 'model_app/form.html', {'form': form})