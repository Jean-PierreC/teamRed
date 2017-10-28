import numpy as np
import math
import cv2

from Target import Target

class TargetProcessor:
    def _init_():
        None = None
        RectHeight = 500
        RectWidth = 200
        RectcentX = None
        RectcentY = None
        focalLen = 480
        minX = 0
        minY = 0
        maxX = 3333333
        maxY = 3333333
        imgWidth = 10
        imgHeight = 22
        horizCent = 200
        vertiCent = 333
        offsetX = abs(RectcentX - horizCent)
        offsetY = abs(RectcentY - vertiCent) 
    def loadTarget():


    def findDistance():
        if imgWidth != None:
            dist = RectWidth * focalLen / imgWidth
            print (dist)

    def findAzimuth():
        if imgWidth != None:
            azimuth = np.arctan(offsetX/ focalLen)*180/math.pi
            print (azimuth)

    def findAltitude():
        if imgWdith != None:
            altit = np.arctan(offsetY/ focalLen)*180/math.pi
            print (altit)
