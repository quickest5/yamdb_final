from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(data):
    if data.lower() in settings.FORBIDDEN_USERNAMES:
        raise ValidationError(
            f'Нельзя использовать "{data}" в качестве username.'
        )


def validate_year(data):
    current_year = timezone.now().year
    if not 1 < data < current_year:
        raise ValidationError(
            f'Год должен быть в пределах от 1 до {current_year}; '
            f'указан год: {data}'
        )
