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

#--------------------------- extra -------------------------------------------------
from apiApp.admin_pages.image_upload import image_upload
from apiApp.admin_pages.layout import layoutCreation,addTab
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
                        'page_link':'/admin/sub_admin_page/vn_temple_edit/'
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

    res['all_page_data'] = data[:2]
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
         sub_dict['status'] = i['show_status']
         section_data = [
                           {  'id':mock_id,
                              'title':'Heading',
                              'content':i['h1'],
                              'type':'text',
                              'link_status': True,
                           },
                           {
                              'id':mock_id+1,
                              'title':'Sub Heading',
                              'content':i['h2'],
                              'type':'text',
                              'link_status': False if i['layout'] in ['left_image','right_image'] else True

                           },
                           {
                              'id':mock_id+2,
                              'title':'Brief Info',
                              'content':i['p'],
                              'type':'text',
                              'link_status': True,
                           },
                           {
                              'id':mock_id+3,
                              'title':'Cover Image',
                              'content':i['img'].split('|'),
                              'type':'image',
                              'link_status': True,
                           },
                           {
                              'id':mock_id+4,
                              'title':'Background Color',
                              'content':i['background_color'],
                              'type':'color',
                              'link_status': False if i['layout'] in ['hero'] else True
                           },
                           {
                              'id':mock_id+5,
                              'title':'Youtube',
                              'content_title':i['yt_title'],
                              'content':i['yt_link'],
                              'type':'yt_link',
                              'link_status': True if i['layout'] in ['left_image','right_image'] else False
                           },
                           {
                              'id':mock_id+6,
                              'title':'PDF',
                              'content_title':i['file_title'],
                              'content':[i['file_link']],
                              'type':'file',
                              'link_status': True if i['layout'] in ['left_image','right_image'] else False
                           },
                           
                        ]
         mock_id = mock_id + 7
         sub_dict['section_data'] = section_data
         all_sections.append(sub_dict)
      
      res['all_sections'] = all_sections
      return Response(res)
   if request.method == 'PUT':
      data = request.data

      for i in data['all_sections']:
         obj = landing_page.objects.filter(id = i['section_id']).values().last()
         h1 = i['section_data'][0]['content']
         h2 = i['section_data'][1]['content']
         p = i['section_data'][2]['content']
         image = '|'.join(i['section_data'][3]['content'])
         background_color = i['section_data'][4]['content']
         yt_link = i['section_data'][5]['content']
         yt_title = i['section_data'][5]['content_title']
         file_link = i['section_data'][6]['content'][0]
         file_title =i['section_data'][6]['content_title']

         landing_page.objects.filter(id = i['section_id']).update(
                                                                     h1 = h1,
                                                                     h2 = h2,
                                                                     p = p,
                                                                     img = image,
                                                                     background_color = background_color,
                                                                     yt_link = yt_link,
                                                                     file_link = file_link,
                                                                     yt_title = yt_title,
                                                                     file_title = file_title,
                                                                  )
      res = {
               'status':True,
               'data':data
            }
      return Response()



@api_view(['POST','DELETE','PUT'])
def addSectionLandingPage(request,format=None):
   if request.method == 'POST':
      layout_type = request.data['layout_type']
      last_order = landing_page.objects.aggregate(max = Max('order'))['max']
      if layoutCreation(last_order,layout_type):
         res = {
                  'status': True,
                  'message':'new section created',
               }
      else:
         res = {
                  'status': False,
                  'message':'invalid layout type',
               }
      return Response(res)
   if request.method == 'DELETE':
      section_id = request.data['section_id']
      landing_page.objects.filter(id = section_id).delete()
      res = {
               'status':True,
               'message':'section deleted successfully'
            }
      return Response(res)
   if request.method == 'PUT':
      section_id = request.data['data']['section_id']
      current_status = request.data['data']['current_status']
      if current_status:
         landing_page.objects.filter(id = section_id).update(show_status = False)
      else:
         landing_page.objects.filter(id = section_id).update(show_status = True)

      res = {
               'status':True,
               'message':'section status changed successfully'
            }
      return Response(res)


@api_view(['GET','PUT','POST','DELETE','PATCH'])
def vn_temple_edit(request,format=None):
   page_id = request.GET.get('page_id')
   if page_id != None:
      if request.method =="GET":
         obj = vanamamalai_temple.objects.filter(id = page_id).values().last()
         tab_obj = list(vanamamalai_temple_tab.objects.filter(temple_id = page_id)\
                                                .annotate(
                                                            tab_name = F('tab_heading'),
                                                            tab_id = F('id'),
                                                            tab_data = F('tab_desc')
                                                ).values('tab_name','tab_id','tab_data','show_status'))
         res = {}
         res['page_id'] = page_id
         res['pageName'] = obj['banner_heading']
         res['subPageName'] = obj['content_title']
         res['heading'] = obj['content_title']
         res['subheading'] = obj['content_subtitle']
         res['content_image'] = obj['content_image']
         
         c = 1
         for i in tab_obj:
            i['tab_data'] = eval(i['tab_data'])
            for j in i['tab_data']:
               j['id'] = 'bf'+str(c)
               c = c + 1
         res['all_tabs'] = tab_obj
         res['new_id'] = c   
         return Response(res)
      
      if request.method == 'PUT':
         data = request.data
         page_id = data['page_id']
         heading = data['heading']
         subheading = data['subheading']
         content_image = data['content_image']
         vanamamalai_temple.objects.filter(id = page_id).update(
                                                                  content_title = heading,
                                                                  content_subtitle = subheading,
                                                                  content_image = content_image,
                                                               )
         for i in data['all_tabs']:
            tab_show_status = i['show_status']
            tab_name = i['tab_name']
            tab_id = i['tab_id']
            tab_desc = str(i['tab_data'])
            vanamamalai_temple_tab.objects.filter(temple_id = page_id,id = tab_id)\
                                          .update(
                                                   tab_heading = tab_name,
                                                   tab_desc = tab_desc,
                                                   show_status = tab_show_status,
                                                 )
         res = {
                  'status':True,
                  'message':'Updation successfull'
         }
         return Response(res)
      
      if request.method == 'POST':
         page_id = request.data['page_id']
         
         data = vanamamalai_temple_tab(
                                    temple_id = page_id,
                                    tab_heading = 'New Tab',
                                    tab_desc = "[{'data': 'Lorem ipsum', 'type': 'text'}]",
                                    show_status = False,
                               )
         data.save()
         res = {
                  'status': True,
                  'message': 'new tab created successfully'
               }
         return Response(res)

      if request.method == 'PATCH':
         tab_id = request.data['data']['tab_id']
         obj = vanamamalai_temple_tab.objects.filter(id = tab_id).values()
         if obj.last()['show_status']:
            obj.update(show_status = False)
         else:
            obj.update(show_status = True)
         res = {
                  'status' : True,
                  'message': 'tab show status updated successfully',
               }
         return Response(res)

      if request.method == "DELETE":
         tab_id = request.data['tab_id']
         vanamamalai_temple_tab.objects.filter(id = tab_id).delete()
         res = {
                  'status':True,
                  'message':' tab deleted successfully',
               }
         return Response(res)

   else:
      if request.method == 'GET':
         obj = vanamamalai_temple.objects.values()
         res = {}
         res['pageName'] = obj.first()['banner_heading']
         mock_id = 1
         all_input_fields = [
                              {
                                 'content': obj.first()['banner_heading'],
                                 'id': mock_id,
                                 'title': "Heading",
                                 'type': "text",
                              },
                              {
                                 'content': obj.first()['banner_image'].split(','),
                                 'id': mock_id+1,
                                 'title': "Banner Image",
                                 'type': "image",
                                 },
                           ]
         res['all_input_fields'] = all_input_fields
         sub_page_list = obj.annotate(
                                          subpage_name = Lower(F('content_title')),
                                          subpage_link = Concat(
                                                                  V('/admin/sub_admin_page/vn_temple_edit/'),
                                                                  Cast('id',CharField()),
                                                                  output_field=CharField()
                                                               )
                                       )\
                           .values('id','subpage_name','subpage_link','show_status')
         res['sub_page_list'] = sub_page_list
         return Response(res)

      if request.method == 'PUT':
         data = request.data
         banner_heading = data['all_input_fields'][0]['content']
         banner_image = ''.join(data['all_input_fields'][1]['content'])
         vanamamalai_temple.objects.all().update(
                                                   banner_image = banner_image,
                                                   banner_heading = banner_heading,
                                                )
         res = {
                  'status':True,
                  'message':'Updation successfull',
               }
         return Response(res)

      if request.method == 'POST':
         data = vanamamalai_temple(
                                       banner_image = '',
                                       banner_heading = 'Vanamamalai Temple',
                                       content_title = 'New Section',
                                       content_subtitle = '', 
                                       content_image = '',
                                       show_status = False,
                                    )
         data.save()
         res = {
                  'status':True,
                  'message':'new section created successfully',
               }
         return Response(res)

      if request.method == 'DELETE':
         data = request.data
         vanamamalai_temple.objects.filter(id = data['id']).delete()
         vanamamalai_temple_tab.objects.filter(temple_id = data['id']).delete()
         res = {
               'status':True,
               'message':'deleted successfully',
            }
         return Response(data)

      if request.method == 'PATCH':
         data = request.data['data']
         obj = vanamamalai_temple.objects.filter(id = data['id']).values()
         if obj.last()['show_status']:
            obj.update(show_status = False)
         else:
            obj.update(show_status = True)
         res = {
               'status':True,
               'message':'status changed successfully',
            }
         return Response(res)      

@api_view(['POST'])
def adminAddNewTabData(request,format=None):
   id = request.data['id']
   type1 =request.data['type']
   array = eval(request.data['dataArray'])[0]
   tab_id = eval(request.data['tabId'])[0]

   page_data = request.data['pageData'].replace('true','True')
   page_data = page_data.replace('false','False')
   page_data = eval(page_data)
   
   res = addTab(id,type1,array)
   for i in page_data['all_tabs']:
      if i['tab_id'] == tab_id:
         i['tab_data'] = res
         break

   return Response(page_data)


@api_view(['POST'])
def addImageTabDataAdmin(request,format=None):
   file = request.FILES['file']
   id = request.data['id']
   array = eval(request.data['dataArray'])[0]
   tab_id = eval(request.data['tabId'])[0]

   page_data = request.data['pageData'].replace('true','True')
   page_data = page_data.replace('false','False')
   page_data = eval(page_data)
   
   img_path = 'img/'
   upload_res = image_upload(file,img_path)
   updated_value = 'media/'+upload_res
   array.append({
                  'data':updated_value,
                  'type':'image',
                  'id':'bf'+str(id)

               })
   for i in page_data['all_tabs']:
      if i['tab_id'] == tab_id:
         i['tab_data'] = array
         break


   return Response(page_data)