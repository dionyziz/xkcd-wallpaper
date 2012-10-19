import os
from ctypes import windll
from win32con import *
from PIL import Image
import xkcd
import random

# This function is by AKM licensed under the BSD license
# 
def setWallPaperFromBmp( pathToBmp ):
    result = windll.user32.SystemParametersInfoA(
        SPI_SETDESKWALLPAPER, 0,
        pathToBmp,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

def setWallPaper( pathToImage ):
    bmpImage = Image.open( pathToImage )
    newPath = os.getcwd()
    newPath = os.path.join( newPath, 'pywallpaper.bmp' )
    bmpImage.save( newPath, 'BMP' )
    setWallPaperFromBmp( newPath )

maxNum = xkcd.Comic( 0 ).num
choice = random.randint( 1, maxNum )
import urllib

url = xkcd.Comic( choice ).img
urllib.urlretrieve( url, 'xkcd.jpg' )

setWallPaper( 'xkcd.jpg' )
