# -*- coding: utf-8 -*-
import json
#import re
from django.http import HttpResponse
#from urllib import unquote


#----------------------------- GLOBALS VARIABLES -----------------------------
settingFile = "C:/projects/wsMediacenter/webservice/assets/settings.json"
#----------------------------- -----------------------------

def open_file_settings():
    return json.load(open(settingFile))

def get_settings(request):
    try:
        return send_response(open_file_settings())
    except:
        return send_response(error_messages(2))

def get_setting(request, setting):
    file = open_file_settings()
    return send_response(file[setting])

def add_setting(request, category, value):
    file = open_file_settings()
    category = check_category(category)
    if value not in file[category]:
        file[category].append(value)
        update_file(file)
        return send_response(open_file_settings())
    else:
        return send_response(error_messages(1,value), 405)


def delete_setting(request, category, value):
    file = open_file_settings()
    category = check_category(category)
    data = file[category]

    print "La valeur est: ",value

    for d in data:
        if d == value:
            data.remove(d)
            break

    update_file(file)

    return send_response(open_file_settings())

def check_category(category):
    return {
        'folder' : 'folders',
        'video' : 'videoFormats',
        'audio' : 'audioFormats'
    }.get(category,None)


def send_response(data, code=200):
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response.status_code = code
    response["Access-Control-Allow-Origin"] = "*"
    return response


def update_file(file):
    with open(settingFile, 'r+') as outfile:
        outfile.seek(0)
        outfile.write(json.dumps(file, indent=4))
        outfile.truncate()


def error_messages(id_message, value=''):

    messages = {
        0 : "Une erreur est survenue du cote serveur.",
        1 : "Erreur: "+value+ "existe deja.",
        2 : "Erreur lors de l\'ouverture du fichier de configuration."
    }

    return messages.get(id_message)