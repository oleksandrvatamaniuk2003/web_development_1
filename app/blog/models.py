from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="FontAwesome icon class")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)

    # Зв'язок з користувачем Django. Може бути null (якщо автор видалений або анонім)
    author_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    # Текстове поле для збереження імені (на випадок анонімів)
    author_name = models.CharField(max_length=255, blank=True)

    text = models.TextField()
    image = models.CharField(max_length=500, blank=True)
    publication_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_author(self):
        if self.author_user:
            return self.author_user.username
        return self.author_name or "Anonymous"


class Comment(models.Model):
    text = models.TextField()

    # Коментар теж може мати прив'язку до юзера
    author_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    author_name = models.CharField(max_length=255, blank=True)

    publication_date = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.get_author()}"

    def get_author(self):
        if self.author_user:
            return self.author_user.username
        return self.author_name or "Anonymous"