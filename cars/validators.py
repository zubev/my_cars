from django.core.exceptions import ValidationError


def contains_only_digits(value):
    result = all(x.isdigit() for x in str(value))
    if not result:
        raise ValidationError('Should contain only digits')
