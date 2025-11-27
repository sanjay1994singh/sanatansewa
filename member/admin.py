from django.contrib import admin
from .models import Member, Designation


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_number')
    list_editable = ('order_number',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_number')
    list_editable = ('order_number',)
