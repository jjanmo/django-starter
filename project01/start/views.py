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
    return render(request, 'start/index.html', context)  # 위에 코드를 아래와 같이 쓸 수 있다 : shortcut


def select(request):
    context = {}
    return render(request, 'start/select.html', context)


def result(request):
    numbers = request.GET['numbers']
    if numbers == '':
        selected = []
        while len(selected) < 6:
            tmp = random.randrange(1, 46)
            if tmp in selected:
                continue
            else:
                selected.append(tmp)
    else:
        selected = list(map(int, numbers.split(',')))
    context = {
        "numbers": selected
    }
    return render(request, 'start/result.html', context)
