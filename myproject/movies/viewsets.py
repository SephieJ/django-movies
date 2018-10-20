from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.object.all()
    serializer_class = MovieSerializer