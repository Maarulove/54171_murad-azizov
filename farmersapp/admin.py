from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Users)
class AdminUser(admin.ModelAdmin):
    list_display = ['name','surname', 'email', 'phone', 'create_date']
    list_per_page = 100

    fieldsets = [
        ('personal info',{
            'fields': ["name", 'surname'],
            'description': 'Information  about Author',
            'classes': ['wide']

        }),(
            'Contact',{
                'fields': ["email"],
                'classes': ['collapse']   
            }
        )

    ]    

@admin.register(Area)
class AdminArea(admin.ModelAdmin):
    list_display = ['name', 'square', "user"]
    list_per_page = 20
    # fieldsets = [
    #     ('personal info',{
    #         'fields': ['create_date', 'description', 'update_date'],
    #         'description': 'Information  about Author',
    #         'classes': ['collapse']

    #     }),
    #     ('More', {
    #         'fields': ['name', 'surname', 'birth_date', 'biography']
            
    #     }),(
    #         'Contact',{
    #             'fields': ["email"],
    #             'classes': ['collapse']   
    #         }
    #     )

    # ]    


@admin.register(Expense)
class AdminExpence(admin.ModelAdmin):
    list_display = ["user", 'description', 'amount', 'create_date',]
@admin.register(Income)
class AdminIncome(admin.ModelAdmin):
    list_display = ["user", 'description', 'amount', 'create_date',]

@admin.register(Equipment)
class AdminEquipment(admin.ModelAdmin):
    list_display = ["user",  'description', 'create_date', 'update_date']


# @admin.register(CategoryEquipment)
# class AdminCategoryEquipment(admin.ModelAdmin):
#     list_display = ['name',  'description']

@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Livestock._meta.fields]

# @admin.register(CategoryLivestock)
# class CategoryLivestockAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in CategoryLivestock._meta.fields]

@admin.register(ExpenceCategory)
class CategoryLivestockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExpenceCategory._meta.fields]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


    