# -*- coding: utf-8 -*-
import os
import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
from .models import Map
from office.settings import MEDIA_ROOT


TILE_SIZE = 256


def index(request):
    return render(request, 'maps/index.html', {
        'maps': Map.objects.all()
    })


def map(request, pk):
    return render(request, 'maps/map.html', {
        'map_json_data': json.dumps(
            get_map_data(Map.objects.get(pk=pk))
        )
    })


def get_map_data(map_data):
    fields = serializers.serialize('python', [map_data])[0].get('fields')
    fields['width'] = map_data.map_image.width
    fields['height'] = map_data.map_image.height
    return fields


def tile(_, pk, x, y, z):
    map_data = Map.objects.get(pk=pk)
    image = Image.open(os.path.join(MEDIA_ROOT, map_data.map_image.path))
    # image = image.resize((image.width << int(z), image.height << int(z)))
    image = image.crop((
        TILE_SIZE * int(x),
        TILE_SIZE * int(y),
        TILE_SIZE * (int(x) + 1),
        TILE_SIZE * (int(y) + 1)
    ))
    response = HttpResponse(content_type='image/png')
    image.save(response, 'PNG')
    return response
