from django import forms

class CarSearchForm(forms.Form):
    query = forms.CharField(label='Search by Cars',max_length=50)