from django.shortcuts import render
from app_two.models import User

# Create your views here.
def index(request):
    return render(request, 'app_two/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'app_two/users.html', context=user_dict)
