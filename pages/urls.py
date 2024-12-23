from django.urls import path
from .views import ListPost , CreatePost

urlpatterns = [
    path('', ListPost.as_view(), name='home'),
    path('createpost/', CreatePost.as_view(), name='createpost')
]