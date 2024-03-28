from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UserCreationForm
import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# log_file = logging.FileHandler("logfile.log")
# log_file.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# log_file.setFormatter(formatter)
# logger.addHandler(log_file)

# Configure the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler and set its level and formatter
log_file = logging.FileHandler("logfile.log")
log_file.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(log_file)



def login_view(request):
    logger.info("login view is called.")

    if request.method == 'POST':
        logger.info("Login view is called.")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            logger.info("User is authenticated.")
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('farmersapp:home'))
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

def signup_view(request):
    logger.info("Signup view is called.")
    if request.method == 'POST':
        logger.info("Signup view is called.")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            logger.info("User creation form is valid.")
            user = form.save()
            login(request, user)
            return redirect('login')  
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')

    return redirect('login')  # Change 'login' to the name of your login URL pattern