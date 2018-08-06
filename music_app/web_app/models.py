# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db import models



class BlogPosts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Titles =  models.CharField(max_length=100)
    Description = models.TextField()
    BlogImage = models.FileField(upload_to='Blog/Images/', blank=False, null=True)
    PublishedDate = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        Title = str(self.Title)
        return Titles


#Genre class
class GenreType(models.Model):
    Genre = models.CharField(max_length=50)

    def __unicode__(self):
        Genre = str(self.Genre)
        return Genre


#Artist class
class ArtistType(models.Model):
    GenreType = models.ForeignKey(GenreType, related_name="GenreTypes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Name = models.CharField(max_length=100)
    Born  = models.DateTimeField(auto_now=True, auto_now_add=False)
    Bio = models.TextField()
    DateJoined = models.DateTimeField(blank=True, null=True)
    Artist = models.FileField(upload_to='Genre/Artist/', blank=False, null=True)


    def __unicode__(self):
        Name = str(self.Name)
        return Name

#Album class
class AlbumType(models.Model):
    ArtistName = models.ForeignKey(ArtistType, related_name="ArtistTypes")
    AlbumName = models.CharField(max_length=100)
    AlbumCover = models.FileField(upload_to='Genre/Artist/Album/', blank=False, null=True)
    YearReleased = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        AlbumName = str(self.AlbumName)
        return AlbumName


#Song class
class SongType(models.Model):
    AlbumNames = models.ForeignKey(AlbumType, related_name="AlbumTypes")
    SongName = models.CharField(max_length=100)
    Song = models.FileField(upload_to='Genre/Artist/Album/Song/', blank=False, null=True)
    ReleaseDate = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        SongName = str(self.SongName)
        return SongName
