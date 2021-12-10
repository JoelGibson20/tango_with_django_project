# This file contains all the views for the application. They handle requests to that specific page
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm, PageForm
from datetime import datetime


def index(request):  # View for the index page
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    # Retrieve the 5 most liked categories, and 5 most viewed pages from the database
    context_dict = {'categories': category_list, 'pages': page_list}
    # These categories and pages are added to the context_dict, which is a dictionary containing variables to be
    # used within the HTML page

    visitor_cookie_handler(request)  # Make a call to the function visitor_cookie_handler, it increments the page view
    # counter whenever a new viewer visits the index page that day
    context_dict['visits'] = request.session['visits']
    # This page visits counter is also added the context dictionary

    response = render(request, 'rango/index.html', context=context_dict)
    # Response to the user is to render the specified page (index in this case), with the context dictionary
    return response


def about(request):  # View for the about page
    context_dict = {'boldmessage': "This tutorial has been put together by Joel"}
    # This context dictionary just includes a bold message to be displayed on the page
    # Defining the message here rather than in the HTML template itself means the HTML template can be re-used to
    # display different content if necessary

    # Response to the user is to render the specified page, with the context dictionary
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):  # View for a category page
    # All the categories share the same page template, they just display different information. So the context
    # dictionary will be populated with different content based on which category is requested
    context_dict = {}

    try:
        # Attempt to retrieve the category based on the provided slug e.g: python
        category = Category.objects.get(slug=category_name_slug)
        # Failure to find the category will raise a Category.DoesNotExist exception (handled below)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Adds our pages list to the context dictionary under the name pages
        context_dict['pages'] = pages
        # Category object also added to the context dictionary
        context_dict['category'] = category

    except Category.DoesNotExist:
        # Did not find the category from the slug provided
        context_dict['category'] = None
        context_dict['pages'] = None
        # Render a page which informs the user the specified category doesn't exist
        # (the code for this message is found in the HTML template category.html)
    return render(request, 'rango/category.html', context_dict)


def add_category(request):  # View for the add category page
    form = CategoryForm()  # Create an add category form (found in forms.py)

    # Check if HTTP request was POST (meaning the user submitted the form)
    if request.method == 'POST':
        form = CategoryForm(request.POST)  # Get the submitted form

        if form.is_valid():  # Check if we've been provided a valid form
            form.save(commit=True)  # Save the new category to the database
            return index(request)  # Redirect back to the index
    else:
        # The supplied form contained errors which are printed to the terminal
        print(form.errors)

    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):  # View for add page page
    try:
        category = Category.objects.get(slug=category_name_slug)  # Check whether the provided category exists
    except Category.DoesNotExist:
        category = None  # No such category found, set category to none

    form = PageForm()  # Create an add page form

    # Check if HTTP request was POST (meaning the user submitted the form)
    if request.method == 'POST':
        form = PageForm(request.POST)  # Get the submitted form

        if form.is_valid():  # Check if we've been provided a valid form
            if category:  # If the category exists
                page = form.save(commit=False)  # Save the form categories to the new page
                page.category = category
                page.views = 0
                # Add the category and views fields to the page (not provided through the form)
                page.save()  # Save the new page to the database

                # Returns the user to the category page they've successfully added a new page to
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)


# A helper method for retrieving cookies
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)  # Tries to get session cookie from the server
    if not val:
        val = default_val

    return val


# Function which tracks visitors to the index and increments the views counter accordingly
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))  # Get the session cookie for the visitor
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    # Get the cookie for the last time time the visitor visited the index
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    # Use the last visit cookie to deduce the last time the visitor visited the index

    if (datetime.now() - last_visit_time).days > 0:  # If it's been more than a day since the last visit
        visits = visits + 1  # Add a visit to the visits counter
        # Update the last visit cookie for the user to represent this visit as their latest visit
        request.session['last_visit'] = str(datetime.now())
    else:  # It hasn't been more than a day since their last visit
        # Just update the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits


def restricted(request):
    return render(request, 'rango/restricted.html')
