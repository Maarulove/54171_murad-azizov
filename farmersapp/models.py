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


# class CategoryArea(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     def __str__(self):
#         return self.name
    
class Area(Category):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1 )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    square = models.FloatField()
    # categories = models.ManyToManyField(Category, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name
    




    
# class CategoryLivestock(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
#     def __str__(self):
#         return self.name

class Money_spent(models.Model):
    for_what = models.CharField(max_length = 100, blank=True)
    from_where = models.CharField(max_length = 100, blank=True)
    amount = models.DecimalField(default=0, max_digits=3, decimal_places=2)

class Money_got(models.Model):
    from_where = models.CharField(max_length = 100, blank=True)
    amount = models.DecimalField(default=0, max_digits=3, decimal_places=2)

class Livestock(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, blank=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    money_spent = models.DecimalField(default=0, max_digits=30, decimal_places=2)
# # 
# class CategoryEquipment(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Assuming Users is defined elsewhere
    description = models.TextField(blank=True, null=True)  # Null is more appropriate for TextField default
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class ExpenceCategory(models.Model):
    category = models.ManyToManyField(Category, blank=True)    


class Expense(models.Model):
    EXPENSE_CATEGORIES = [
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('utilities', 'Utilities'),
        # Add more categories as needed
    ]
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    where = models.CharField(max_length=50, choices=EXPENSE_CATEGORIES)
    categories = models.ManyToManyField(Category, blank=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Expense {self.id}"
    
class Income(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
