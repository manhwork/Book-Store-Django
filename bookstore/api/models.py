from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='./static/media/category', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, default="active")
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    discountPercentage = models.FloatField()
    stock = models.IntegerField()
    thumbnail = models.ImageField(upload_to='./static/media/category', blank=True, null=True)
    category_id = models.CharField(max_length=255)
    awsome_product = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="active")
    deleted = models.BooleanField(default=False)
    reviews = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
