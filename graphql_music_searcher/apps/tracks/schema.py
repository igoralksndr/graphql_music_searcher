import graphene

from graphene import resolve_only_args
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from artists.schema import ArtistType

from .models import Track


class TrackType(DjangoObjectType):
    artists = graphene.List(ArtistType)

    @graphene.resolve_only_args
    def resolve_artists(self):
        return self.artists.all()

    class Meta:
        model = Track

class TrackQuery(graphene.AbstractType):
    track = graphene.Field(TrackType,
                            id=graphene.Int(),
                            by_name=graphene.String(),
                            )
    all_tracks = graphene.List(TrackType)

    def resolve_all_tracks(self, args, context, info):
        return Track.objects.select_related('album').all()

    def resolve_track(self, args, context, info):
        id = args.get('id')
        by_name = args.get('by_name')

        if id is not None:
            return Album.objects.get(id=id)

        if by_name is not None:
            return Album.objects.get(name=by_name)

        return None