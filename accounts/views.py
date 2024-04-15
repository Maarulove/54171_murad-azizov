from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UserCreationForm, SignUpForm, UserForm
import logging
from django.contrib.auth import login as auth_login_user
from django.core.mail import send_mail
from django.conf import settings
from farmersapp.models import Users

import logging
logging.basicConfig(filename='logfile.log', level=logging.INFO)
logger = logging.getLogger(__name__)




# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# # Create a file handler and set its level and formatter
# log_file = logging.FileHandler("logfile.log")
# log_file.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# log_file.setFormatter(formatter)

# # Add the file handler to the logger
# logger.addHandler(log_file)



def login_view(request):
    if request.method == 'POST':
        logger.info("Login view is called.")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        logger.info(user)
        if user is not None:
            logger.info("User is authenticated.")
            return redirect(reverse('profile:home'))
        else:
            logger.error("User is not authenticated.15")
            messages.error(request, 'Invalid username or password.')
    else:
        logger.error("User .18")
        logger.info("d.2 else get request.")

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')

    return redirect('login')  
                                   
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Users.objects.create(user=user, phone=form.cleaned_data['phone'])
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})