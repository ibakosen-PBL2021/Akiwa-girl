from django.shortcuts import render
from .models import Current
# Create your views here.
def index(request):
    num = Current.objects.get()
    return render(request, 'num/index.html', {'num':num})