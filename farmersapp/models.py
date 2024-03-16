from django.db import models
import logging

class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:   
        return f"{self.name} {self.surname}"
    
    

    
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
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)

class Expense(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Expense {self.id}"
    

class Area(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1 )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    square = models.FloatField()
    categories = models.ManyToManyField(Category, blank=True)
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
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Assuming Users is defined elsewhere
    description = models.TextField(blank=True, null=True)  # Null is more appropriate for TextField default
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
class EquipmentExpences(Expense):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
class EquipmentIncome(Income):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)


