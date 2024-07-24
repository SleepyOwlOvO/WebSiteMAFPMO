from django.db import models


class SelfTask(models.Model):
    title = models.CharField('Название задачи', max_length=50)
    task = models.TextField('Задача')
    subtask = models.TextField('Подзадача')
    comment = models.TextField('Комментарии')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/mytask/{self.id}'

    class Meta:
        verbose_name = 'Мои задачи'
        verbose_name_plural = 'Мои задачи'