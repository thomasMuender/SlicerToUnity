import numpy as np
from slicer.app import *

class DataSelector:

    def __init__(self):
        print('DataSelector active')



    def getActiveVolumeAsArray(_self):
        layoutManager = slicer.app.layoutManager()
        compositionNodesIDs = []
        for sliceViewName in layoutManager.sliceViewNames():
            compositeNode = layoutManager.sliceWidget(sliceViewName).sliceLogic().GetSliceCompositeNode()
            print(compositeNode.GetBackgroundVolumeID())
            print(compositeNode.GetForegroundVolumeID())
            print(compositeNode.GetForegroundOpacity())
            compositionNodesIDs.append(compositeNode.GetBackgroundVolumeID)

        a = array(compositionNodesIDs[0])
        return a


    def getActiveVolumeAsNumpyArray(_self):
        layoutManager = slicer.app.layoutManager()
        compositionNodesIDs = []
        for sliceViewName in layoutManager.sliceViewNames():
            compositeNode = layoutManager.sliceWidget(sliceViewName).sliceLogic().GetSliceCompositeNode()
            print(compositeNode.GetBackgroundVolumeID())
            print(compositeNode.GetForegroundVolumeID())
            print(compositeNode.GetForegroundOpacity())
            compositionNodesIDs.append(compositeNode.GetBackgroundVolumeID)

        a = np.array(compositionNodesIDs[0])
        return a


    def getROI(self):
        print 'not working'


    def getRuler(self):
        print 'not working'



class Annotation:

    def __init__(self):
        print 'Initalized new Annotation'

    type = 0
    isRuler = False
    isROI = False
    isFiducial = False

    def setType(self, className):
        if className == 'vtkMRMLAnnotationRulerNode':
            self.isRuler = True
            self.type = 0
        elif className == 'vtkMRMLAnnotationROINode':
            self.isROI = True
            self.type = 1
        elif className == 'vtkMRMLMarkupsFiducialNode':
            self.isFiducial = True
            self.type = 2

    def getType(self):
        return self.type


def getAllAnnotations():
    allRulers = slicer.mrmlScene.GetNodesByClass('vtkMRMLAnnotationRulerNode')
    allROIs = slicer.mrmlScene.GetNodesByClass('vtkMRMLAnnotationROINode')
    allFiducials = slicer.mrmlScene.GetNodesByClass('vtkMRMLMarkupsFiducialNode')

    






def getAnnotations():
    listNodeID = 'vtkMRMLAnnotationHierarchyNode1'  # All Annotations List
    annotationHierarchyNode = slicer.mrmlScene.GetNodeByID(listNodeID)
    print annotationHierarchyNode
    annotationIDs = []
    annotationListIDs = []

    i = annotationHierarchyNode.GetNumberOfChildrenNodes()

    while i >= 0:
        print i
        innerList = annotationHierarchyNode.GetNthChildNode(i)
        if innerList is None:
            i -= 1
            continue
        annotationListIDs.append(innerList)
        print 'added ' + str(innerList.GetID()) + ' to annotationListIDs'
        j = innerList.GetNumberOfChildrenNodes() - 1
        i -= 1
        while j >= 0:
            print innerList.GetNthChildNode(j)
            if innerList.GetNthChildNode(j) is None:
                j -= 1
                continue
            if innerList.GetNthChildNode(j).GetAssociatedNode() is None:
                j -= 1
                continue
            annotationIDs.append(innerList.GetNthChildNode(j).GetAssociatedNode())
            print 'added ' + str(innerList.GetNthChildNode(j).GetAssociatedNode().GetID()) + ' to annotationIDs'
            j -= 1


def getROIControlPoints( attrID ):
    attribute = slicer.mrmlScene.GetNodeByID(attrID)
    p1 = [0,0,0] # origin
    p2 = [0,0,0] # radius
    attribute.GetRadiusXYZ(p1)
    attribute.GetXYZ(p2)
    controlPoints = [p1, p2]
    return controlPoints


def getRulerPositions( attrID ):
    attribute = slicer.mrmlScene.GetNodeByID(attrID)
    p1 = [0,0,0] # start point
    p2 = [0,0,0] # end point
    attribute.GetPosition1(p1)
    attribute.GetPosition2(p2)
    positionPoints = [p1, p2]
    return positionPoints


listNodeID = 'vtkMRMLAnnotationHierarchyNode1' # All Annotations List
annotationHierarchyNode = slicer.mrmlScene.GetNodeByID(listNodeID)
print annotationHierarchyNode
annotationIDs = []
annotationListIDs = []

i = annotationHierarchyNode.GetNumberOfChildrenNodes()

while i >= 0 :
    print i
    innerList = annotationHierarchyNode.GetNthChildNode(i)
    if innerList is None:
        i -= 1
        continue
    annotationListIDs.append(innerList)
    print 'added ' + str(innerList.GetID()) + ' to annotationListIDs'
    j = innerList.GetNumberOfChildrenNodes() - 1
    i -= 1
    while j >= 0:
        print innerList.GetNthChildNode(j)
        if innerList.GetNthChildNode(j) is None:
            j -= 1
            continue
        if innerList.GetNthChildNode(j).GetAssociatedNode() is None:
            j -= 1
            continue
        annotationIDs.append(innerList.GetNthChildNode(j).GetAssociatedNode())
        print 'added ' + str(innerList.GetNthChildNode(j).GetAssociatedNode().GetID()) + ' to annotationIDs'
        j -= 1



i = annotationHierarchyNode.GetNumberOfChildrenNodes()
while i >= 0 :
    print i
    i -= 1

