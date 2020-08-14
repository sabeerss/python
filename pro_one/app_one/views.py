from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello test')
    my_dic = {'insert_me': 'hello! i am from views.py!'}
    return render(request, 'app_one/index.html', context=my_dic)
