from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Users)
class AdminUser(admin.ModelAdmin):
    list_display = ['user', 'phone']
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
    list_display = ['name', 'square']
    list_per_page = 20

    
    # Define custom action for adding expense
    def add_expense_action(self, request, queryset):
        for area in queryset:
            # Add expense for each selected area
            area.add_expense(amount=100,  description='Expense added via admin')

    add_expense_action.short_description = "Add Expense"

    # Register the custom action
    actions = [add_expense_action]

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

@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Livestock._meta.fields]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


@admin.register(AreaExpences)
class AreaExpencesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AreaExpences._meta.fields]

@admin.register(EquipmentExpences)
class EqipmentExpencesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EquipmentExpences._meta.fields]

@admin.register(LivestockExpence)
class LiveStockExpencesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LivestockExpence._meta.fields]


@admin.register(AreaIncome)
class AreaIncomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AreaIncome._meta.fields]
    # Add more categories as needed

@admin.register(LivestockIncome)
class LivestockIncomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LivestockIncome._meta.fields]
    # Add more categories as needed

@admin.register(EquipmentIncome)
class EquipmentIncomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EquipmentIncome._meta.fields]
    # Add more categories as needed


