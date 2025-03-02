from django.urls import path
from .views import comment_view_unsecured, comment_view_secured

urlpatterns = [
    path('comment-unsecured/',comment_view_unsecured),
    path('comment-secured/', comment_view_secured)
]