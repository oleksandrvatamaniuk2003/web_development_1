from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    return render(request, 'blog/index.html', {'latest_articles': latest_articles})

def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})