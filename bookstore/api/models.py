from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe


class Book(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField()
    price = models.FloatField()
    discountPer = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='./static/media/book', blank=True, null=True)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isExist = models.BooleanField(default=True)
    categoryID = models.ForeignKey('Category', on_delete=models.CASCADE)
    idAuthor = models.ForeignKey('Author', on_delete=models.CASCADE)
    isOutStanding = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='./static/media/category', blank=True, null=True)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isExist = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='./static/media/blog', blank=True, null=True)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isExist = models.BooleanField(default=True)
    categoryBlogID = models.ForeignKey('CategoryBlog', on_delete=models.CASCADE)
    isOutStanding = models.BooleanField(default=False)


class CategoryBlog(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)


class Author(models.Model):
    fullName = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='./static/media/author', blank=True, null=True)


class Review(models.Model):
    idBook = models.ForeignKey('Book', on_delete=models.CASCADE)
    idUser = models.ForeignKey('User', on_delete=models.CASCADE)
    cmt = models.TextField()

# class Category(models.Model):
#     title = models.CharField(max_length=255)
#     thumbnail = models.ImageField(upload_to='./static/media/category', blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     status = models.CharField(max_length=255, default="active")
#     deleted = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     slug = models.SlugField(unique=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Category, self).save(*args, **kwargs)

    
#     def __str__(self):
#         return self.title

# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.FloatField()
#     discountPercentage = models.FloatField()
#     stock = models.IntegerField()
#     thumbnail = models.ImageField(upload_to='./static/media/category', blank=True, null=True)
#     category_id = models.CharField(max_length=255)
#     awsome_product = models.CharField(max_length=255)
#     status = models.CharField(max_length=255, default="active")
#     deleted = models.BooleanField(default=False)
#     reviews = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title
