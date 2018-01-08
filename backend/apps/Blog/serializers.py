from rest_framework import serializers

from .models import Article


class ArticlesSerializer(serializers.ModelSerializer):

    """
    Article Model Serializer
    """

    # return author username
    author = serializers.CharField(source="author.username")

    class Meta:
        model = Article
        fields = "__all__"
