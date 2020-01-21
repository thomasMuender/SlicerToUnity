import numpy as np


class DataSelector:

    def __init__(self):
        print('DataSelector active')






# input = '/Users/thomasmildner/Documents/02_Projekte/2020/ProjectWeek/AnonymousPatient_10'
#
# loadedVolumeNode = slicer.util.loadVolume('input')
#
# """
# The following can be pasted into the python console to examine the headers
# of all the dicom objects in the database
# """
#
# import DICOMLib
# import numpy as np
#
# parent = qt.QWidget()
# layout = qt.QVBoxLayout()
# parent.setLayout(layout)
#
# slider = ctk.ctkSliderWidget()
#
# header = DICOMLib.DICOMHeaderWidget(parent)
#
# layout.addWidget(slider)
# layout.addWidget(header.widget)
# parent.show()
#
# db = slicer.dicomDatabase
# patients = []
# study = []
# series = []
# files = []
#
# patient_id = 0
#
#
# for patient in db.patients():
#     for st in db.studiesForPatient(patient):
#         for se in db.seriesForStudy(st):
#             for f in db.filesForSeries(se):
#                 files.append(db.filesForSeries(f))
#             series.append(files)
#             #files = []
#         study.append(series)
#         #series = []
#    patients.append(study)
#    patient_id += 1
#
#
# for patient in patients:
#    for st in study:
#        for se in series:
#            arrayFromVolume(series)
#            print 'Image: \t' + str(se)
#
#
# slider.decimals = 0
# slider.maximum = len(files)-1
# callback = lambda v: header.setHeader(files[int(v)])
# slider.connect('valueChanged(double)',callback)
#
# dcmdump + textBrowser option
# textBrowser = qt.QTextBrowser()
# layout.addWidget(textBrowser)
#
# callback = lambda v: textBrowser.setText(str(DICOMLib.DICOMCommand('dcmdump', [files[int(v)]] ).start()))
# slider.connect('valueChanged(double)',callback)
#
