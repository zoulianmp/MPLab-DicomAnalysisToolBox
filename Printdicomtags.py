from dicom.UID import  pydicom_root_UID, generate_uid
import time
        
StudyInstanceUID =  generate_uid()
time.sleep(0.156)

SeriesInstanceUID = generate_uid()
time.sleep(0.156)

FrameofReferenceUID =  generate_uid()



print StudyInstanceUID
print SeriesInstanceUID
print FrameofReferenceUID

import sys
import dicom





folder = "C:\\Users\\zoulian\\Desktop\\magicalphantomtest"

filename = "\\EcliseTPS.CT.1.phantom.dcm"

path1 = folder + filename

#dataset = dicom.read_file(path1)

dataset = dicom.read_file(path1,force=True)

print dataset





        
        