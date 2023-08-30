from django.db import models


class Note(models.Model):
    title = models.CharField("Название заметки", max_length=100)
    text = models.TextField("Описание заметки", default="")

    def __str__(self):
        return self.title
