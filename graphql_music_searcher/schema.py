import graphene

from artists.schema import ArtistQuery
from albums.schema import AlbumQuery
from tracks.schema import TrackQuery


class Query(
        ArtistQuery,
        AlbumQuery,
        TrackQuery,
        graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)