from django.core.validators import MinValueValidator
from django.db import models


def validate_only_letters(value):
    if not value.isalpha():
        raise ValueError("Ensure this value contains only letters.")


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 20

    MAX_LENGTH_LAST_NAME = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        default=0,
        validators=(
            MinValueValidator(0),
        ),
        null=True,
        blank=True,
        verbose_name="Profile Age"
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    MAX_LENGTH_TITLE = 20

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        verbose_name='Title',
        null=True,
        blank=True,
    )

    content = models.TextField(
        verbose_name='Content',
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Link to Image',
        null=True,
        blank=True,
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
    )
    # profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.CASCADE,
    # )

    class Meta:
        ordering = ('-title',)
