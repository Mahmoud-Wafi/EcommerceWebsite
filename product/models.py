from django.db import models
from category.models import Category
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify



class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug=models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock= models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    product_image = models.ImageField(upload_to='photos/product_images', blank=True, null=True)
    category= models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE)
    
    verbose_name = 'Product Name'
    verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)