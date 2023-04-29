from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


class RecipeAdmin(admin.ModelAdmin):
    """Класс для работы с рецептами в админ-панели."""
    list_display = ('name', 'author', 'id', 'in_favorites',)
    list_filter = ('author', 'name', 'tags',)
    readonly_fields = ('in_favorites',)
    search_fields = ('name',)

    def in_favorites(self, object):
        return object.favorites.count()


class TagAdmin(admin.ModelAdmin):
    """Класс для работы с тегами в админ-панели."""

    list_display = ('name', 'slug', 'hexcolor',)
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    """Класс для работы с ингредиентами в админ-панели."""

    list_display = ('name', 'measurement_unit',)
    search_fields = ('name',)
    list_filter = ('name',)


class ShoppingCartAdmin(admin.ModelAdmin):
    """Класс для работы со списками покупок в админ-панели."""
    list_display = ('user', 'recipe',)


class FavoritesAdmin(admin.ModelAdmin):
    """Класс для работы с избранным в админ-панели."""
    list_display = ('user', 'recipe',)


class IngredientRecipeAdmin(admin.ModelAdmin):
    """Класс для работы с количеством ингредиентов."""
    list_display = ('recipe', 'ingredient', 'amount',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Favorite, FavoritesAdmin)
admin.site.register(IngredientRecipe, IngredientRecipeAdmin)
