from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from api.validators import validate_username

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'

CHOICE_STATUS = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Админ'),
)


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(
        max_length=settings.MAX_LENGTH_NAME,
        unique=True,
        validators=[
            validate_username,
            UnicodeUsernameValidator(),
        ]
    )
    email = models.EmailField(
        max_length=settings.MAX_LENGTH_EMAIL,
        unique=True
    )
    first_name = models.CharField(
        max_length=settings.MAX_LENGTH_NAME,
        blank=True
    )
    last_name = models.CharField(
        max_length=settings.MAX_LENGTH_NAME,
        blank=True
    )

    bio = models.TextField('Биография', blank=True)
    role = models.CharField(
        max_length=max([len(role[0]) for role in CHOICE_STATUS]),
        choices=CHOICE_STATUS,
        default='user',
    )

    class Meta:
        ordering = ('pk',)

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR or self.is_staff
