from django.urls import path

from .views import create_digest, get_all_digest

urlpatterns = [
    path('api/v1/digest_for_userid_<int:user_id>/', create_digest),
    path('api/v1/get_all_digest', get_all_digest),
]
