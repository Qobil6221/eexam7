from django.contrib import admin
from .models import Author, Product, Categories


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'bid', 'owner', 'owner_username']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']


@admin.register(Categories)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'img']