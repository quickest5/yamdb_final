from api.validators import validate_year
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class GenreCategoryBase(models.Model):
    name = models.CharField(max_length=settings.MAX_LENGTH_CONTENT,)
    slug = models.SlugField(max_length=settings.MAX_LENGTH_SLUG, unique=True,)

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        return self.name


class Genre(GenreCategoryBase):
    pass


class Category(GenreCategoryBase):
    pass


class Title(models.Model):
    name = models.CharField(
        max_length=settings.MAX_LENGTH_CONTENT,
        verbose_name='Произведение',
        help_text='Введите название произведения'
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
        validators=[validate_year]
    )
    description = models.CharField(
        max_length=settings.MAX_LENGTH_CONTENT,
        verbose_name='Описание',
        null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        help_text='Категория, к которой будет относиться произведение',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='titles'
    )
    genre = models.ManyToManyField(Genre, related_name='genres')

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name


class UserContentBase(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class Review(UserContentBase):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )

    score = models.PositiveSmallIntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        ordering = ('pub_date', 'pk')
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            ),
        ]
        default_related_name = 'reviews'


class Comment(UserContentBase):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('pub_date', 'pk')
        default_related_name = 'comments'
