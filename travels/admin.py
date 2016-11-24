from django.contrib import admin
from .models import Travel

@admin.register(Travel)
class AdminTravel(admin.ModelAdmin):
	list_display = ('name', 'price',)
	list_filter = ('price',)