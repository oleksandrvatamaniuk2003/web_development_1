from django.contrib import admin
from .models import Category, Tag, Article, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'is_published')
    list_filter = ('is_published', 'category')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'publication_date')