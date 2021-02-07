from django.shortcuts import render
from datetime import datetime
import random


def index(request):
    # template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)  # 위에 코드를 아래와 같이 쓸 수 있다 : shortcut


def select(request):
    number = random.randrange(1, 11)
    context = {
        'number': number
    }
    return render(request, 'select.html', context)


def result(request):
    context = {
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, 'result.html', context)
