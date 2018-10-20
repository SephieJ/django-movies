from django.db import models


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=255)
    is_active = models.BooleanField()
