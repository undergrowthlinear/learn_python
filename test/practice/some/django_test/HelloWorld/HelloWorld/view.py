from django.http import HttpRequest
from django.shortcuts import render


class Student():
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['athlete_list'] = [Student('张三'), Student('李四')]
    #request = HttpRequest(request)
    print('request {}'.format(request))
    if request.GET:
        print('request.Get {}'.format(request.GET))
    if request.POST:
        print('request.POST {}'.format(request.POST))
    return render(request, 'hello.html', context)


def hello_ex(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['athlete_list'] = [Student('张三'), Student('李四')]
    return render(request, 'hello_ex.html', context)
