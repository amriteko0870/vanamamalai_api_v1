from django.db import models

# Create your models here.

class landing_page(models.Model):
    order = models.IntegerField(blank=True)
    h1 = models.CharField(max_length=2000,blank=True)
    h2 = models.CharField(max_length=2000,blank=True)
    p = models.CharField(max_length=2000,blank=True)
    img = models.TextField(blank=True)
    read_link = models.TextField(blank=True)
    yt_link = models.TextField(blank=True)
    file_link = models.TextField(blank=True)
    yt_title = models.CharField(max_length=2000,blank=True)
    file_title = models.CharField(max_length=2000,blank=True)
    layout = models.CharField(max_length=2000,blank=True)

#-------------------------------------------------------------------------------
class vanamamalai_temple(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()
    content_title = models.TextField()
    content_subtitle = models.TextField()
    content_image = models.TextField()

class vanamamalai_temple_tab(models.Model):
    temple_id = models.IntegerField()
    tab_heading = models.TextField()
    tab_desc = models.TextField()

#----------------------------------------------------------------------------------
class vanamamalai_other_temple(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()
    content_title = models.TextField()
    content_subtitle = models.TextField()
    content_image = models.TextField()

class vanamamalai_other_temple_tab(models.Model):
    temple_id = models.IntegerField()
    tab_heading = models.TextField()
    tab_desc = models.TextField()

#-----------------------------------------------------------------------------------
class vanamamalai_mutt_branches(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()
    content_title = models.TextField()
    content_subtitle = models.TextField()
    content_image = models.TextField()

class vanamamalai_mutt_branches_tab(models.Model):
    branch_id = models.IntegerField()
    tab_heading = models.TextField()
    tab_desc = models.TextField()

#------------------------------------------------------------------------------------
class ponnadikkal_jeeyar(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()
    content_title = models.TextField()
    content_subtitle = models.TextField()
    content_image = models.TextField()

class ponnadikkal_jeeyar_tab(models.Model):
    jeeyar_id = models.IntegerField()
    tab_heading = models.TextField()
    tab_desc = models.TextField()

#------------------------------------------------------------------------------------
class thaniyans_and_vazhi_thirunamams(models.Model):
    pass

#------------------------------------------------------------------------------------
class vanamamalai_education(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()
    content_title = models.TextField()
    content_subtitle = models.TextField()
    content_image = models.TextField()

class vanamamalai_education_tab(models.Model):
    education_id = models.IntegerField()
    tab_heading = models.TextField()
    tab_desc = models.TextField()

#------------------------------------------------------------------------------------
class gallery_album(models.Model):
    album_name = models.TextField()

class gallery_sub_album(models.Model):
    album_name = models.TextField()
    sub_album_name = models.TextField()
    sub_album_image = models.TextField()
    sub_album_details = models.TextField()

class gallery_details(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()

class gallery_youtube(models.Model):
    title = models.TextField()
    url = models.TextField()

class gallery(models.Model):
    album_name = models.TextField()
    sub_album_name = models.TextField()
    image = models.TextField()
    name = models.TextField()
    details = models.TextField()

#---------------------------------------------------------------------
class jeeyars(models.Model):
    name = models.TextField()
    prefix = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()
    jeeyar_no_suffix = models.TextField()
    image = models.TextField()
    jeeyar_no = models.IntegerField()
    banner_image = models.TextField()
    banner_heading = models.TextField()


class jeeyars_tab(models.Model):
    jeeyar_id = models.IntegerField()
    tab_heading = models.TextField()
    tab_desc = models.TextField()

