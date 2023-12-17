from django.contrib import admin
from .models import *


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'creation_date')
    list_display_links = ('id', 'user')
    search_fields = ('description', 'creation_date')
    prepopulated_fields = {"slug": ("user",)}


admin.site.register(Portfolio, PortfolioAdmin)


admin.site.register(AcademicAchievements)
admin.site.register(Category)
