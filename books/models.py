from django.db import models
from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books", verbose_name="Автор"
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
