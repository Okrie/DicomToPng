"""
    ### Dicom Image To Png Files and Headers by Okrie
    #### pixelData Controller
    Author : Okrie
    Version : 0.1
    site : https://github.com/Okrie/DicomToPng
    Created : 2023.12.22
    Last Updated : 2023.12.22
"""

import numpy as np
import os

# byte to ndarray
def Recontrol(co, arrdType, arrShape):
    """
        ### Recontrol
        Reshape Array
    """
    
    convertArray = np.frombuffer(co, dtype=arrdType)
    arrRes = np.reshape(convertArray, arrShape)
    return arrRes

# Convert Pixel data
def convertPixel(filename):
    """
        ### convertPixel
    """

    paths = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/'

    f = open(paths+filename+'.dcm', 'rb')
    tempdata = bytes(f.read())
    f.close()

    f = open(paths+filename+'.txt', 'w')
    f.write(str(tempdata))
    f.close()

    return tempdata