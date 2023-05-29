from django import forms
from .models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ["content"]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }