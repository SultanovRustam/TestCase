from rest_framework import serializers

from .models import Digest, Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'popularity', 'source')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['source_name'] = instance.source.name
        return representation


class DigestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    posts = PostSerializer(many=True)

    class Meta:
        model = Digest
        fields = ('user', 'posts')
