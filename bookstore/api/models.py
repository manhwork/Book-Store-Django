from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.core.validators import MinValueValidator
# from django.db import User 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Change form register django
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class Book(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)], null=True)
    discountPer = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(validators=[MinValueValidator(1)],null=True)
    image = models.ImageField(upload_to='./static/media', blank=True, null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Author = models.ForeignKey('Author', on_delete=models.CASCADE)
    isOutStanding = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='./static/media', blank=True, null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" width="50" height="50" />' % (self.image))
    
    image_tag.short_description = 'Image'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='./static/media', blank=True, null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    categoryBlogID = models.ForeignKey('CategoryBlog', on_delete=models.CASCADE, related_name='blogs_from_categoryBlogID')
    # isOutStanding = models.BooleanField(default=False)
    blogCate = models.ForeignKey('CategoryBlog', on_delete=models.CASCADE,  related_name='blogs_from_blogCate')  
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class CategoryBlog(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)  
    createAt = models.DateTimeField(auto_now_add=True)  
    updateAt = models.DateTimeField(auto_now=True)  
    is_active = models.BooleanField(default=True)  

    def save(self, *args, **kwargs):
        # Tạo slug từ title nếu chưa có
        if not self.slug:
            self.slug = slugify(self.title)
        super(CategoryBlog, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title


class Author(models.Model):
    fullName = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='./static/media', blank=True, null=True)
    def __str__(self):
        return self.fullName 


class Review(models.Model):
    idBook = models.ForeignKey('Book', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    cmt = models.TextField()
