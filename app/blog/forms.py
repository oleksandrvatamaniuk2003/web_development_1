from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        labels = {
            'author_name': "Ваше ім'я (якщо не увійшли)",
            'text': "Текст коментаря"
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }


        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['author_name'].widget = forms.HiddenInput()
            self.fields['author_name'].required = False