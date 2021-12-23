from django.shortcuts import render
from .models import Current
# Create your views here.
def index(request):
    num = Current.objects.get().num
    if num > 20:
        crowdedness = "混雑"
    elif num > 15:
        crowdedness = "やや混雑"
    elif num > 10:
        crowdedness = "やや快適"
    else:
        crowdedness = "快適"
    dist = {
        'num': num,
        'crowdedness': crowdedness,
    }
    return render(request, 'num/index.html', dist)