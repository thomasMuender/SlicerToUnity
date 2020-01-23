import numpy as np
from slicer.app import *

class ActiveVolumeelector:

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

    type = 0
    isRuler = False
    isROI = False
    isFiducial = False
    controlPoints = []
    className = ''
    id = ''

    def __init__(self, attrID):
        self.id =  attrID
        self.className = slicer.mrmlScene.GetNodeByID(attrID).GetClassName()
        if attrID is '':
            print 'No Attribute ID has been given.'
            pass

        if self.className == 'vtkMRMLAnnotationRulerNode':
            self.isRuler = True
            self.type = 0
            self._setRulerPositions()
            print 'Set Annotation Type: RULER'
        elif self.className == 'vtkMRMLAnnotationROINode':
            self.isROI = True
            self.type = 1
            self._setROIControllPoints()
            print 'Set Annotation Type: ROI'
        elif self.className == 'vtkMRMLMarkupsFiducialNode':
            self.isFiducial = True
            self.type = 2
            self._setFiducialPosition()
            print 'Set Annotation Type: FIDUCIAL'

    def _setROIControllPoints(self):
        attribute = slicer.mrmlScene.GetNodeByID(self.id)
        p1 = [0, 0, 0]  # origin
        p2 = [0, 0, 0]  # radius
        attribute.GetRadiusXYZ(p1)
        attribute.GetXYZ(p2)
        self.controlPoints = [p1, p2]

    def _setRulerPositions(self):
        attribute = slicer.mrmlScene.GetNodeByID(self.id)
        p1 = [0, 0, 0]  # start point
        p2 = [0, 0, 0]  # end point
        attribute.GetPosition1(p1)
        attribute.GetPosition2(p2)
        self.controlPoints = [p1, p2]

    def _setFiducialPosition(self):
        attribute = slicer.mrmlScene.GetNodeByID(self.id)
        p1 = [0,0,0]    # single fiducial point
        count = attribute.GetNumberOfFiducials()
        while count >= 0:
            attribute.GetNthFiducialPosition(0,p1)
            self.controlPoints.append(p1)
            count -= 1

    def getControlPoints(self):
        return self.controlPoints

    def getType(self):
        return self.type





def getAllAnnotations():
    allAnnotations = []
    rulerCollection = slicer.util.getNodesByClass('vtkMRMLAnnotationRulerNode')
    roiCollection = slicer.util.getNodesByClass('vtkMRMLAnnotationROINode')
    fiducialCollection = slicer.util.getNodesByClass('vtkMRMLMarkupsFiducialNode')

    rulerIDs = []
    for ruler in rulerCollection:
        rulerIDs.append(ruler.GetID())

    roiIDs = []
    for roi in roiCollection:
        roiIDs.append(roi.GetID())

    fiducialIDs = []
    for fid in fiducialCollection:
        fiducialIDs.append(fid.GetID())

    for id in rulerIDs:
        allAnnotations.append(Annotation(id))

    return allAnnotations



#
#
#
#
# def getAnnotations():
#     listNodeID = 'vtkMRMLAnnotationHierarchyNode1'  # All Annotations List
#     annotationHierarchyNode = slicer.mrmlScene.GetNodeByID(listNodeID)
#     print annotationHierarchyNode
#     annotationIDs = []
#     annotationListIDs = []
#
#     i = annotationHierarchyNode.GetNumberOfChildrenNodes()
#
#     while i >= 0:
#         print i
#         innerList = annotationHierarchyNode.GetNthChildNode(i)
#         if innerList is None:
#             i -= 1
#             continue
#         annotationListIDs.append(innerList)
#         print 'added ' + str(innerList.GetID()) + ' to annotationListIDs'
#         j = innerList.GetNumberOfChildrenNodes() - 1
#         i -= 1
#         while j >= 0:
#             print innerList.GetNthChildNode(j)
#             if innerList.GetNthChildNode(j) is None:
#                 j -= 1
#                 continue
#             if innerList.GetNthChildNode(j).GetAssociatedNode() is None:
#                 j -= 1
#                 continue
#             annotationIDs.append(innerList.GetNthChildNode(j).GetAssociatedNode())
#             print 'added ' + str(innerList.GetNthChildNode(j).GetAssociatedNode().GetID()) + ' to annotationIDs'
#             j -= 1
#
#
# def getROIControlPoints( attrID ):
#     attribute = slicer.mrmlScene.GetNodeByID(attrID)
#     p1 = [0,0,0] # origin
#     p2 = [0,0,0] # radius
#     attribute.GetRadiusXYZ(p1)
#     attribute.GetXYZ(p2)
#     controlPoints = [p1, p2]
#     return controlPoints
#
#
# def getRulerPositions( attrID ):
#     attribute = slicer.mrmlScene.GetNodeByID(attrID)
#     p1 = [0,0,0] # start point
#     p2 = [0,0,0] # end point
#     attribute.GetPosition1(p1)
#     attribute.GetPosition2(p2)
#     positionPoints = [p1, p2]
#     return positionPoints
#
#
# listNodeID = 'vtkMRMLAnnotationHierarchyNode1' # All Annotations List
# annotationHierarchyNode = slicer.mrmlScene.GetNodeByID(listNodeID)
# print annotationHierarchyNode
# annotationIDs = []
# annotationListIDs = []
#
# i = annotationHierarchyNode.GetNumberOfChildrenNodes()
#
# while i >= 0 :
#     print i
#     innerList = annotationHierarchyNode.GetNthChildNode(i)
#     if innerList is None:
#         i -= 1
#         continue
#     annotationListIDs.append(innerList)
#     print 'added ' + str(innerList.GetID()) + ' to annotationListIDs'
#     j = innerList.GetNumberOfChildrenNodes() - 1
#     i -= 1
#     while j >= 0:
#         print innerList.GetNthChildNode(j)
#         if innerList.GetNthChildNode(j) is None:
#             j -= 1
#             continue
#         if innerList.GetNthChildNode(j).GetAssociatedNode() is None:
#             j -= 1
#             continue
#         annotationIDs.append(innerList.GetNthChildNode(j).GetAssociatedNode())
#         print 'added ' + str(innerList.GetNthChildNode(j).GetAssociatedNode().GetID()) + ' to annotationIDs'
#         j -= 1
#
#
#
# i = annotationHierarchyNode.GetNumberOfChildrenNodes()
# while i >= 0 :
#     print i
#     i -= 1
#
