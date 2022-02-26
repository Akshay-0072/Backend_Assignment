from django.contrib import admin
from accounts.models import User

# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'company_name', 'age', 'city', 'state', 'zip', 'email', 'web']