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


class vanamamalai_temple(models.Model):
    banner_image = models.TextField()
    banner_heading = models.TextField()
    content_title = models.TextField()
    content_subtitle = models.TextField()
    content_image = models.TextField()
    tab1_heading = models.TextField()
    tab1_desc = models.TextField()
    tab1_schema = models.TextField()
    tab2_heading = models.TextField()
    tab2_desc = models.TextField()
    tab2_schema = models.TextField()
    tab3_heading = models.TextField()
    tab3_desc = models.TextField()
    tab3_schema = models.TextField()
    tab4_heading = models.TextField()
    tab4_desc = models.TextField()
    tab4_schema = models.TextField()

class vanamamalai_other_temple(models.Model):
    pass

class vanamamalai_mutt_branches(models.Model):
    pass

class ponnadikkal_jeeyar(models.Model):
    pass

class jeeyar_parampara(models.Model):
    pass

class thaniyans_and_vazhi_thirunamams(models.Model):
    pass

class vanamamalai_education(models.Model):
    pass


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