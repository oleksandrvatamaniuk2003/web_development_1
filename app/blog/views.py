from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    return render(request, 'blog/index.html', {'latest_articles': latest_articles})
def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'blog/article_list.html', {'articles': articles})
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all().order_by('-publication_date')
    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article


            if request.user.is_authenticated:
                comment.author_user = request.user



            comment.save()
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm(user=request.user)

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })
@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    is_moderator = request.user.groups.filter(name='Moderator').exists()

    if request.user != comment.author_user and not is_moderator:


        return HttpResponseForbidden(" немає прав редагувати цей коментар")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=comment.article.pk)
    else:
        form = CommentForm(instance=comment, user=request.user)

    return render(request, 'blog/comment_form.html', {'form': form})





@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    is_moderator = request.user.groups.filter(name='Moderator').exists()
    if request.user != comment.author_user and not is_moderator:
        return HttpResponseForbidden("нема прав видаляти цей коментар")

    if request.method == 'POST':
        article_pk = comment.article.pk
        comment.delete()

        return redirect('article_detail', pk=article_pk)

    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})