
from dicom.UID import  pydicom_root_UID, generate_uid

import sys
import dicom



borrowuidroot = '2.16.840.1.114337.'

pydicomroot = '1.2.826.0.1.3680043.8.498.'





uid = generate_uid()

uid_brrow1= generate_uid(prefix=borrowuidroot)

uid_brrow2= generate_uid(prefix=borrowuidroot)
uid_brrow3= generate_uid(prefix=borrowuidroot)
uid_brrow4= generate_uid(prefix=borrowuidroot)





folder = "C:\\Users\\zoulian\\Desktop\\magicalphantomtest"

filename = "\\Vscan.CT.1.phantom.dcm"

path1 = folder + filename

#dataset = dicom.read_file(path1)

dataset = dicom.read_file(path1,force=True)

print dataset





        
        