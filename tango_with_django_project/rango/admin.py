from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fields = ["title", "category", "url", "views"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
