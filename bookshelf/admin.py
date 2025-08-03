from django.contrib import admin

# Register your models here.
# bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Library

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Library)
