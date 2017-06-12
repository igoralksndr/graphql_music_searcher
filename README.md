# Graphql Music Searcher

Basic example of the use of graphene integration with Django

## Deploying locally with Docker


```bash
git clone git@github.com:igoralksndr/graphql_music_searcher.git
cd graphql_music_searcher

# Set-up the environment and make migrations
docker-compose run web python3 manage.py makemigrations

# Setup the db
docker-compose run web python3 manage.py migrate

# Seed the db
docker-compose run web python3 manage.py seed_music_searcher

```

Once you have everything done, just run:

```bash
docker-compose up
```

Open your browser and visit [localhost:8000/graphql](http://localhost:8000/graphql) et voilá!