from django.db import models

from artists.models import Artist

class Album(models.Model):
    """
    Model that describes an album
    """
    artist = models.ForeignKey(Artist, db_index=True)
    name = models.CharField(max_length=128)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'artist'