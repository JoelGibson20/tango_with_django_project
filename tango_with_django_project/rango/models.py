# This file contains the definitions of models which Django will use to create the underlying database tables
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):  # Model for a category
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    # All fields are defined here, including extra properties like default values, max length, and whether or not the
    # field must be unique or not

    def save(self, *args, **kwargs):  # This function creates a slug for the category based on the provided name
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:  # Nested meta class contains other metadata about the class
        # Plenty of options: https://docs.djangoproject.com/en/2.0/topics/db/models/#meta-options
        verbose_name_plural = "Categories"  # Defines what the plural for this class should be

    def __str__(self):  # Provides a string representation for the class
        return self.name


class Page(models.Model):  # Model for a page
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    # All fields are defined here, including extra properties like default values, and max length.
    # Category is set as a foreign key to match a page to a category. Consequently we must decide what happens if this
    # category (and thus the foreign key is deleted). We decided to CASCADE and delete all pages within this category
    # when the page is deleted.
    # Other options found here: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey

    def __str__(self):  # Provides a string representation for the class
        return self.title
