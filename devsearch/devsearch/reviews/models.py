from django.db import models

from devsearch.common.models import BaseModel
from devsearch.projects.models import Project

class Review(BaseModel):
    VOTE_TYPE=(
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    MAX_VOTE_LENGTH=max([len(x) for x,_ in VOTE_TYPE])
    print(MAX_VOTE_LENGTH)
    description = models.TextField(
        null=True,
        blank=True
        )
    value= models.CharField(
        max_length=MAX_VOTE_LENGTH,
        choices=VOTE_TYPE
        )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return self.value
