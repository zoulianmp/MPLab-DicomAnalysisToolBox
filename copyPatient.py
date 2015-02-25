#!/usr/bin/python

# AUTHOR:  Derek M. Tishler
# SCRIPT:  copyPatient.py
# SUMMARY: Generate new set of Dicom images that will easily load into GEANT4 Dicom importer
# DATE:    5/21/2012

"""
Take invalid Dicom file and copy nessecary data to fresh dicom set with proper headers.
"""

import dicom as dcm
from dicom.dataset import Dataset, FileDataset
import dicom.UID
import numpy as np

#location of patient we need to fix
patientDir = "../../decimal/DCM_CMS_Rescan/"

#Lets make a slice location array
#L = np.arange(-54,258,3)

#We need to fix all the dicom images in the folder
fileNames = []
for i in L:
	fileNames.append(patientDir+"CT.rtp1.1.0889608.DECIMAL.T.%.0f.CT.dcm" % i)

#Number of slices in patient
n = len(fileNames)

print("Number of slices: %i" % n)

#Create each dcm file and copy data from ^^
for i in range(n):

    dsOld = dicom.read_file(fileNames[i], force=True) #force required??? Talk to Ken.

    filename = r"%i.dcm" % (i+1)

    # Following 10 lines adapted from pydicom makenew.py examaple: Darcy Mason. 
    # Populate required values for file meta information
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID    = '1.2.840.10008.5.1.4.1.1.2' # CT Image Storage
    file_meta.MediaStorageSOPInstanceUID = "1.2.3" # !! Need valid UID here for real work
    file_meta.ImplementationClassUID     = "1.2.3.4" # !!! Need valid UIDs here
        
    # Create the FileDataset instance (initially no data elements, but file_meta supplied)
    ds = FileDataset(filename, {}, file_meta=file_meta, preamble="\0"*128)

    ds.SpecificCharacterSet       = dsOld.SpecificCharacterSet
    ds.ImageType                  = dsOld.ImageType
    ds.SOPInstanceUID             = dsOld.SOPInstanceUID
    ds.SOPClassUID                = dsOld.SOPClassUID
    ds.StudyDate                  = dsOld.StudyDate
    ds.StudyTime                  = dsOld.StudyTime
    ds.StudyInstanceUID           = dsOld.StudyInstanceUID
    ds.SeriesInstanceUID          = dsOld.SeriesInstanceUID
    ds.StudyID                    = dsOld.StudyID
    ds.SeriesNumber               = dsOld.SeriesNumber
    #Reverse order for viewing standard.
    ds.InstanceNumber             = dsOld.InstanceNumber
    ds.FrameofReferenceUID        = dsOld.FrameofReferenceUID

    ds.Modality                   = dsOld.Modality
    ds.Manufacturer               = dsOld.Manufacturer
    #ds.InstitutionName            = dsOld.InstitutionName
    
    # Add the data elements -- not trying to set all required here. Check DICOM standard
    ds.PatientsName = dsOld.PatientsName
    ds.PatientID   = dsOld.PatientID
    ds.PatientsBirthDate = dsOld.PatientsBirthDate
    ds.PatientsSex = dsOld.PatientsSex
    ds.PatientAge = 0#dsOld.PatientAge
    ds.SliceThickness = dsOld.SliceThickness
    #ds.SpacingBetweenSlices = dsOld.SpacingBetweenSlices
    ds.PatientPosition = dsOld.PatientPosition

    #Image info (check need in ct modality
    ds.ImagePositionPatient = dsOld.ImagePositionPatient
    ds.ImageOrientationPatient = dsOld.ImageOrientationPatient
    ds.FrameofReferenceUID = dsOld.FrameofReferenceUID
    ds.SliceLocation = dsOld.SliceLocation
    ds.PixelSpacing = dsOld.PixelSpacing
    ds.SamplesperPixel = dsOld.SamplesperPixel
    ds.PhotometricInterpretation = dsOld.PhotometricInterpretation
    ds.Rows =  dsOld.Rows
    ds.Columns = dsOld.Columns
    ds.BitsAllocated = dsOld.BitsAllocated
    ds.BitsStored = dsOld.BitsStored
    ds.HighBit = dsOld.HighBit
    ds.PixelRepresentation = dsOld.PixelRepresentation
    #ds.WindowCenter = dsOld.WindowCenter
    #ds.WindowWidth = dsOld.WindowWidth
    ds.RescaleIntercept = dsOld.RescaleIntercept
    ds.RescaleSlope = dsOld.RescaleSlope

    # create 2d image of air HU
    ds.pixel_array = dsOld.pixel_array
    ds.PixelData   = dsOld.PixelData
        
    # Set the transfer syntax
    ds.is_little_endian = True
    ds.is_implicit_VR   = True

    ds.SequenceDelimiter = 0
        
    ds.save_as(filename)
