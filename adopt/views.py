# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import random

def index(request):
    i = random.random()
    return HttpResponse(f'Hi! How are you {i}!!!')
