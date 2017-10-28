import numpy as np
import math
import cv2

from Target import Target

class TargetProcessor:
    def _init_():
        RectHeight = 500
        RectWidth = 200
        focalLen = 486
        horizCent = 200
        vertiCent = 333
    def loadTarget(target):
        imgWidth = target.getWidth()
        imgHeight = target.getHeight()
        imgCenter = target.getCenter()
        RectcentX = imgCenter[0]
        RectcentY = imgCenter[1]
        offsetX = math.fabs(RectcentX - horizCent)
        offsetY = math.fabs(RectcentY - vertiCent)

    def findDistance():
        if imgWidth != None:
            dist = RectWidth * focalLen / imgWidth
            return (dist)

    def findAzimuth():
        if imgWidth != None:
            azimuth = np.arctan(offsetX/ focalLen)*180/math.pi
            return (azimuth)

    def findAltitude():
        if imgWdith != None:
            altit = np.arctan(offsetY/ focalLen)*180/math.pi
            return (altit)
