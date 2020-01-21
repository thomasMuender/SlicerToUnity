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

