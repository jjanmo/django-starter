from django.shortcuts import render


def list(request):
    context = {}
    return render(request, 'blog/list.html', context)
