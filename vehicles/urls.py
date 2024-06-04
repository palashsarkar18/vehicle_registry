from django.urls import path
from .views import upload_file, search, index

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_file, name='upload_file'),
    path('search/', search, name='search')
]
