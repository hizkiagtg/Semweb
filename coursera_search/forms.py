from django import forms

class SearchForm(forms.Form):
    SMS_TEXT_CHOICES = [
        ('course', 'by Course'),
        ('university', 'by University'),
        ('price', 'by Price'),
        ('skills', 'by Skills'),
        ('ratings', 'by Ratings'),
        ('level', 'by Level'),
        ('type', 'by Type'),
        ('duration', 'by Duration'),
    ]

    sms_text = forms.CharField(
        label='Search Your Course',
        widget=forms.Textarea(attrs={'rows': 1, 'spellcheck': 'false', 'style': 'margin-left: 6%;'}),
    )
    
    search_type = forms.ChoiceField(
        choices=SMS_TEXT_CHOICES,
        widget=forms.Select,
    )
    
