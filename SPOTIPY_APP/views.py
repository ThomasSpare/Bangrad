from django.shortcuts import render
from django.views import generic, View
from .models import Post
from __future__ import print_function
import json
import spotipy
import time
import sys




# shows acoustic features for tracks for the given artist

if len(sys.argv) > 1:
    tids = sys.argv[1:]
    print(tids)

    start = time.time()
    features = sp.audio_features(tids)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print("features retrieved in %.2f seconds" % (delta,))


#  view post on blog (i think ? )

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
