from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # होमपेज का रास्ता
    path('movie/<int:movie_id>/', views.play_movie, name='play_movie'), # प्लेयर का रास्ता
]
