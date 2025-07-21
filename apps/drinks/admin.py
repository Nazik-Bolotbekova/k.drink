from django.contrib import admin
from apps.drinks.models import DrinkCategory, Drink, Review



admin.site.register(Review)

@admin.register(DrinkCategory)
class DrinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    list_filter = ('id','name')
    list_display_links = ('id', 'name',)
    ordering = ('id',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('name',)
        }),
        ('Описание', {
            'fields': ('description',)
        }),
    )


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','is_available','category','country','volume','image')
    search_fields = ('name',)
    list_filter = ('id','name')
    list_display_links = ('id', 'name',)
    ordering = ('id',)
    list_editable = ['price','is_available']

    fieldsets = (
        ('Основная информация', {
            'fields': ('name','price','volume','is_available','image')
        }),
        ('Категория', {
            'fields': ('category','country')
        }),
    )




