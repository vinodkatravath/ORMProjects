from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg, Sum, Max, Min, Count
from MyApps1.models import Employee

# Create your views here.
def display_view(request):
    avg1=Employee.objects.all().aggregate(Avg('sal'))
    max = Employee.objects.all().aggregate(Max('sal'))
    min = Employee.objects.all().aggregate(Min('sal'))
    sum = Employee.objects.all().aggregate(Sum('sal'))
    count = Employee.objects.all().aggregate(Count('sal'))
    my_dict = {'avg1': avg1, 'max': max, 'min': min, 'sum': sum, 'count': count}
    return render(request, 'MyApps1/aggregate.html',my_dict)