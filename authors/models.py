from django.db import models
from django.contrib.auth import get_user_model


class Author(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Имя")
    second_name = models.CharField(max_length=25, verbose_name="Фамилия")
    birth_at = models.DateField(verbose_name="Дата рождения")

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="author", verbose_name="Пользователь")

    def __str__(self) -> str:
        return f"{self.second_name} {self.first_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
