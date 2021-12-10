# Tango with Django Project
This repository was produced following **Tango with Django 2**, a guide to web development with Django. It can be found here: https://www.tangowithdjango.com/.

The repository contains a simple web application called **Rango**. It aggregates web pages submitted by users, categorised by users. It features a registration and log-in system supported by [**Django Registration Redux**](https://django-registration-redux.readthedocs.io/en/latest/), and its front-end design is heavily borrowed from [**Bootstrap**](https://getbootstrap.com/).

## Technologies
**Presentation tier -** HTML/CSS supported by Django Template Language

**Data tier -** SQLite3

**Application tier -** Django 2.1.5

## Running the project
To run the server, navigate to the root of the project in terminal and run the following command:
`python manage.py runserver IP:PORT`

I would recommend using:
`python manage.py runserver 127.0.01:8000`

Terminal output should confirm the server has started with a message similar to:
> Starting development server at http://IP:PORT/
> Quit the sever with CTRL-BREAK

Visiting the `IP:PORT` you chose in your web browser should also show the webpage.

## Admin Account Details
Only one admin account exists for the site. I will provide the login details for it below as it may be useful to access the admin interface to view data in the database. Additionally, being logged into the admin account unlocks a debug toolbar - created using [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - which can be used to view and measure all sorts of useful performance metrics.
| Username | Password |
| :-----------:|:------:|
| joelg | Password1! |

## Navigating the repository
The repository has a fair amount of directories and files so I will do my best to explain what they contain.

**`tango_with_django_project/media` -** Stores all media for the application that may change. For example you would store user profile pictures here, as they may change.

**`tango_with_django_project/rango` -** Contains all the Python code for the Rango application including database models and views.

**`tango_with_django_project/static` -** Stores all static media for the application, media that won't change, such as the website icon.

**`tango_with_django_project/tango_with_django_project`-** Stores the setup for the application. Importantly the ***<span>settings<span>.py*** file is located here, which holds many setup and configuration options for the project.

**`tango_with_django_project/templates/rango`-** Holds all the HTML page templates for the Rango application such as *index.html*, *category.html* etc.

**`tango_with_django_project/templates/registration`-** Holds all the HTML page templates needed by **Django Registration Redux** for login, logout, registration (etc) pages.

**`tango_with_django_project/db.sqlite3`-** The database file for the application.

**`tango_with_django_project/populate_rango.py`-** A population script to automatically add some test categories and pages to the database.

**`tango_with_django_project/requirements.txt`-** The requirements list for the project. Can be used with pip install like so: `pip install -r requirements.txt`.

## Running tests
The repository comes with some of the unit tests written for **Tango with Django**. Navigating to the project root and running the following command in the terminal will run those tests:

`python manage.py test`

More unit tests can be found [here](https://github.com/tangowithcode).

