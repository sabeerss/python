from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<em>test</em>")


def help(request):
    help_dict = {'help_insert': 'help page from views!'}
    return render(request, 'app_two/help.html', context=help_dict)
