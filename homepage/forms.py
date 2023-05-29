from django import forms
from .models import comment

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.truyen = kwargs.pop('truyen', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.truyen = self.truyen
        comment.save()

    class Meta:
        model = comment
        fields = ["content"]
