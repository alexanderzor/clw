# -*- coding: utf-8
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Text(models.Model):
    number = models.IntegerField(blank=True, null=True)
    description = RichTextField(blank=True)
    #date = models.DateField(default=timezone.now())
    #verbose_title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='scc/images/', blank=True)

    def __str__(self):
        return 'Текстовый урок ' + str(self.number)
    class Meta:
        verbose_name = "Текстовые уроки"

class Task(models.Model):
    title = models.CharField(max_length=20, unique=True)

    #video = models.FileField(upload_to='video/', blank=True)
    date = models.DateField(default=timezone.now())

    author = models.CharField(max_length=50, blank=True)
    private = models.BooleanField(default=False, blank=True)
    url = models.URLField(blank=True)
    text = models.ForeignKey(Text, null=True)
    #verbose_title = models.CharField(max_length=50, blank=True)
    number = models.IntegerField(blank=True, null=True)
    #description = RichTextField(blank=True)
    #image = models.ImageField(upload_to='scc/images/', blank=True)

    def _keyword(self):
        return str(self.title) + str(self.author) + str(self.date)

    #keyword = models.CharField(max_length=60, default=_keyword)
    class Meta:
        verbose_name = "Видео"
        ordering = ['-date']

class Consultant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=40)
    skype = models.CharField(max_length=40)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/consultants/')
    active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Консультанты"
