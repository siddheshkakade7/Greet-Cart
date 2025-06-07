from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=50,unique=True) # url of category
    description = models.TextField(max_length=255 ,blank = True)  # product description
    cat_image = models.ImageField(upload_to='photos/categories',blank=True) # we need pillow library so install it


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    # def get_url(self):
    #     return "http://127.0.0.1:8000/store/" + str(self.slug)

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
# 'products_by_category' --> url name in urls.py
#  args=[self.category.slug, self.slug
    def __str__(self):
        return self.category_name
