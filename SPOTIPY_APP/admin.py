from django.contrib import admin
from .models import LodgeForum, Discussion, BangradSearchFields

admin.site.register(BangradSearchFields)
admin.site.register(LodgeForum)
admin.site.register(Discussion)
