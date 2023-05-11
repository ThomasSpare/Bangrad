from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View


class SpotifySearch(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
