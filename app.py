"""
    ### Dicom Image To Png Files and Headers by Okrie
    #### DCM Program
    Author : Okrie
    Version : 0.1
    site : https://github.com/Okrie/DicomToPng
    Created : 2023.12.22
    Last Updated : 2023.12.22
"""

from module import viewDcm, recontrol

def viewMenu():
    print("======================SELECT MENU======================")
    print("== 1. View DCM")
    print("== 2. View DCM Information")
    print("== 3. View pixel Data")
    print("== 4. Save DCM")
    print("== 99. Exit")
    print("=======================================================")


def __main__():
    menu = 0
    while True:
        while True:
            # Print Menu
            if menu == 0:
                try:
                    viewMenu()
                    menu = int(input("Input Menu Number : "))
                except Exception as e:
                    
                    print("Retry Input Number")
            elif menu != 0:
                # View DCM
                if menu == 1:
                    filename = str(input("Input File Name : "))
                    result = viewDcm.loadFile(filename, 1)
                    viewDcm.viewDCM(filename, result)
                
                # View DCM Information
                elif menu == 2:
                    filename = str(input("Input File Name : "))
                    ds = viewDcm.loadFile(filename, 2)
                    print("View DCM Information")
                    print(ds)

                # View Pixel Data
                elif menu == 3:
                    filename = str(input("Input File Name : "))
                    result = recontrol.convertPixel(filename)
                    print(result)
                
                # Save DCM
                elif menu == 4:
                    filename = str(input("Input File Name : "))
                    result = viewDcm.loadFile(filename, 1)
                    viewDcm.saveTopng(filename, result)
                
                # Exit Program
                elif menu == 99:
                    exit()

                else:
                    pass
                
                print('Done')
                menu = 0
                break

            else:
                print("Wrong Menu Number")
                menu = 0

if __name__ == '__main__':
    __main__()