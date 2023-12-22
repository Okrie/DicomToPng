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
import base64
from pydicom import dcmread

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
def convertPixel(filename, type='b'):
    """
        ### convertPixel
    """

    paths = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/'
    
    if(type == 'b'):
        f = open(paths+filename+'.dcm', 'rb')
        ds = bytes(f.read())
        f.close()

        f = open(paths+filename+'.txt', 'w')
        f.write(str(ds))
        f.close()
    else:
        ds = dcmread(paths + filename + '.dcm')
        f = open(paths + filename + '.json', 'w')
        f.write(str(ds.to_json()))
        f.write(str(','))
        f.write(str({'base64' : base64.b64encode(ds.pixel_array)}).replace("'", '"'))
        f.close()

    return ds