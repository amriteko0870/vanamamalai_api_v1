import numpy as np
import pandas as pd
import time
from datetime import datetime as dt
import datetime
import re
from operator import itemgetter 
import os
import random
#-------------------------Django Modules---------------------------------------------
from django.http import Http404, HttpResponse, JsonResponse,FileResponse
from django.shortcuts import render
from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField
from django.db.models import F,Func,Q
from django.db.models import Value as V
from django.db.models.functions import Concat,Cast,Substr
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Min, Max
from django.db.models import Subquery
from django.db.models.functions import Lower, Replace
#----------------------------restAPI--------------------------------------------------
from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response

#----------------------------models---------------------------------------------------
from apiApp.models import landing_page,vanamamalai_temple
from apiApp.models import gallery,gallery_album,gallery_details,gallery_sub_album,gallery_youtube
from apiApp.models import jeeyars

#-----------------------------extra -----------------------------------------------------
from apiApp.extra import navbar_extra_data,other_temple_extra,branches_extra,ponnadikkal_jeeyar_extra

@api_view(['GET'])
def landingPage(request,format=None):
    data = landing_page.objects.annotate(
                                        seq_no = Concat(V('landing_page_'),Cast('order',CharField()),output_field=CharField()),
                                        ).values()
    n_data = pd.DataFrame(data)
    n_data['img'] = n_data['img'].str.split('|')
    res = n_data.to_dict(orient='records')
    for i in res:
        while '' in i['img']:
            i['img'].remove('')
    return Response({
                    'message':'True',
                    'data':res
                   })


@api_view(['GET'])
def sideBar(request,format=None):
    navbar = []

    home = {
            "main_link": {
                        "link_name": "Home",
                        "link_path": "/",
                       },
           }
    navbar.append(home)
    vn_temple = {
                 "main_link":{
                              "link_name": "Vanamamalai Temple",
                              "link_path": "/sub_page/vanamamalai_temple/temple_history",
                             },
                }
    vn_sub_links = vanamamalai_temple.objects.annotate(
                                                        sub_link_name = F('content_title'),
                                                        # link_name = Lower(Replace('content_title', V(' '), V('_')),output_field=CharField()),
                                                        sub_link_path = Concat(V('/sub_page/vn_temple/'),Cast('id',CharField()),output_field=CharField())
    ).values('id','sub_link_name','sub_link_path')
    vn_temple['main_link']['link_path'] = vn_sub_links[0]['sub_link_path'] 
    vn_temple['sub_links'] = vn_sub_links
    navbar.append(vn_temple)
    
    d = navbar_extra_data()
    for i in d:
        navbar.append(i)
    
    jeeyar = {
                'main_link': {
                            'link_name': "Jeeyars",
                            'link_path': "/jeeyars",
                            }
              }
    navbar.append(jeeyar)

    gallery = {
                'main_link': {
                            'link_name': "Gallery",
                            'link_path': "/gallery",
                            }
              }
    navbar.append(gallery)
    return Response(navbar)

@api_view(['POST'])
def vn_temple(request,format=None):
    id = request.data['id']
    res = {}
    obj = vanamamalai_temple.objects.filter(id = id).values().last()
    banner = {
                'heading':'Vanamamalai Temple',
                'image': obj['banner_image']
             }
    res['banner'] = banner

    content = {
                'title':obj['content_title'],
                'sub_title':obj['content_subtitle'],
                'image':obj['content_image']
              }
    res['content'] = content

    tab_data = []
    
    tab1 = {
            'name':obj['tab1_heading']
           }
    tab1_content = []
    for i in range(len(obj['tab1_desc'].split('|'))):
        tab1_content.append({'data':obj['tab1_desc'].split('|')[i],'type':obj['tab1_schema'].split('|')[i]})
    tab1['content'] = tab1_content
    

    tab2 = {
            'name':obj['tab2_heading']
           }
    tab2_content = []
    for i in range(len(obj['tab2_desc'].split('|'))):
        tab2_content.append({'data':obj['tab2_desc'].split('|')[i],'type':obj['tab2_schema'].split('|')[i]})
    tab2['content'] = tab2_content


    tab3 = {
            'name':obj['tab3_heading']
           }
    tab3_content = []
    for i in range(len(obj['tab3_desc'].split('|'))):
        tab3_content.append({'data':obj['tab3_desc'].split('|')[i],'type':obj['tab3_schema'].split('|')[i]})
    tab3['content'] = tab3_content


    tab4 = {
            'name':obj['tab4_heading']
           }
    tab4_content = []
    for i in range(len(obj['tab4_desc'].split('|'))):
        tab4_content.append({'data':obj['tab4_desc'].split('|')[i],'type':obj['tab4_schema'].split('|')[i]})
    tab4['content'] = tab4_content

    tab_data.append(tab1)
    tab_data.append(tab2)
    tab_data.append(tab3)
    tab_data.append(tab4)

    res['tab_data'] = tab_data

    return Response(res)

@api_view(['GET'])
def gallery_page(request,format=None):
    res = {}

    obj = gallery_details.objects.values().last()
    banner = {
                "heading": obj['banner_heading'],
                'image': obj['banner_image'] 
             }
    res['banner'] = banner

    obj = gallery_youtube.objects.annotate(
                                            video_title = F('title'),
                                            video_id = F('url')
                                          ).values('video_title','video_id')
    res['carousel_data'] = obj

    content = []
    albums = gallery_album.objects.values_list('album_name','id')
    for i in albums:
        d = {
              'title' : i[0],
              'id':i[1]
            }
        content_data = gallery_sub_album.objects.filter(album_name = i[0])\
                                        .annotate(
                                                    year = F('sub_album_name'),
                                                    image = F('sub_album_image')
                                                 )\
                                        .values('year','image')
        d['content_data'] = content_data

        content.append(d)
    res['content'] = content

    return Response(res)
    
@api_view(['POST'])
def sub_album_page(request,format=None):
    sub_album_name = request.data['sub_album_name']
    album_id  = request.data['album_id']
    album_name = gallery_album.objects.filter(id = album_id).values().last()['album_name']
    res = {}

    obj = gallery_details.objects.values().last()
    banner = {
                "heading": obj['banner_heading'],
                'image': obj['banner_image'] 
             }
    res['banner'] = banner

    obj = gallery_sub_album.objects.filter(sub_album_name = sub_album_name,album_name = album_name).values().last()

    res['title'] = obj['sub_album_name']
    
    album_banner = {
                    'p': obj['sub_album_details'],
                    'image': obj['sub_album_image']
                   }
    res['album_banner'] = album_banner

    content = gallery.objects.filter(sub_album_name = sub_album_name,album_name = album_name)\
                             .annotate(
                                        sub_heading = F('name'),
                             ).values('sub_heading','image','details')
    res['content'] = content
    return Response(res)

@api_view(['POST'])
def all_sub_album_page(request,format=None):
    album_id  = request.data['album_id']
    album_name = gallery_album.objects.filter(id = album_id).values().last()['album_name']
    res = {}

    obj = gallery_details.objects.values().last()
    banner = {
                "heading": obj['banner_heading'],
                'image': obj['banner_image'] 
             }
    res['banner'] = banner

    res['title'] = album_name

    res['id'] = album_id

    content = gallery_sub_album.objects.filter(album_name = album_name)\
                                       .annotate(
                                                 sub_heading = F('sub_album_name'),
                                                 image = F('sub_album_image')
                                                ).values('sub_heading','image')

    res['content'] = content

    return Response(res)


@api_view(['GET'])
def jeeyars_parampara(request,format=None):
    res = {}
    res['title'] = "Jeeyar Paramapara"
    jeeyar = jeeyars.objects.values('id','image','name','prefix','start_date','end_date','jeeyar_no','jeeyar_no_suffix')
    res['jeeyars'] = jeeyar
    return Response(res)


@api_view(['POST'])
def other_temple(request,format=None):
    id = request.data['id']
    res = other_temple_extra(int(id))
    return Response(res)

@api_view(['POST'])
def branches(request,format=None):
    id = request.data['id']
    res = branches_extra(int(id))
    return Response(res)

@api_view(['POST'])
def ponnadikkal_jeeyar(request,format=None):
    res = ponnadikkal_jeeyar_extra()
    return Response(res)



@api_view(['GET'])
def index(request):
    # l = [['Shri Ramanuja alias Sri Udayavar','AD','1017','',1,'st'],
    #     ['Shri Manavala Maamunigal','AD','1370','',2,'nd'],
    #     ['Ponnadikkal Jeeyar','AD','1447','1482','3','rd'],
    #     ['Sri Chendalangara Ramanuja Jeer Swami','AD','1502','1520',4,'th'],
    #     ['Sri Rengappa Ramanuja Swami','AD','1520','1586',5,'th']]

    # for i in l:
    #     print('name :',i[0])
    #     print('prefix :',i[1])
    #     print('start_date :',i[2])
    #     print('end_date :',i[3])
    #     print('jeeyar_no :',i[4])
    #     print('jeeyar_no_sufix :',i[5])
    #     print()
    #     data = jeeyars(
    #                                 name = i[0],
    #                                 prefix = i[1],
    #                                 start_date = i[2],
    #                                 end_date = i[3],
    #                                 jeeyar_no = i[4],
    #                                 jeeyar_no_suffix = i[5],
    #                                 image = 'media/img/jeeyars/sample.svg',
    #                             )
    #     data.save()
    return Response('sample')
