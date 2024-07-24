from .models import SelfTask
from django.forms import ModelForm, TextInput, Textarea

class SelfTaskForm(ModelForm):
    class Meta:
        model = SelfTask
        fields = ['title', 'task', 'subtask', 'comment']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Задача'
            }),
            "subtask": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Подзадачи'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),

        }