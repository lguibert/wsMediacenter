import json
from django.http import HttpResponse, StreamingHttpResponse
from webservice.views import setting_views
from django.views.decorators.http import condition
import os

import re
import pdb

import time


def get_files(request):
    settings = setting_views.open_file_settings()
    folders = settings['folders']

    #daddy = [None, [],[],[]]
    tmpsfile = []
    tmpssub = []
    rootfolder = None
    for folder in folders:
        for root, subdirs, files in os.walk(folder):
            tmpssub.append(subdirs)
            tmpsfile.append(files)
            rootfolder = root
            break

    #plus pour le rangement
    '''
    final = []
    for tmp in tmps:
        if tmp not in final:
            match = re.search("\.[a-z]{1,4}$", tmp)
            if match :
                final.append(tmp)

    final = classify_files(final)
    '''

    tmpssub = ordering(unnuller(tmpssub))

    return setting_views.send_response([tmpssub, tmpsfile, rootfolder])


def ordering(array):
    for a in array:
        a.sort()

    return array

def unnuller(array):
    tmp = []
    for i, a in enumerate(array):
        if a:
            tmp.append(array[i])

    return tmp


def classify_files(files):
    settings = setting_views.open_file_settings()
    audios = settings['audioFormats']
    videos = settings['videoFormats']

    aud = []
    vid = []

    for file in files:
        for audio in audios:
            if re.search('\.'+audio+'$', file):
                aud.append([delete_extension(file), audio])
        for video in videos:
            if re.search("\."+video+'$', file):
                vid.append([delete_extension(file), video])

    return [aud, vid]

def delete_extension(file):
    return file.split('.')[0]