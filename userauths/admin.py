from django.contrib import admin
from userauths.models import User, Profile

# تخصيص واجهة إدارة المستخدمين
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('user_permissions',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'verified']
    list_editable = ['verified']
    search_fields = ['user__username', 'phone', 'address']
    list_filter = ['verified']
    ordering = ['user']

admin.site.register(User, UserCustomAdmin)
admin.site.register(Profile, ProfileAdmin)
