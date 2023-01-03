from django.db import models
from django.core.validators import MinLengthValidator

from devsearch.common.models import BaseModel

class Tag(BaseModel):
    MIN_NAME_LENGTH=2
    MAX_NAME_LENGTH=200
    name=models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
        ],
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name