# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Map(models.Model):
    title = models.CharField(max_length=127)
    map_image = models.ImageField()
    max_zoom = models.PositiveSmallIntegerField()
