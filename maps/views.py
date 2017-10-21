# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image


TILE_SIZE = 256


def index(request):
    return render(request, 'maps/index.html', {})


def tile(_, x, y, z):
    fallback = Image.new('RGBA', (TILE_SIZE, TILE_SIZE), (int(x) * 16, int(y) * 16, int(z) * 16, 255))
    try:
        with open(os.path.join(os.path.dirname(__file__), 'static/img/test.png'), 'rb') as png:
            return HttpResponse(png.read(), content_type='image/png')
    except IOError:
        response = HttpResponse(content_type='image/png')
        fallback.save(response, 'PNG')
        return response
