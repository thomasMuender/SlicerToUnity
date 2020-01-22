import numpy as np
from slicer.app import *

def savePoly():

    segtion = []  # array of segmentations
    segment = []  # array of segmentation _segments_
    polys = [] # _polyData_ of segments

    segnodes = slicer.util.getNodesByClass('vtkMRMLSegmentationNode')  # Segmentation _nodes_

    for i in range(len(segnodes)):
        segtion.append(segnodes[i].GetSegmentation())
        if segnodes[i].GetSegmentation().GetNumberOfSegments() > 0:
            for j in range(node.GetNumberOfSegments()):
                polys.append(segnodes[i].GetClosedSurfaceRepresentation(node.GetNthSegmentID(j)))


### longer version of code above

    '''
    for i in range(len(segnodes)):
        segtion.append(segnodes[i].GetSegmentation())
    
    for node in segtion:
        if node.GetNumberOfSegments() > 0:
            for i in range(node.GetNumberOfSegments()):
                segment.append(node.GetNthSegmentID(i))
    
    for i in range(len(segnodes)):
        if segnodes[i].GetSegmentation().GetNumberOfSegments() > 0:
            for poly in range(len(segment)):
                polys.append(segnodes[i].GetClosedSurfaceRepresentation(segment[poly]))'''

##### from slicer testing

''' slicer.util.getNodesByClass('vtkMRMLSegmentationNode')
n = getNode("Segmentation_1")

s = n.GetSegmentation()

s.GetNumberOfSegments()
>> 2
s.GetNthSegmentID(1)
n.GetClosedSurfaceRepresentation('Segment_2') #polydata

#(vtkCommonDataModelPython.vtkPolyData)0x146393db8
'''
