from django.contrib import admin
from .models import Category
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", 'description', 'cat_image') # model field
    prepopulated_fields = {"slug": ('category_name',)}
     # 'slug field ' --> auto type ,
     #category_name--> data get from here (when we add category)


admin.site.register(Category, CategoryAdmin)
