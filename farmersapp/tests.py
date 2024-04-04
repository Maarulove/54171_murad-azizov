from django.test import TestCase

# Create your tests here.
from django.db import migrations
from .models import Category

def populate_user_id(apps, schema_editor):
    Category = apps.get_model('myapp', 'Category')
    for category in Category.objects.all():
        # Update user_id field for each category based on your application's logic
        # For example, you might assign a default user or use some other criteria
        category.user_id = 1
        category.save()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '000x_previous_migration'),
    ]

    operations = [
        migrations.RunPython(populate_user_id),
    ]
