# This file contains URL mappings for the application
from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    # No URL pattern for the index, so just typing in the webpage will take you to the index
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    # Category pages located at their slug e.g: category/python
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    # Add page is a part of a particular category e.g: category/python/add_page is the url to add a new page to the
    # Python category
    path('restricted/', views.restricted, name='restricted'),

    # All these URLs are linked to a view, which handles the request to the page. It will load any content required for
    # the page, and will then return the HTML page to be displayed.
    # Most of these views can be found in views.py
]

