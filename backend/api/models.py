from django.db import models


class Note(models.Model):
    title = models.CharField("Название заметки", max_length=100)
    description = models.TextField("Описание заметки", default="")
    completed = models.BooleanField("Выполнено", default=False)

    def __str__(self):
        return self.title
