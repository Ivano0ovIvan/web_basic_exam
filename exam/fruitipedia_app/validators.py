from django.core.exceptions import ValidationError


def check_if_value_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def check_if_value_contains_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")


