from django.db import models

class Artist(models.Model):
    """
    Model that describes an artist
    """
    name = models.CharField(max_length=128)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)