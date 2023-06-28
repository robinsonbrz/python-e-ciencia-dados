from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category
from tag.models import Tag


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField()

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name'
    )
    # related field example, getting id from relation
    # # category = serializers.PrimaryKeyRelatedField(
    # #     queryset=Category.objects.all(),
    # # )
    # related field example, getting CategoryName from relation
    category = serializers.StringRelatedField()
    category_name = serializers.StringRelatedField(
        source='category',
    )
    # author = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all()
    # )
    author = serializers.StringRelatedField()
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    tag_objects = TagSerializer(
        many=True, source='tags'
    )

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'