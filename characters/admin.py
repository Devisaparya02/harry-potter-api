from django.contrib import admin

from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'house', 'role', 'wand', 'patronus')
    list_filter = ('house', 'role')
    search_fields = ('name',)

admin.site.register(Character, CharacterAdmin)