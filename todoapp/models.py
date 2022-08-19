
from django.db import models


PRIORITY = (("danger","high"),("info","normal"),("secondary","low"))
# Create your models here.
class ToDoModel(models.Model):
    title = models.CharField(max_length=60)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
        )
    duedate = models.DateField()
    def __str__(self) -> str:
        return self.title
    # stringという特殊メソッドを使うことにより表示を変更できる。