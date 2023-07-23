from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Digest, Post, User
from .serializers import DigestSerializer


@api_view(['POST'])
def create_digest(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    subscribed_sources = user.subscriptions.values_list('source', flat=True)

    popular_posts = Post.objects.filter(source__in=subscribed_sources,
                                        popularity__gt=80)

    digest = Digest.objects.create(user=user)
    digest.posts.set(popular_posts)
    serializer = DigestSerializer(digest)

    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET'])
def get_all_digest(request):
    digest = Digest.objects.all()
    serializer = DigestSerializer(digest, many=True)

    return Response(serializer.data, status.HTTP_200_OK)
