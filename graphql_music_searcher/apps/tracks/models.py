from django.db import models

from albums.models import Album

class Track(models.Model):
    """
    Model that describes a track
    """
    album = models.ForeignKey(Album, db_index=True)
    name = models.CharField(max_length=128)
    preview_url = models.CharField(max_length=255)
    track_number = models.PositiveIntegerField()    

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'album'