from django.contrib import admin
from userauths.models import User

# Register your models here.
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username' , 'email']
    

admin.site.register(User, UserCustomAdmin)
