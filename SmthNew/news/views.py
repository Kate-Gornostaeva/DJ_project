from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

# Create your views here.
def home_news(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')  # убедитесь, что имя URL верное!
        else:
            error = "Ошибка: " + str(form.errors)  # показываем ошибки
    else:
        form = News_postForm()
    return render(request, 'news/create_news.html', {'form': form, "error": error})