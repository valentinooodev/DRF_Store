from django.db import models
from core.settings import MEDIA_URL
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    tags = models.ManyToManyField('ProductTag', related_name='product_tag')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='product-images/')
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['updated']

    def __str__(self):
        return self.name

    def get_absolute_image_url(self):
        return "{0}{1}".format(MEDIA_URL, self.image.url)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    alt = models.TextField()
    image = models.ImageField(upload_to='product_img')
    is_main_image = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Product Images'


class ProductTag(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Product Tags'
        ordering = ['name']

    def __str__(self):
        return self.name
