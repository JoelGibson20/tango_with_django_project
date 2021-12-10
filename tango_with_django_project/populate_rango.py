# Population script, creates some values and stores them in the database
# Can be used in unit testing to test the database
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page  # Import our database models


def populate():
    # Create lists of dictionaries containing the pages we want to add into each category.

    python_pages = [{"title": "Official Python Tutorial",
                     "url": "http://docs.python.org/2/tutorial/",
                     "views": 50},
                    {"title": "How to Think like a Computer Scientist",
                     "url": "http://www.greenteapress.com/thinkpython/",
                     "views": 40},
                    {"title": "Learn Python in 10 Minutes",
                     "url": "http://www.korokithakis.net/tutorials/python/",
                     "views": 70}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 15},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 25},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 35}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 5},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 20}]

    # Create a dictionary of dictionaries for our categories.
    cats = {"Python": [{"pages": python_pages}, 128, 64],
            "Django": [{"pages": django_pages}, 64, 32],
            "Other Frameworks": [{"pages": other_pages}, 32, 16]}

    for cat, cat_data in cats.items():  # Iterate through the category dictionaries in cats dictionary
        c = add_cat(cat, cat_data[1], cat_data[2])  # Add category to database with the category's fields
        for p in cat_data[0].items():
            for q in p[1]:  # Iterate through the pages in the category dictionary
                add_page(c, q["title"], q["url"], q["views"])  # Add the pages to the database

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views):  # Method that saves a page to the database
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views, likes):  # Method that saves a category to the database
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Execution started here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
