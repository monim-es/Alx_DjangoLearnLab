from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'followers')
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
