from django import forms

class RatingForm(forms.Form):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Dropdown choices from 1 to 5
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating', widget=forms.Select(attrs={'class': 'form-select'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)


 