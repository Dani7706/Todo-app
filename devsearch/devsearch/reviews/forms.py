from statistics import mode
from django import forms

from devsearch.reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields=['description', 'value']