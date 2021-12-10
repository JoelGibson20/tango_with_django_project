# This file contains all form models/classes
from django import forms
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):  # Form for adding a new category
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # The hidden input fields are auto-generated for the category
    # Views and likes are initialised at 0
    # Slug is generated in the category model in models.py using the slugify command

    class Meta:  # An inline class to provide additional information on the form.
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)
        # Here we define the order to display the form fields to the user, but we only want to display the name field
        # as that is the only field they provide a value for


class PageForm(forms.ModelForm):  # Form for adding a new page
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # Views is once again hidden, and initialised to 0

    class Meta:  # An inline class to provide additional information on the form.
        # Provide an association between the ModelForm and a model
        model = Page
        exclude = ('category',)
        # Here instead of defining what fields to display, we define what fields to hide
        # The page model has foreign key category, but the user doesn't need to see this
        # They've already chosen to add a new page to this specific category

    def clean(self):  # This function is intended to correct url format to ensure it starts with http://
        # This doesn't appear to be working
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', then prepend 'http://'
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url  # Reassign new value with 'http://' prepended

        return cleaned_data  # Must finish clean method by returning cleaned_data or value changes won't be applied
