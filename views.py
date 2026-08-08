from django.shortcuts import render, get_object_or_404
from .models import Movie

def home(request):
    featured_movies = Movie.objects.filter(is_featured=True)
    all_movies = Movie.objects.all()
    action_movies = Movie.objects.filter(genre__icontains='Action')
    animation_movies = Movie.objects.filter(genre__icontains='Animation')
    
    context = {
        'featured_movies': featured_movies,
        'all_movies': all_movies,
        'action_movies': action_movies,
        'animation_movies': animation_movies,
    }
    return render(request, 'home.html', context)

def play_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'play.html', {'movie': movie})
