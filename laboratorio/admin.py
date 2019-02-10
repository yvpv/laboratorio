from django.contrib import admin

from .models  import  Laboratorio
# Register your models here.

admin.site.register(Laboratorio)

class VillainAdmin(admin.ModelAdmin):
    
    change_form_template = "laboratorio/laboratorio_changed_form.html"