from django.contrib import admin
from userauths.models import User, Profile

# Register your models here.
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username' , 'email']
    search_fields = ['first_name' , 'last_name' , 'username']
    list_filter = ['username']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user' , 'verified']
    list_editable = ['verified']    

admin.site.register(User, UserCustomAdmin)
admin.site.register(Profile, ProfileAdmin)
