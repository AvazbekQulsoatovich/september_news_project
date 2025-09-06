from django.contrib import admin
from .models import News, Category 

# Register your models here.

#admin.site.register(News)
#admin.site.register(Category)

@admin.register(Category)
class  CategoryAdmin (admin.ModelAdmin):
    list_display = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'status']
    list_filter = ['title', 'created_at']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']