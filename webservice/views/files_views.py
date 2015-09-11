import json
from django.http import HttpResponse, StreamingHttpResponse
from webservice.views import setting_views
from django.views.decorators.http import condition
import os

import re
import pdb
from uuid import uuid4

import time

import urllib
import urlparse
import pprint

# ------------------------------------
avoid = ['$RECYCLE.BIN']


# ------------------------------------


def get_files(request, folders=None):
    settings = setting_views.open_file_settings()

    if folders is None:
        folders = settings['folders']
    else:
        folders = [urllib.unquote_plus(folders)]

    final = []

    for folder in folders:
        tmpssub = []
        for root, subdirs, files in os.walk(folder):
            for sub in subdirs:
                if secure_dir(sub):
                    tmpssub.append(sub)

            final.append([trace_navigation(root), tmpssub, files])
            break

    return setting_views.send_response(final)


def trace_navigation(root):
    sroot = root;
    splitroot = root.split("/")

    trace = "<a href='#' ng-click='findChildren(\""+splitroot[0] + '/' + splitroot[1]+"\")'>"+splitroot[0] + '/' + splitroot[1]+"</a>"

    return trace


'''

    function traceNavigation (root){
        console.log(root);
        var sroot = root;
        var splitroot = root.split("/");

        var trace = "<a href='#' ng-click='findChildren(\""+splitroot[0] + '/' + splitroot[1]+"\")'>"+splitroot[0] + '/' + splitroot[1]+"</a>";

        console.log(trace);

        /*for(var i = 2; i < splitroot.length; i++){

        }*/




        return trace;
    };
'''



def secure_dir(dir):
    if dir not in avoid:
        return True
    else:
        return False


def ordering(array):
    for a in array:
        if isinstance(a, list):
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
            if re.search('\.' + audio + '$', file):
                aud.append([delete_extension(file), audio])
        for video in videos:
            if re.search("\." + video + '$', file):
                vid.append([delete_extension(file), video])

    return [aud, vid]


def delete_extension(file):
    return file.split('.')[0]
