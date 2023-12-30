from django import forms
from .models import Books

# creating a form
class BooksForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Books

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]