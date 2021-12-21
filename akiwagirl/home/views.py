from django.shortcuts import render

# Create your views here.

def index(request):
    num = 12
    crowdedness = "快適"
    if num > 10:
        crowdedness = "やや快適"
    dist = {
        'num': num,
        'crowdedness': crowdedness,
    }
    return render(request, 'home/index.html', dist)