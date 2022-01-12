from django.shortcuts import render

# Create your views here.
from num.models import Current
from seat.models import Occupancy
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
    seatnum = Occupancy.objects.filter(occupancy=1).count()
    dist = {
        'num': num,
        'crowdedness': crowdedness,
        'seatnum': seatnum
    }
    return render(request, 'home/index.html', dist)
