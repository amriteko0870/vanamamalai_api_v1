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
                #  "call_link":"vn_temple",
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




# def index(request):
#     album_name = 'album 2'
#     sub_album_name = '2022'
#     image = 'media/gallery/image.png'
#     image_name = 'image name'
#     details = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime assumenda rerum iusto atque, mollitia ab ipsum sapiente debitis blanditiis voluptatum eligendi'

#     for i in range(5):
#         data = gallery(
#                         album_name = album_name,
#                         sub_album_name = sub_album_name,
#                         image = image,
#                         name = image_name + ' ' + str(i+1),
#                         details = details,
#         )
#         data.save()
#     return HttpResponse('Hello')

# @api_view(['GET'])
# def index(request,format=None):
#     landing_page.objects.
#     landingPageData = [
#     {
#       'id': "landing_section_01",
#       'h1': "SRI VANAMAMALAI (THOTHADRI) MUTT",
#       'h2': "SRI VANACHALA MAHAMUNI PARAMPARA",
#       'p': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean pellentesque quam vitae ornare porta. Vivamus pretium eleifend risus laoreet pretium. Ut sit amet finibus metus, nec cursus lacus.",
#       'img': ["static/img/first_section_image.png"],
#       'read_link': '',
#       'yt_link': '', 
#       'file_link': '',
#       'yt_title': '',#
#       'file_title': '',#
#       'layout': "hero",
#     },

#     {
#       'id': "landing_section_02",
#       'h1': "Sri Vanamamalai divyadesam",
#       'h2': "Sri varamangai nachiyar sametha sri deivanayaga perumal",
#       'p': "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.",
#       'img': [""],
#       'read_link': '',#
#       'yt_link': '',#
#       'file_link': '',#
#       'yt_title': '',#
#       'file_title': '',#
#       'layout': "event",
#     },

#     {
#       'id': "landing_section_03",
#       'h1': "SRI VANAMAMALAI DIVYADESAM",
#       'h2': "SRI VARAMANGAI NACHIYAR SAMETHA SRI DEIVANAYAGA PERUMAL",
#       'p': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean pellentesque quam vitae ornare porta. Vivamus pretium eleifend risus laoreet pretium. Ut sit amet finibus metus, nec cursus lacus.",
#       'img': ["static/img/second_section_img_1.png","static/img/second_section_img_2.png"],
#       'read_link': '',
#       'yt_link': '',
#       'file_link': '',
#       'yt_title': '',
#       'file_title': '',
#       'layout': "two_images",
#     },

#     {
#       'id': "landing_section_04",
#       'h1': "'PONNADIKKAL JEEYAR' WHO ESTABLISHED THE VANAMAMALAI MUTT",
#       'h2': '',
#       'p': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod odio dicta, temporibus magnam ea eius quas iure illo consequuntur nostrum tempore laudantium, blanditiis, minima possimus velit? Id perspiciatis, dolores reiciendis aspernatur voluptate quod consectetur rerum. Quos, voluptatem. Harum error quis sapiente itaque, magnam dolores tenetur repellat labore adipisci ab at numquam iure accusantium minima reprehenderit dolorum est, eum soluta nesciunt facere temporibus. Adipisci debitis rerum assumenda necessitatibus iure inventore temporibus minus distinctio sed omnis culpa magni ducimus, similique ab esse natus officia facilis earum accusantium maxime officiis! Labore animi impedit fuga recusandae alias, voluptate repellendus suscipit consequatur assumenda quidem qui et sunt facere rerum doloribus beatae mollitia asperiores cumque nesciunt vitae nemo corporis blanditiis nobis? Error dolores quas",
#       'img': ["statc/img/ zthird_section_image.png"],
#       'read_link': '',
#       'yt_link': '',
#       'file_link': '',
#       'yt_title': "WATCH PONNADIKKAL JEEYAR'S PRAPATHI & MANGALASASANAM",
#       'file_title': "THANIYAN AND VAZHI THIRUNAMAM",
#       'layout': "right_image",
#     },

#     {
#       'id': "landing_section_05",
#       'h1': "SRI MADHURAKAVI VANAMAMALAI RAMANUJA JEEYAR SWAMI - 31ST",
#       'h2': '',
#       'p': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum accusantium magnam commodi explicabo hic laborum quae, id repellat. Magni nobis rerum inventore delectus in molestiae? Est amet commodi atque nam delectus. Ipsum molestiae ipsa consequuntur inventore quibusdam repellat praesentium consequatur harum facere cupiditate soluta iste, non quos voluptas dignissimos velit ut incidunt eligendi aspernatur quidem aperiam odio, nisi quam doloremque? Ad eos incidunt distinctio ut facilis quidem hic error quaerat? Facilis quod assumenda inventore distinctio molestias. Rerum, aliquid. Aliquid molestiae fuga necessitatibus expedita, officiis possimus rem debitis doloremque repellendus officia, iusto nobis ullam sequi dolorem et impedit doloribus accusamus. Fugit quisquam delectus ratione modi quos illum cupiditate, totam enim officia consequuntur et repellat. Provident unde at eius odit molestias commodi quod, ipsum perferendis dicta! Nesciunt, eligendi asperiores ab cupiditate eum doloremque obcaecati aperiam vero inventore corporis laborum",
#       'img': ["static/img/forth_section_image.png"],
#       'read_link': '',
#       'yt_link': '',
#       'file_link': '',
#       'yt_title': "WATCH PONNADIKKAL JEEYAR'S PRAPATHI & MANGALASASANAM",
#       'file_title': "THANIYAN AND VAZHI THIRUNAMAM",
#       'layout': "right_image",
#     },

#     {
#       'id': "landing_section_06",
#       'h1': "SRI VANAMAMALAI DIVYADESAM",
#       'h2': "SRI VARAMANGAI NACHIYAR SAMETHA SRI DEIVANAYAGA PERUMAL",
#       'p': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestiae eveniet vel, qui voluptatibus magnam quis. Aliquid iusto nobis, dignissimos minima suscipit, aliquam eum accusantium quam distinctio ipsa explicabo blanditiis veritatis accusamus inventore cupiditate, quia porro. Qui animi vitae ipsum, laborum explicabo autem blanditiis sit ad nisi cupiditate facere, provident amet cum reiciendis veritatis aperiam possimus consectetur! Fugiat tempore qui perferendis veritatis quibusdam odit rem, labore placeat facere",
#       'img': ["static/img/fithsection_image_1.png","static/img/fithsection_image_2.png"],
#       'read_link': '',
#       'yt_link': '',
#       'file_link': '',
#       'yt_title': '',
#       'file_title': '',
#       'layout': "two_images",
#     },
#     ]
#     for i in range(len(landingPageData)):
#         data = landing_page(order = i+1,
#                             h1 = landingPageData[i]['h1'],
#                             h2 = landingPageData[i]['h2'],
#                             p = landingPageData[i]['p'],
#                             img = landingPageData[i]['img'],
#                             read_link = landingPageData[i]['read_link'],
#                             yt_link = landingPageData[i]['yt_link'],
#                             file_link = landingPageData[i]['file_link'],
#                             yt_title = landingPageData[i]['yt_title'],
#                             file_title = landingPageData[i]['file_title'],
#                             layout = landingPageData[i]['layout'])
#         data.save()
#         print(i+1)
#         print(landingPageData[i]['h1'])
#         print(landingPageData[i]['h2'])
#         print(landingPageData[i]['p'])
#         print(landingPageData[i]['img'])
#         print(landingPageData[i]['read_link'])
#         print(landingPageData[i]['yt_link'])
#         print(landingPageData[i]['file_link'])
#         print(landingPageData[i]['yt_title'])
#         print(landingPageData[i]['file_title'])
#         print(landingPageData[i]['layout'])
#         print()

        
#     return HttpResponse('Hello world')













