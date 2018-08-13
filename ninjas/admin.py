from django.contrib import admin
from .models import Nija, NijaImage, HiddenVillages


class NijaImageInline(admin.TabularInline):
    model = NijaImage


class NijaAdmin(admin.ModelAdmin):
    inlines = [
        NijaImageInline
    ]


admin.site.register(Nija, NijaAdmin)
