import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Artist

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        model.albums = model.album_set
        exclude_fields = ('album_set')

class ArtistQuery(graphene.AbstractType):
    artist = graphene.Field(ArtistType,
                            id=graphene.Int(),
                            by_name=graphene.String(),
                            name='queryArtists')
    all_artists = graphene.List(ArtistType)

    def resolve_all_artists(self, args, context, info):
        return Artist.objects.all()

    def resolve_artist(self, args, context, info):
        id = args.get('id')
        by_name = args.get('by_name')

        if id is not None:
            return Artist.objects.get(id=id)

        if by_name is not None:
            return Artist.objects.get(name=by_name)

        return None

