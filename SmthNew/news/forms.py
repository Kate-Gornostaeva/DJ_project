from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date', 'author']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите полное описание'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'От кого новость'}),
        }