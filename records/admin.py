from django.contrib import admin
from .models import (
    Mechanical_Dept,
    Electrical_Dept,
    Civil_Dept,
    Computer_Science_Dept,
    Comp_Engr_Dept,
    Pharmaceutical_Tech_Dept,
    Science_Lab_Tech_Dept,
    Food_Tech_Dept,
    Dispensary_and_Opticiary_Dept,
    Agric_Engr_Dept
)

# Register your models here.
class MechAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Mechanical_Dept, MechAdmin)

class ElectAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Electrical_Dept, ElectAdmin)

class CivilAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Civil_Dept, CivilAdmin)

class CompscienceAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Computer_Science_Dept, CompscienceAdmin)

class CompengrAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Comp_Engr_Dept, CompengrAdmin)

class PharmAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Pharmaceutical_Tech_Dept, PharmAdmin)

class SciencelabAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Science_Lab_Tech_Dept, SciencelabAdmin)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Food_Tech_Dept, FoodAdmin)

class DispenseAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Dispensary_and_Opticiary_Dept, DispenseAdmin)

class AgricAdmin(admin.ModelAdmin):
    list_display = ('name_of_students','amount','balance','total')
admin.site.register(Agric_Engr_Dept, AgricAdmin)