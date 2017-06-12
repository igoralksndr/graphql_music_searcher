from django.db import models

from albums.models import Album
from artists.models import Artist

class Track(models.Model):
    """
    Model that describes a track
    """
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, db_index=True)
    name = models.CharField(max_length=128)
    preview_url = models.CharField(max_length=2083)
    track_number = models.PositiveIntegerField()    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Track, self).save(*args, **kwargs)
        # Need to get id with save before use the many-to-many relationship
        self.artists.add(self.album.artist)


    class Meta:
        order_with_respect_to = 'album'