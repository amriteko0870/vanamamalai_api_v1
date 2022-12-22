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
from PIL import Image  
import PIL  
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
from apiApp.models import rootPageStatus
#---------------------------------------- start your views -----------------------------------------------

@api_view(['POST'])
def adminDashboard(request,format=None):
    obj = rootPageStatus.objects.values()

    res = {}
    res['title'] = ["Page title", " Side pages", "Status", "Actions"]
    data = []   

    home = {
            'page_name':'Home Page',
            'page_link':'/admin/home_edit'
           }
    data.append(home)

    vm_temple_data = {
                        'page_name':'Vanamamalai temple',
                        'sub_pages':vanamamalai_temple.objects.values().count(),
                        'status':obj.filter(title__iexact = 'Vanamamalai temple').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(vm_temple_data)

    other_temple_data = {
                        'page_name':'Other temple',
                        'sub_pages':vanamamalai_other_temple.objects.values().count(),
                        'status':obj.filter(title__iexact = 'Other temple').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(other_temple_data) 

    branches_data = {
                        'page_name':'Branches',
                        'sub_pages':vanamamalai_mutt_branches.objects.values().count(),
                        'status':obj.filter(title__iexact = 'Branches').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(branches_data) 

    ponnadikkal_jeeyar_data = {
                        'page_name':'Ponnadikkal Jeeyar',
                        'sub_pages':ponnadikkal_jeeyar.objects.values().count(),
                        'status':obj.filter(title__iexact = 'Ponnadikkal Jeeyar').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(ponnadikkal_jeeyar_data)   

    jeeyar_data = {
                        'page_name':'Jeeyars',
                        'sub_pages':jeeyars.objects.values().count(),
                        'status':obj.filter(title__iexact = 'Jeeyars').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(jeeyar_data)   
  
    education_data = {
                        'page_name':'Education',
                        'sub_pages':vanamamalai_education.objects.values().count(),
                        'status':obj.filter(title__iexact = 'Education').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(education_data) 

    gallery_data = {
                        'page_name':'Gallery',
                        'sub_pages':'1',
                        'status':obj.filter(title__iexact = 'Gallery').values_list('status',flat=True).last(),
                        'page_link':'/admin/home_edit'
                     }
    data.append(gallery_data)

    res['all_page_data'] = data
    return Response(res)
    

@api_view(['GET','PUT'])
def home_page(request,format=None):
   if request.method == 'GET':
      obj = landing_page.objects.values()
      res = {}
      res['pageName'] = 'Home'
      mock_id = 1
      all_sections = []
      for i in obj:
         sub_dict = {}
         sub_dict['section_name'] = 'Section '+str(i['order'])
         sub_dict['section_id'] = i['id']
         section_data = [
                           {  'id':mock_id,
                              'title':'Heading',
                              'content':i['h1'],
                              'type':'text'
                           },
                           {
                              'id':mock_id+1,
                              'title':'Sub Heading',
                              'content':i['h2'],
                              'type':'text'
                           },
                           {
                              'id':mock_id+2,
                              'title':'Brief Info',
                              'content':i['p'],
                              'type':'text'
                           },
                           {
                              'id':mock_id+3,
                              'title':'Cover Image',
                              'content':i['img'].split('|'),
                              'type':'image',
                              'update':False
                           },
                        ]
         mock_id = mock_id + 4
         sub_dict['section_data'] = section_data
         all_sections.append(sub_dict)
      
      res['all_sections'] = all_sections
      return Response(res)
   if request.method == 'PUT':
      data = request.data
      for i in data['all_sections']:
         obj = landing_page.objects.filter(id = i['section_id'])
         print(i['section_data'])
         h1 = i['section_data'][0]['content']
         h2 = i['section_data'][1]['content']
         p = i['section_data'][2]['content']
         return Response(i)
      # return Response(data['all_sections'])


