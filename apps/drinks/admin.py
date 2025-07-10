from django.contrib import admin
from apps.drinks.models import DrinkCategory,Drink

# admin.site.register(DrinkCategory)
# admin.site.register(Drink)


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

    # fieldsets = (
    #     (
    #         'Основная информация', {
    #         'fields': ('name',)
    #     })
    # )

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','is_available','category')
    search_fields = ('name',)
    list_filter = ('id','name')
    list_display_links = ('id', 'name',)
    ordering = ('id',)
    list_editable = ['price','is_available']

    fieldsets = (
        ('Основная информация', {
            'fields': ('name',)
        }),
    )

    # fieldsets = (
    #     ('Основная информация', {
    #         'fields': ('name', 'category')
    #     }),
    #     ('Описание', {'fields': ('description', 'volume')
    #                   }),
    #     ('Цена и наличие', {'fields': ('price', 'is_available')
    #                         }),
    #     ()
    # )



