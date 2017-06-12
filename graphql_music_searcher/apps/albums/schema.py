import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Album

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        model.tracks = model.track_set
        exclude_fields = ('track_set')

class AlbumQuery(graphene.AbstractType):
    album = graphene.Field(AlbumType,
                            id=graphene.Int(),
                            by_name=graphene.String(),
                            )
    all_albums = graphene.List(AlbumType)

    def resolve_all_albums(self, args, context, info):
        return Album.objects.select_related('artist').all()

    def resolve_album(self, args, context, info):
        id = args.get('id')
        by_name = args.get('by_name')

        if id is not None:
            return Album.objects.get(id=id)

        if by_name is not None:
            return Album.objects.get(name=by_name)

        return None
