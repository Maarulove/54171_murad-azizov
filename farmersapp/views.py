from django.shortcuts import render, HttpResponse
from .models import Users, Equipment, Expense, Income
# Create your views here.



def init(request):
    return render(request, 'farmersapp/index.html')

