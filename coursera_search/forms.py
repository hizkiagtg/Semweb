from django import forms

class SearchProviderForm(forms.Form):
    searched_provider = forms.CharField(label='Enter Provider Name')