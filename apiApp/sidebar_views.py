import numpy as np
import pandas as pd
import time
from datetime import datetime as dt
import datetime
import re
from operator import itemgetter 
import os
import random
import simplejson as json
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
from apiApp.models import landing_page,vanamamalai_temple,vanamamalai_temple_tab
from apiApp.models import gallery,gallery_album,gallery_details,gallery_sub_album,gallery_youtube
from apiApp.models import jeeyars,jeeyars_tab
from apiApp.models import vanamamalai_other_temple,vanamamalai_other_temple_tab
from apiApp.models import vanamamalai_mutt_branches,vanamamalai_mutt_branches_tab
from apiApp.models import ponnadikkal_jeeyar,ponnadikkal_jeeyar_tab
from apiApp.models import vanamamalai_education,vanamamalai_education_tab

#----------------------------start you views-----------------------------------------------


@api_view(['GET'])
def sideBar(request,format=None):
    navbar = []

    home = {
            "main_link": {
                        "link_name": "Home",
                        "link_path": "/home",
                        "link_code":'home'
                       },
           }
    navbar.append(home)
    vn_temple = {
                 "main_link":{
                              "link_name": "Vanamamalai Temple",
                              "link_code": "vn_temple"
                             },
                }
    vn_sub_links = vanamamalai_temple.objects.annotate(
                                                        link_code = V('vn_temple'),
                                                        sub_link_name = F('content_title'),
                                                        # link_name = Lower(Replace('content_title', V(' '), V('_')),output_field=CharField()),
                                                        sub_link_path = Concat(V('/sub_page/vn_temple/'),Cast('id',CharField()),output_field=CharField())
    ).values('id','sub_link_name','sub_link_path','link_code')
    vn_temple['main_link']['link_path'] = vn_sub_links[0]['sub_link_path'] 
    vn_temple['sub_links'] = vn_sub_links
    navbar.append(vn_temple)

    

    vn_other_temple = {
                 "main_link":{
                              "link_name": "Other Temple",
                              "link_code": "other_temple"

                             },
                }
    vn_sub_links = vanamamalai_other_temple.objects.annotate(
                                                        link_code = V('other_temple'),
                                                        sub_link_name = F('content_title'),
                                                        # link_name = Lower(Replace('content_title', V(' '), V('_')),output_field=CharField()),
                                                        sub_link_path = Concat(V('/sub_page/other_temple/'),Cast('id',CharField()),output_field=CharField())
    ).values('id','sub_link_name','sub_link_path','link_code')
    vn_other_temple['main_link']['link_path'] = vn_sub_links[0]['sub_link_path'] 
    vn_other_temple['sub_links'] = vn_sub_links
    navbar.append(vn_other_temple)


    vn_branches = {
                 "main_link":{
                              "link_name": "Branches",
                              "link_code": "branches"
                             },
                }
    vn_sub_links = vanamamalai_mutt_branches.objects.annotate(
                                                        link_code = V('branches'),
                                                        sub_link_name = F('content_title'),
                                                        # link_name = Lower(Replace('content_title', V(' '), V('_')),output_field=CharField()),
                                                        sub_link_path = Concat(V('/sub_page/branches/'),Cast('id',CharField()),output_field=CharField())
    ).values('id','sub_link_name','sub_link_path','link_code')
    vn_branches['main_link']['link_path'] = vn_sub_links[0]['sub_link_path'] 
    vn_branches['sub_links'] = vn_sub_links
    navbar.append(vn_branches)
    
    pon_jeeyar = {
                    "main_link": {
                                    "link_name": "Ponnadikkal Jeeyar",
                                    "link_path": "/sub_page/ponnadikkal_jeeyar/1",
                                    "link_code": "ponnadikkal_jeeyar"

                                 },
                 }
    navbar.append(pon_jeeyar)           
    jeeyar = {
                'main_link': {
                            'link_name': "Jeeyars",
                            'link_path': "/jeeyars",
                            "link_code": "/jeeyars"

                            }
              }
    navbar.append(jeeyar)

    vn_edu = {
                 "main_link":{
                              "link_name": "Education",
                              "link_code": "vn_education"
                              
                             },
                }
    vn_sub_links = vanamamalai_education.objects.annotate(
                                                        link_code = V('vn_education'),
                                                        sub_link_name = F('content_title'),
                                                        # link_name = Lower(Replace('content_title', V(' '), V('_')),output_field=CharField()),
                                                        sub_link_path = Concat(V('/sub_page/vn_education/'),Cast('id',CharField()),output_field=CharField())
    ).values('id','sub_link_name','sub_link_path','link_code')
    vn_edu['main_link']['link_path'] = vn_sub_links[0]['sub_link_path'] 
    vn_edu['sub_links'] = vn_sub_links
    navbar.append(vn_edu)

    gallery = {
                'main_link': {
                            'link_name': "Gallery",
                            'link_path': "/gallery",
                            "link_code": "/gallery"
                            }
              }
    navbar.append(gallery)
    return Response(navbar)