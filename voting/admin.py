from django.contrib import admin
from .models import Bill, Votes

class BillAdmin(admin.ModelAdmin):
    list_display = ['name', 'result', 'description', 'status']

admin.site.register(Bill, BillAdmin)


class VotesAdmin(admin.ModelAdmin):
    list_display = ['vote', 'bill', 'voter']

admin.site.register(Votes, VotesAdmin)