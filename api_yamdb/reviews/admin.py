from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from reviews.models import Category, Comment, Genre, Review, Title, User


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]


class CommentResource(resources.ModelResource):
    review = fields.Field(attribute='review',
                          column_name='review_id',
                          widget=ForeignKeyWidget(Review, 'id'))

    class Meta:
        model = Comment
        fields = ('id', 'review', 'text', 'author', 'pub_date')


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    resource_classes = [CommentResource]


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug',)


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]


class ReviewResource(resources.ModelResource):
    title = fields.Field(attribute='title',
                         column_name='title_id',
                         widget=ForeignKeyWidget(Title, 'id'))

    class Meta:
        model = Review
        fields = ('id', 'title', 'text', 'author', 'score',)


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    resource_classes = [ReviewResource]


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category',)


@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'bio',
                  'first_name', 'last_name',)


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]
