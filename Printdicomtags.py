


import sys
import dicom





folder = "C:\\Users\\zoulian\\Desktop\\magicalphantomtest"

filename = "\\EcliseTPS.CT.5.phantom.dcm"

path1 = folder + filename

#dataset = dicom.read_file(path1)

dataset = dicom.read_file(path1,force=True)

print dataset





        
        