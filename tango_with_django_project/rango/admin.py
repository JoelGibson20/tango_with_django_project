# This file defines models to be displayed within the admin interface, and how they should be displayed
from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):  # Defines how the page model is shown in the admin interface
    fields = ["title", "category", "url", "views"]
    # Will display the fields for the page class in this order


class CategoryAdmin(admin.ModelAdmin):  # Defines how the category model is shown in the admin interface
    prepopulated_fields = {'slug': ('name',)}
    # Pre-populates the slug input for the page by creating a slug from the category's name


# Register models here
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
