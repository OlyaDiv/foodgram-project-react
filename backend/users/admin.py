from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    """Класс для работы с пользователями в админ-панели."""
    list_display = ('id', 'username', 'email', 'first_name', 'last_name',)
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)


class FollowAdmin(admin.ModelAdmin):
    """Класс для работы с подписками в админ-панели."""
    list_display = ('user', 'author',)


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
