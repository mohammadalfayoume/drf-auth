from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer 
# Create your views here.
from .models import Movie
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

class MovieListView(ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer
    permission_classes=[IsOwnerOrReadOnly]

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer
    permission_classes=[IsOwnerOrReadOnly]