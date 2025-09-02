from django.db import models
from django.utils.text import slugify 

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    slug= models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    cat_image = models.ImageField(upload_to='photos/category', blank=True, null=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'  
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.cat_name)
        super().save(*args, **kwargs)       
    def __str__(self):
        return self.cat_name
    