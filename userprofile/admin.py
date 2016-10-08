from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mp', 'date_of_birth', 'photo']

admin.site.register(UserProfile, UserProfileAdmin)