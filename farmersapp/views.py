from django.shortcuts import render, HttpResponse, redirect
from . import models
from . import forms
import logging
# Create your views here.
logger = logging.getLogger(__name__)


def init(request):
    logger.info("Init")
    return render(request, 'farmersapp/index.html')


def get_users(request):
    print(11)
    users = models.Users.objects.all()
    return render(request, 'farmersapp/users.html', {'users': users})

# def get_users(request):
#     logger.info("get users launched")
#     if request.method == "POST":
#         form = forms.UserForm(request.POST)
#         if form.is_valid():
#             return redirect("get_users")

#         return render(request, )