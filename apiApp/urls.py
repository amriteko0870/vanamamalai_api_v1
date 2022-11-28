
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #-------------------Filters------------------------------------
    path('landingPage',views.landingPage,name='landingPage'),
    path('sideBar',views.sideBar,name='sideBar'),
    path('vn_temple',views.vn_temple,name='vn_temple'),
    
    # path('',views.index,name='landingPage'),

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
