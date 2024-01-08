from django import forms
from .models import Twitts

class TwittsForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
            "placeholder":"Twitts something...", 
            "class": "textarea is success is-medium"
            }
        ),
        label="",
    )
    class Meta:
        model = Twitts
        exclude = ('user', )