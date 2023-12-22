"""
    ### Dicom Image To Png Files and Headers by Okrie
    #### View DCM 
    Author : Okrie
    Version : 0.1
    site : https://github.com/Okrie/DicomToPng
    Created : 2023.12.22
    Last Updated : 2023.12.22
"""

import matplotlib.pyplot as plt
from pydicom import dcmread, multival
import numpy as np

# View Image
def viewDCM(filename, arr):
    """
    ### View Dicom Image by MatPlotLib
    """

    plt.title(filename)
    plt.imshow(arr, cmap='gray')
    plt.show()


# Save Pixel_data to Image File
def saveTopng(filename, arr, dpi=500, type='png'):
    """
    ### Dcm Image to Png    
    require : filename, arr    
    arr : dicom pixel_data    
    default dpi : 1000    
    default type : png    
    """ 

    plt.axis('off')
    plt.imshow(arr, cmap='gray')
    plt.savefig(f'{filename}.{type}', dpi=dpi, transparent=True)


# Load pixel_data with Dicom Header
def loadFile(filename, i):
    """
    ### DCM Convert pixel_data      
    require : fileName, i      
    i : 1 (pixel_data), 2 (Dicom Header)     
    information : Check Header data and convert pixel_data
    """

    ds = dcmread(filename + '.dcm', force=True)
    if ds is None:
        raise Exception('File Exits')
    pixel_array = ds.pixel_array

    img = ds.pixel_array.astype(np.float32)

    # Noramalization
    img = (img / (2 ** ds.BitsStored))

    # Convert Rescale
    if(('RescaleSlope' in ds) and ('RescaleIntercept' in ds)):
        pixel_array = (pixel_array * ds.RescaleSlope) + ds.RescaleIntercept

    if('WindowCenter' in ds):
        if(type(ds.WindowCenter) == multival.MultiValue):
            window_center = float(ds.WindowCenter[0])
            window_width = float(ds.WindowWidth[0])
            lwin = window_center - (window_width / 2.0)
            rwin = window_center + (window_width / 2.0)
        else:    
            window_center = float(ds.WindowCenter)
            window_width = float(ds.WindowWidth)
            lwin = window_center - (window_width / 2.0)
            rwin = window_center + (window_width / 2.0)
    else:
        lwin = np.min(pixel_array)
        rwin = np.max(pixel_array)
        
        
    pixel_array[np.where(pixel_array < lwin)] = lwin
    pixel_array[np.where(pixel_array > rwin)] = rwin
    pixel_array = pixel_array - lwin

    if(ds.PhotometricInterpretation == 'MONOCHROME1'):
        pixel_array[np.where(pixel_array < lwin)] = lwin
        pixel_array[np.where(pixel_array > rwin)] = rwin
        pixel_array = pixel_array - lwin
        pixel_array = 1.0 - pixel_array

    else:
        pixel_array[np.where(pixel_array < lwin)] = lwin
        pixel_array[np.where(pixel_array > rwin)] = rwin
        pixel_array = pixel_array - lwin

    if i == 1:
        return pixel_array
    elif i == 2:
        return ds