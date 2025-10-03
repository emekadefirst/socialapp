from django.urls import path
from .views import index, create_post, add_comment


urlpatterns = [    
    path('', index, name='index'),
    path('create', create_post, name='create_post'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
]