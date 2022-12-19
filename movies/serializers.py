from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        # fields=['id','name','image', 'user', 'description','rate']
        fields='__all__'