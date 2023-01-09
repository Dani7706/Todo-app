from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
"""
Category
    • Name - maximum 15 characters
Todo
    • Title - maximum 30 characters
    • Description - any text, with no limit of words/chars
    • Category – a relation to category
    • State – can be either “Done” or “Not done”
"""
UserModel=get_user_model()

class Category(models.Model):
    MAX_NAME_LEN=15
    name= models.CharField(
        max_length=MAX_NAME_LEN,
        null=False,
        blank=False,
        unique=True,
    )
    def __str__(self):
        return f'{self.name}'

class Todo(models.Model):
    MAX_TITLE_LEN=30
    DEFAULT_STATE=False
    title=models.CharField(
        max_length=MAX_TITLE_LEN,
        null=False,
        blank=False,
    )
    description=models.TextField(
        null=True,
        blank=True,
    )
    is_done=models.BooleanField(
        default=DEFAULT_STATE,
        null=False,
        blank=False,
    )
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    user=models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )
    def __str__(self):
        return f'{self.title}'