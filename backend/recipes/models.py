from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Tag(models.Model):
    """Модель Тега."""
    name = models.CharField(
        verbose_name='Название тега',
        max_length=200,
        unique=True,
        help_text='Введите название тега'
    )
    slug = models.SlugField(
        verbose_name='Адрес',
        unique=True,
        help_text='Укажите адрес'
    )
    hexcolor = models.CharField(
        unique=True,
        max_length=7,
        default="#ffffff",
        help_text='Выберите цвет'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    """Модель Ингредиенты."""
    name = models.CharField(
        verbose_name='Название ингредиента',
        max_length=200,
        help_text='Введите название ингредиента'
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=200,
        help_text='Введите единицу измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    """Модель Рецепта."""
    text = models.TextField(
        verbose_name='Текст рецепта',
        help_text='Введите текст рецепта'
    )
    name = models.CharField(
        verbose_name='Название рецепта',
        max_length=200,
        help_text='Введите название рецепта'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тег',
        help_text='Выберите тег'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты',
        help_text='Выберите необходимые ингредиенты'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipes/',
        help_text='Прикрепите фото приготовленного блюда'
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления(мин.)',
        validators=[MinValueValidator(1)],
        default=1,
        help_text='Введите время приготовления в минутах'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']


class IngredientRecipe(models.Model):
    """Модель для связи id рецепта и id его ингредиентов."""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        validators=[MinValueValidator(1)],
        default=1,
    )

    class Meta:
        verbose_name = 'Рецепт и ингредиент'
        verbose_name_plural = 'Рецепты и ингредиенты'
        constraints = [
            UniqueConstraint(
                fields=['ingredient', 'recipe'], name='unique_ingredientrecipe'
            )
        ]

    def __str__(self):
        return f'Рецепт: {self.recipe}, ингредиенты: {self.ingredient}'


class Favorite(models.Model):
    """Модель Избранное."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт в избранном'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorite'
            )
        ]

    def __str__(self):
        return f'{self.user} добавил рецепт: {self.recipe} в Избранное'


class ShoppingCart(models.Model):
    """Модель Список Покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'], name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        return f'{self.user} добавил рецепт: {self.recipe} в список покупок'
