from rest_framework import serializers

from blog.models import (User,
                         Article,
                         Editor,
                         Author)


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"


class AuthorSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = Author

class EditorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author


class ArticleSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    # editor = UserSerializer(many=True)


    class Meta:
        model = Article
        #exclude = ("password")
        fields = "__all__"

class Comments(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False,  read_only=True)
    article = serializers.PrimaryKeyRelatedField(many=False, read_only=True)  # id user who wrote a comment
    text = serializers.CharField(max_length=2500)
    create = serializers.DateTimeField()
    update = serializers.DateTimeField()