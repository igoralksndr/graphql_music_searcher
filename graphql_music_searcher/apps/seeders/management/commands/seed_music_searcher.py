import urllib.parse

from django.core.management.base import BaseCommand
from artists.models import Artist
from albums.models import Album
from tracks.models import Track

class Command(BaseCommand):
    help = 'This command will seed the database (Artists, Albums and Tracks)'

    def handle(self, *args, **options):
        print('\n  Music Seeder is running...\n')

        print('    Deleting...')
        cleanModels()

        print('    Inserting...')
        insertModels()

def cleanModels():
    Track.objects.all().delete()
    Album.objects.all().delete()
    Artist.objects.all().delete()
    print('    Artists, Albums and Tracks have been deleted')

def insertModels():
    
    at1 = Artist(name= 'Pink Floyd', image_url=urllib.parse.quote('cdn4.pitchfork.com/artists/3319/m.2df68254.jpg'))
    at1.save()
    
    abm11 = at1.album_set.create(name='The Dark Side of the Moon', image_url=urllib.parse.quote('upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png'))
    abm11.track_set.create(name='Breathe', preview_url='', track_number=2)
    abm11.track_set.create(name='Money', preview_url='', track_number=6)
    abm11.track_set.create(name='Us and Them', preview_url='', track_number=7)
    
    abm12 = at1.album_set.create(name='Wish You Were Here', image_url=urllib.parse.quote('upload.wikimedia.org/wikipedia/en/a/a4/Pink_Floyd%2C_Wish_You_Were_Here_(1975).png'))
    abm12.track_set.create(name='Shine On You Crazy Diamond Part I', preview_url='', track_number=1)
    abm12.track_set.create(name='Have a Cigar', preview_url='', track_number=7)
    abm12.track_set.create(name='Wish You Were Here', preview_url='', track_number=8)

    
    at2 = Artist(name= 'Solid Globe', image_url=urllib.parse.quote('img.discogs.com/0ITHOlhTcjzhFfavvsVocXaMQyA=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-6291815-1415727886-9789.jpeg.jpg'))
    at2.save()
    
    abm21 = at2.album_set.create(name='Sahara vs. North Pole', image_url=urllib.parse.quote('img.discogs.com/YRaNt_nmWd9Q86Y2yq3Ufrhq_rg=/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-819529-1164177393.jpeg.jpg'))
    abm21.track_set.create(name='North Pole vs. Sahara (Alex M.O.R.P.H. Remix)', preview_url='', track_number=1)
    abm21.track_set.create(name='North Pole (Thomas Datt Remix)', preview_url='', track_number=2)
    
    abm22 = at2.album_set.create(name='Lost Cities / Found', image_url=urllib.parse.quote('img.discogs.com/BtDwId0VI6qPwGfCGh4gzmiUMIk=/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-458576-1145966783.jpeg.jpg'))
    abm22.track_set.create(name='Lost Cities', preview_url='', track_number=1)
    abm22.track_set.create(name='Found', preview_url='', track_number=2)

    
    at3 = Artist(name= 'Natiruts', image_url=urllib.parse.quote('i.scdn.co/image/9b3411def3d9d7e9ddfb34b9b102997ec0a9b863'))
    at3.save()
    at4 = Artist(name= 'Luiz Melodia', image_url=urllib.parse.quote('rollingstone.uol.com.br/media/images/medium/2012/05/04/img-1005476-luiz-melodia.jpg'))
    at4.save()
    at5 = Artist(name= 'Sonia Savinell', image_url=urllib.parse.quote('i.vimeocdn.com/portrait/5278758_300x300'))
    at5.save()
    
    abm31 = at3.album_set.create(name='Povo Brasileiro', image_url=urllib.parse.quote('e.snmc.io/lk/f/l/fcd44e7b52a73f3a0326ce6ce74a8f55/1859850.jpg'))
    abm31.track_set.create(name='Eu e Ela', preview_url='', track_number=4)
    abm31.track_set.create(name='A Cor', preview_url='', track_number=6)
    
    abm32 = at3.album_set.create(name='Natiruts Acustico no Rio de Janeiro', image_url=urllib.parse.quote('statics.livrariacultura.net.br/products/capas_lg/615/30215615.jpg'))
    abm32.track_set.create(name='Dentro da Música II', preview_url='', track_number=1)
    abm32.track_set.create(name='Quero Ser Feliz Tambem', preview_url='', track_number=6)
    abm32.track_set.create(name='Pedras Escondidas', preview_url='', track_number=11)
    trck8 = abm32.track_set.create(name='Perola Negra', preview_url='', track_number=8)
    trck8.artists.add(at4)
    trck17 = abm32.track_set.create(name='Sorri, Sou Rei', preview_url='', track_number=17)
    trck17.artists.add(at5)

    at6 = Artist(name= 'Led Zeppelin', image_url=urllib.parse.quote('consequenceofsound.files.wordpress.com/2010/12/led_zeppelin_1225212304_crop_300x300.jpg?quality=80&w=300'))
    at6.save()

    abm61 = at6.album_set.create(name='Led Zeppelin II ', image_url=urllib.parse.quote('upload.wikimedia.org/wikipedia/en/2/20/Led_Zeppelin_-_Led_Zeppelin_II.jpg'))
    abm61.track_set.create(name='Whole Lotta Love', preview_url='', track_number=1)
    abm61.track_set.create(name='Ramble On', preview_url='', track_number=7)

    abm62 = at6.album_set.create(name='Led Zeppelin IV ', image_url=urllib.parse.quote('upload.wikimedia.org/wikipedia/en/2/26/Led_Zeppelin_-_Led_Zeppelin_IV.jpg'))
    abm62.track_set.create(name='Black Dog', preview_url='', track_number=1)
    abm62.track_set.create(name='Stairway To Heaven', preview_url='', track_number=4)

    print('    Artists, Albums and Tracks have been inserted')