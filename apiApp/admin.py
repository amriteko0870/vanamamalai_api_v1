from django.contrib import admin
from apiApp.models import landing_page,vanamamalai_temple,gallery_album,gallery_sub_album,gallery_details,gallery_youtube,gallery
from apiApp.models import jeeyars
# Register your models here.

admin.site.register(landing_page)
admin.site.register(vanamamalai_temple)
admin.site.register(gallery_album)
admin.site.register(gallery_sub_album)
admin.site.register(gallery_details)
admin.site.register(gallery_youtube)
admin.site.register(gallery)
admin.site.register(jeeyars)