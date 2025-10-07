from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    published_date = forms.DateField(
    required=False,
    widget=forms.DateInput(attrs={'type': 'date'})
)


    class Meta:
     model = Book
     fields = ['title', 'author', 'published_date', 'isbn', 'pages', 'cover_url', 'summary']

    widgets = {
     'summary': forms.Textarea(attrs={'rows': 4}),
    }