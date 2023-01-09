from django.db import models
from django.core.validators import MinLengthValidator

from devsearch.tags.models import Tag



class Project(models.Model):
    MIN_TITLE_LENGTH=2
    MAX_TITLE_LENGTH=200
    MAX_DEMO_LINK_LENGTH=2000
    MAX_SOURSE_CODE_LENGTH=2000
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[
            MinLengthValidator(MIN_TITLE_LENGTH)
        ],
        null=False,
        blank=False
    )
    description= models.TextField(
        null=True,
        blank=True,
    )
    featured_image=models.ImageField(
        null=True,
        blank=True,
        default="default-project.png"
    )
    demo_link= models.CharField(
        max_length=MAX_DEMO_LINK_LENGTH,
        null=True,
        blank=True,
    )
    source_code=models.CharField(
        max_length=MAX_SOURSE_CODE_LENGTH,
        null=True,
        blank=True,
    )
    tags= models.ManyToManyField(
        Tag,
        null=False,
        blank=False,
    )
    vote_total= models.IntegerField(
        default=0,
        null=True,
        blank=True
    )
    vote_ratio= models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    created_on= models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title




