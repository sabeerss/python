from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # return HttpResponse('Hello test')
    webpages = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages}
    # my_dic = {'insert_me': 'hello! i am from views.py!'}
    return render(request, 'app_one/index.html', context = date_dict)
