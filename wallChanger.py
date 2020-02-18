import os
import requests
import json
from random import randint
from os import listdir
from os.path import isfile, join
import subprocess as sp
from gi.repository import Gio

class Wallpaper:
    def __init__(self):
        #see instructions to get client_id from UnSplash: https://api.unsplash.com/
        self.client_id = "INSERT YOUR CLIENT_ID HERE"
        self.PAGE_MIN_VAL = 0
        self.PAGE_MAX_VAL = 65
        self.MIN_IMG_COUNT = 0
        #Available types: raw, regular, full, small, thumb
        self.IMG_TYPE = "regular"
        self.path= "YOUR/PATH/TO/BACKGROUND/FOLDER/"
        self.SCHEMA = 'org.gnome.desktop.background'
        self.KEY = 'picture-uri'
        self.gsettings = Gio.Settings.new(self.SCHEMA)

        self.downloadBackground()

    def getURL(self):
        PAGE_NUM = str(randint(self.PAGE_MIN_VAL, self.PAGE_MAX_VAL))
        url = 'https://api.unsplash.com/search/photos?page='+PAGE_NUM+'&query=nature&client_id='+self.client_id
        return url

    def getURLContent(self):
        res = requests.get(self.getURL())
        content = json.loads(res.text)
        return content

    def getImgLink(self):
        content = self.getURLContent()
        MAX_IMG_COUNT = len(content["results"])

        RES_INDEX = randint(self.MIN_IMG_COUNT, MAX_IMG_COUNT)

        IMG_LINK = content["results"][RES_INDEX]["urls"][self.IMG_TYPE]

        return IMG_LINK

    def downloadBackground(self):
        fileName = "Background.jpg"
        self.path += fileName
        sp.run("curl -o {} {}".format(self.path, self.getImgLink()), shell=True)
        self.setBackground()

    def setBackground(self):
        self.gsettings.set_string(self.KEY, self.path)


wall = Wallpaper()
