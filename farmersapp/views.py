from django.shortcuts import render, redirect, reverse
from .forms import UserForm, CategoryForm,LoginForm, IncomeForm, ExpenseForm, AreaForm, LivestockForm, \
    EquipmentForm
import logging
from .models import Users, Category, Income, Expense, Area, Livestock, Equipment, Login, Weather, Task
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from urllib.parse import urlparse


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file = logging.FileHandler('logfile.log')
logger.addHandler(log_file)




def init(request):
    # if not remember_me:
    # # set session expiry to 0 seconds. So   it will automatically close the session after the browser is closed.
    #     self.request.session.set_expiry(0)

    #     # Set session as modified to force data updates/cookie to be saved.
    #     self.request.session.modified = True
    return render(request, 'accounts/login.html')


@login_required  
def home(request):
    return render(request, 'farmersapp/index.html',
                  {"icon": Update_weather.icon, 
                   'summary': Update_weather.precipitation, 
                  'temperature': Update_weather.temperature,
                  'name': Update_weather.name,
                  'precipitation': Update_weather.precipitation,
                  'polygon_area': polygon_area(),
                  })

@login_required
def get_users(request):
    logger.info('Getting all users started')
    if request.method == 'GET':
        all_users = Users.objects.all()
        return render(request, 'farmersapp/users.html', {'users': all_users})
     
     
# @login_required
# def my_areas(request):
#     logger.info('Getting all areas started')
#     if request.method == 'GET':
#         all_areas = Area.objects.all()
#         return render(request, 'farmersapp/areas/my_areas.html', {'areas': all_areas})

#     else:
#         logger.info('Getting all areas else block started')
#         form = AreaForm()
#     return render(request, 'farmersapp/areas/area_form.html', {'form': form})
@login_required
def my_areas(request):
    logger.info('Getting areas for current user started')
    if request.method == 'GET':
        current_user_areas = Area.objects.filter(user=request.user)
        return render(request, 'farmersapp/areas/my_areas.html', {'areas': current_user_areas})
    else:
        form = AreaForm()
        return render(request, 'farmersapp/areas/area_form.html', {'form': form})

@login_required
def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        logger.info('Creating a new area started')
        logger.info(form.errors)
        if form.is_valid():
            logger.info('Area Form is valid')
            area = form.save(commit=False)
            area.user = request.user  # Set the user field before saving
            area.save()
            messages.success(request, 'Fields added successfully')
            next_url = request.POST.get('next', '/')
            if next_url: 
                return HttpResponseRedirect(next_url)  
            else:
                return redirect('profile:my_areas')
        else:
            logger.error('Form is not valid')
    else:
        form = AreaForm()
    return render(request, 'farmersapp/areas/area_form.html', {'form': form})

# def create_area(request):
#     if request.method == 'POST':
#         form = AreaForm(request.POST)
#         if form.is_valid():
#             area = form.save(commit=False)
#             category_name = request.POST.get('category_name')
#             if category_name:
#                 category = form.create_category(category_name)
#                 area.category = category
#             area.save()
#             return redirect('area_detail', pk=area.pk)
#     else:
#         form = AreaForm()
#     return render(request, 'farmersapp/areas/area_form.html', {'form': form})

#     # return render(request, 'create_area.html', {'form': form})
@login_required
def area_edit(request, id):
    area = Area.objects.get(id=id)
    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('profile:my_areas')
    else:
        form = AreaForm(instance=area)
    return render(request, 'farmersapp/areas/edit_area.html', {'form': form})

def delete_area(request, id):
    area = Area.objects.get(id=id)
    if request.method == 'POST':
        area.delete()
        return redirect('profile:my_areas')
    return render(request, 'farmersapp/areas/my_areas.html', {'area': area})




@login_required
def categories(request):
    if request.method == 'GET':

        all_categories = Category.objects.filter(user=request.user)
        return render(request, 'farmersapp/category/categories.html', {'categories': all_categories})
    else:
        form = CategoryForm()
    return render(request, 'farmersapp/category/category_form.html', {'form': form})

def create_category(request):
    # referring_page = request.META.get('HTTP_REFERER', '/')
    # print(referring_page, 321)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            form.save()
            # messages.success(request, 'category created successfully')
            # next = request.POST.get('next', '/')
            # return HttpResponseRedirect(next)
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            next = request.GET.get('next', '/')
            nextt = next
            return HttpResponseRedirect(nextt)
            next_url = request.POST.get('next', '/')
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect('profile:home')

        else:
            logger.error('Form is not valid')
    else:
        form = CategoryForm()
        # if 'next' in request.GET:
        #     return redirect(request.GET['next'])
        # else:
        #     return redirect('profile:home')
    return render(request, 'farmersapp/category/category_form.html', {'form': form})


def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('profile:categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'farmersapp/category/edit_cat.html', {'form': form})

def delete_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('profile:categories')
    return render(request, 'farmersapp/category/categories.html', {'category': category})



def equipments(request):
    if request.method == 'GET':
        all_equipments = Equipment.objects.all()
        return render(request, 'farmersapp/equipment/equipment.html', {'equipments': all_equipments})
    else:
        form = EquipmentForm()
    return render(request, 'farmersapp/equipment/equipment.html', {'form': form})


@login_required
def create_equipment(request):
    # https://openweathermap.org/api/geocoding-api
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.user = request.user
            equipment.save()
            messages.success(request, 'category created successfully')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
            # return redirect('profile:equipment')
    else:
        form = EquipmentForm()
    return render(request, 'farmersapp/equipment/equipment_form.html', {'form': form})
    
def edit_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('profile:equipments')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'farmersapp/equipment/edit_equipment.html', {'form': form})

def delete_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('profile:equipments')
    return render(request, 'farmersapp/equipment/equipments.html', {'equipment': equipment})


def create_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile:incomes')
    else:
        form = IncomeForm()
    return render(request, 'farmersapp/income_form.html', {'form': form})

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile:expenses')
    else:
        form = ExpenseForm()
    return render(request, 'farmersapp/expense_form.html', {'form': form})


def create_livestock(request):
    if request.method == 'POST':
        form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile:livestocks')
    else:
        form = LivestockForm()
    return render(request, 'farmersapp/livestock_form.html', {'form': form})

def get_lat_lng(city_name):
    # https://openweathermap.org/api/geocoding-api
    API_KEY = 'cab5bb60507cace9c1291861909cf334'
    city_name = city_name
    limit = 1
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_KEY}')
    data = response.json()
    return data[0]['lon'], data[0]['lat'], data[0]['name']

class Update_weather:
    API_KEY = 'b5fc99d5de9b9472ce9bd0f9a7a533db'
    lat, lon, name =  get_lat_lng('zaqatala')
    lang = 'az'
    
    response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}&lang={lang}')

    data = response.json()
    
    summary = data["daily"][-1]['summary']
    temperature = round(data['current']['temp'] - 273.15, 1)
    icon = data['current']['weather'][0]['icon']
    precipitation = data['current']['weather'][0]['description']
    name = name
    
    weather = Weather(temperature=temperature, precipitation=precipitation, summary=summary, icon=icon)
    weather.save()


def polygon_area():
    pass
    # # https://agromonitoring.com/api/polygons
    # API_KEY = 'c9a1406871da26c6df3bb34ed774b1e9'
    # responce = requests.post('https://api.agromonitoring.com/agro/1.0/polygons?appid=API_KEY')
    # data = responce.json()
    # logger.info(data)