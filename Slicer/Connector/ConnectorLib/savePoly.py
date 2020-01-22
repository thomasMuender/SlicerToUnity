def savePoly():

    nodes = slicer.util.getNodesByClass('vtkMRMLSegmentationNode') # Segmentation _nodes_
    s = []  # array of segmentations
    sno = []  # array of segmentation _segments_
    polys = [] # _polyData_ of segments
    for i in range(len(nodes)):
        s.append(nodes[i].GetSegmentation())

    for node in s:
        if node.GetNumberOfSegments() > 0:
            for i in range(node.GetNumberOfSegments()):
                sno.append(node.GetNthSegmentID(i))

    for i in range(len(nodes)):
        if nodes[i].GetSegmentation().GetNumberOfSegments() > 0:
            for poly in range(len(sno)):
                polys.append(nodes[i].GetClosedSurfaceRepresentation(sno[poly]))

#####

''' slicer.util.getNodesByClass('vtkMRMLSegmentationNode')
n = getNode("Segmentation_1")

s = n.GetSegmentation()

s.GetNumberOfSegments()
>> 2
s.GetNthSegmentID(1)
n.GetClosedSurfaceRepresentation('Segment_2') #polydata

#(vtkCommonDataModelPython.vtkPolyData)0x146393db8
'''
