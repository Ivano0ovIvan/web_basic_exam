from django.core import validators
from django.db import models
from .validators import check_if_value_starts_with_letter, check_if_value_contains_only_letters


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            validators.MinLengthValidator(2),
            check_if_value_starts_with_letter],
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            validators.MinLengthValidator(1),
            check_if_value_starts_with_letter],
    )
    email = models.EmailField(max_length=40)
    password = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(8),]
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"



class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(1),
            check_if_value_contains_only_letters
        ]
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
    # profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)