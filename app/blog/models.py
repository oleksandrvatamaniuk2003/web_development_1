from django.db import models


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
    author = models.CharField(max_length=255)
    text = models.TextField()
    image = models.CharField(max_length=500, blank=True)
    publication_date = models.DateField()
    is_published = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.author}"