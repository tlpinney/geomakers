from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
import os, re


class UserProfile(models.Model):
    # This line is required.  Links UserProfile to a User model instance.
    user = models.OneToOneField(User, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.URLField(default="", null=True, blank=True)
    twitter = models.URLField(default="", null=True, blank=True)
    linkedin = models.URLField(default="", null=True, blank=True)
    picture = models.ImageField(upload_to="images", null=True, blank=True, default=settings.STATIC_URL+"skyshaker/img/user/default.jpg")
    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return os.path.split(self.image.name)[1]

class Tag(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

class Link(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

class Video(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    embed = models.TextField(default="",null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

class MakerSpace(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    lon = models.DecimalField(max_digits=8, decimal_places=5)
    url = models.URLField(default="", null=True, blank=True)

class Project(models.Model):
    owner = models.OneToOneField(User, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    abstract = models.TextField()
    location = models.CharField(max_length=200)
    links = models.ManyToManyField('Link', blank=True)
    videos = models.ManyToManyField('Video', blank=True)
    images = models.ManyToManyField('Image', blank=True)
    rating = models.IntegerField(default='3',null=True, blank=True)
    ratingAsString = models.TextField(null=True, blank=True)
    typeOfProject = models.CharField(max_length=200,null=True, blank=True, choices=(("GeoDream","GeoDream"),("GeoRecipe","GeoRecipe"),("GeoBoost","GeoBoost")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, editable=True)
    related = models.ManyToManyField('self', blank=True)
    def __str__(self):
        return self.title

def updateVideoEmbed(sender, instance, **kwargs):
    instance_url = str(instance.url)
    if 'youtube' in instance_url:
        idOfYoutubeVideo = re.search('(?<=v=)\w+', instance_url).group(0)
        instance.embed = '<iframe width="560" height="315" src="//www.youtube.com/embed/' + idOfYoutubeVideo + '" frameborder="0" allowfullscreen></iframe>'
    elif 'vimeo' in instance.url:
        idOfVimeoVideo = re.search('(?<=com/)\w+', instance_url).group(0)
        instance.embed = '<iframe src="//player.vimeo.com/video/' + idOfVimeoVideo + '" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>'
    post_save.disconnect(updateVideoEmbed, sender=Video)
    instance.save()
    post_save.connect(updateVideoEmbed, sender=Video)

def updateRatingAsString(sender, instance, **kwargs):
    ratingAsString = ""
    for i in range(0,instance.rating):
        ratingAsString += "<span class='star starFilled'>&#9733;</span>"
    for i in range(0,5-instance.rating):
        ratingAsString += "<span class='star starUnfilled'>&#9734;</span>"
    instance.ratingAsString = ratingAsString
    post_save.disconnect(updateRatingAsString, sender=Project)
    instance.save()
    post_save.connect(updateRatingAsString, sender=Project)

# register the signal
post_save.connect(updateVideoEmbed, sender=Video)
post_save.connect(updateRatingAsString, sender=Project) 
