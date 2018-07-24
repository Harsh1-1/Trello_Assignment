# from django.db import models
# # from pygments.lexers import get_all_lexers
# # from pygments.styles import get_all_styles
# #
# # LEXERS = [item for item in get_all_lexers() if item[1]]
# # LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# # STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
#
# class Board(models.Model):
#     created_on = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     type = models.CharField(max_length=20, default='public')
#
#     class Meta:
#         ordering = ('created_on',)

from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Board(models.Model):
    owner = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE, default=1)
    # highlighted = models.TextField()
    name = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField('date published',default=timezone.now())
    def __str__(self):
        return self.name


class TaskList(models.Model):
    board = models.ForeignKey(Board, related_name="task_list",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

# class TaskListForm(ModelForm):
#     class Meta:
#         model = TaskList
#         fields = ['board', 'name']


class Card(models.Model):
    task_list = models.ForeignKey(TaskList, related_name="card", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name
