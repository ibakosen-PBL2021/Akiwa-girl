from django.shortcuts import render
from .models import Occupancy
# Create your views here.
def index(request):
    occupancy = Occupancy.objects.order_by('id')
    seats = Occupancy.objects.filter(occupancy=1).count()
    return render(request, 'seat/index.html', {'occupancy': occupancy, 'num':seats})
