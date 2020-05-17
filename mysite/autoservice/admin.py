from django.contrib import admin
from .models import Paslauga, Paslaugos_kaina, Automobilis, Uzsakymas, UzsakymoEilute

# Register your models here.

class UzsakymoEiluteInLine(admin.TabularInline):
    model = UzsakymoEilute

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilis_id', 'suma')
    inlines = [UzsakymoEiluteInLine]

admin.site.register(Paslauga)
admin.site.register(Paslaugos_kaina)
admin.site.register(Automobilis)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)