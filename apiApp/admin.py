from django.contrib import admin
from apiApp.models import landing_page,vanamamalai_temple,gallery_album,gallery_sub_album,gallery_details,gallery_youtube,gallery
from apiApp.models import vanamamalai_temple_tab
from apiApp.models import vanamamalai_other_temple,vanamamalai_other_temple_tab
from apiApp.models import jeeyars,jeeyars_tab
# Register your models here.

admin.site.register(landing_page)
admin.site.register(vanamamalai_temple)
admin.site.register(gallery_album)
admin.site.register(gallery_sub_album)
admin.site.register(gallery_details)
admin.site.register(gallery_youtube)
admin.site.register(gallery)
admin.site.register(jeeyars)
admin.site.register(vanamamalai_temple_tab)
admin.site.register(vanamamalai_other_temple)
admin.site.register(vanamamalai_other_temple_tab)
admin.site.register(jeeyars_tab)