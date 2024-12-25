from django.urls import path
from .views import ListPost , CreatePost, DetailPost

urlpatterns = [
    path('', ListPost.as_view(), name='home'),
    path('createpost/', CreatePost.as_view(), name='createpost'),
    path('postdetail/<int:pk>', DetailPost.as_view(), name='detailpost')
]