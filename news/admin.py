from django.contrib import admin

from news.models import Category, New

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(New) # Registrando com Decorator
class NewAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)