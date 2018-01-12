from rest_framework import serializers

from .models import Article, Comment


class ArticlesSerializer(serializers.ModelSerializer):

    """
    Article Model Serializer
    """

    # return author username
    author = serializers.CharField(source="author.username")
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_comment_count(self, obj):
        return obj.comment.count()

class CommentsSerializer(serializers.ModelSerializer):

    """
    Comments Model Serializer
    """

    # return author username
    author = serializers.CharField(source="author.username")

    class Meta:
        model = Comment
        fields = "__all__"
