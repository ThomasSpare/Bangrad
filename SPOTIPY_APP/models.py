from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import spotipy


# Example code for spotipy for dev site


class SpotifySearch(models.Model):
    input = 'q'
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify(
        client_credentials_manager=os.environ.get(
            ["SPOTIPY_CLIENT_ID"], ["SPOTIPY_CLIENT_SECRET"])

    results=spotify.artist_albums(birdy_uri, album_type='album')
    albums=results['items']
    while results['next']:
        results=spotify.next(results)
        albums.extend(results['items'])
    for album in albums:
        print(album['name'])


STATUS=((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    author=models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image=CloudinaryField('image', default='placeholder')
    excerpt=models.TextField(blank=True)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS, default=0)
    likes=models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering=["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)

    class Meta:
        ordering=["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
