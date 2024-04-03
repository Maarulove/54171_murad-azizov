from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import logging
from PIL import Image


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self) -> str:   
        return f"{self.user.username}"
        
    def __repr__(self) -> str:
        return self.__str__()   
    
    def save(self, *args, **kwargs):
        super().save()
    
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


    
class Farm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField(help_text="Size of the farm in acres")
    established_date = models.DateField()

    def __str__(self):
        return self.name

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

    
class Category(models.Model):
    def_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    # url = models.CharField("The URL", max_length=40)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.def_name

    def __repr__(self):
        return self.__str__()

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Expense {self.id}"
    

class Area(models.Model):
    user = models.ForeignKey(User, related_name='area', on_delete=models.CASCADE)
    name = models.CharField(max_length=150) 
    description = models.TextField(blank=True, null=True)
    square = models.FloatField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name
            
    
    def add_expense(self, amount, description=''):
        # Assuming Expense is your Expense model
        expense = Expense.objects.create(
            user=self.user,
            amount=amount,
            description=description,
        )
        return expense
    
    
class AreaExpences(Expense):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class AreaIncome(Income):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)



class Livestock(models.Model):
    LIVESTOCK_CATEGORY_CHOICES = (
    (1, "Cattle"),
    (2, "Sheep"),
    (3, "Pigs"),
    (4, "Goats"),
    (5, "Chickens"),
    (6, "Ducks"),
    (7, "Turkeys"),
    (8, "Horses"),
    (9, "Rabbits"),
    (10, "Bees"),
    # Add more categories as needed
    )
    
    name = models.CharField(max_length=100)
    categories = models.CharField(max_length=100, choices=LIVESTOCK_CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    money_spent = models.DecimalField(default=0, max_digits=30, decimal_places=2)

class LivestockExpence(Expense):
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)

class LivestockIncome(Income):
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)


class Equipment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='dsa')  # Assuming Users is defined elsewhere
    categories = models.ManyToManyField(Category, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
class EquipmentExpences(Expense):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
class EquipmentIncome(Income):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class Task(models.Model):
    description = models.TextField()
    due_date = models.DateField()
    
    status = models.CharField(max_length=20)


class Weather(models.Model):
    date = models.DateField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.TextField()
    summary = models.TextField()
    icon = models.ImageField(upload_to='../static/farmersapp/images', blank=True, null=True)

    def __str__(self):
        return f"Weather: {self.date}, tempreature: {self.temperature} C {self.icon}, precipitation: {self.precipitation}mm \nsummary: {self.summary}" 
