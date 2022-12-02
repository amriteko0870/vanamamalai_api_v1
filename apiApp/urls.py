
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #-------------------Filters------------------------------------
    path('landingPage',views.landingPage,name='landingPage'),
    path('sideBar',views.sideBar,name='sideBar'),
    path('vn_temple',views.vn_temple,name='vn_temple'),
    path('gallery_page',views.gallery_page,name='gallery_page'),
    path('sub_album_page',views.sub_album_page,name='sub_album_page'),
    path('all_sub_album_page',views.all_sub_album_page,name='all_sub_album_page'),
    path('jeeyars',views.jeeyars_parampara,name='jeeyars_parampara'),

    path('other_temple',views.other_temple,name='other_temple'),
    path('branches',views.branches,name='branches'),
    path('ponnadikkal_jeeyar',views.ponnadikkal_jeeyar,name='ponnadikkal_jeeyar'),
    
    
    
    
    
    
    path('',views.index,name='index'),

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
