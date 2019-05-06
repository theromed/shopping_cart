from django.contrib import admin

# Register your models here.
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {"slug":('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','price', 'stock', 'available', 'created', 'updated',] # какие столбы видим в БД
	list_editable = ['price','stock', 'available',] # Какие столбцы можем изменять в БД
	prepopulated_fields = {'slug':('name',) } # слаг подставляется на основе имени
	list_per_page = 20

admin.site.register(Product,ProductAdmin)
