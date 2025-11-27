from django.contrib import admin
from .models import SevaActivity

@admin.register(SevaActivity)
class SevaActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_number')
    list_editable = ('order_number',)
