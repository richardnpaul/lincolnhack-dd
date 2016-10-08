from django.contrib import admin
from .models import MP

class MPAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'photo']

admin.site.register(MP, MPAdmin)