from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):  # Method to fetch all the categories to be listed on the sidebar
    return {'cats': Category.objects.all(), 'act_cat': cat}
