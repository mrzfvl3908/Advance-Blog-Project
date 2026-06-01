from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

# getting user model object
# User = get_user_model()

class Post(models.Model):
    """
    this is  a class to define posts for blog app
    """
    author = models.ForeignKey('accounts_app.Profile', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, null=True)

    # class Meta:
    #     ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_app:post-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
