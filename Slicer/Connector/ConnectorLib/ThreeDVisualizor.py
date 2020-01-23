import numpy as np
import math
from slicer.ScriptedLoadableModule import *


class ThreeDVisualizor:

    def __init__(self):
        print 'ThreeDVisualizor loaded.'


    def viewPoint(self):
        return


    def drawSphere(self, x, y, z, w):
        centerPointCoord = [x, y, z]
        radius = 10
        sphere = vtk.vtkSphereSource()
        sphere.SetCenter(centerPointCoord)
        sphere.SetRadius(radius)

        modelsLogic = slicer.modules.models.logic()
        model = modelsLogic.AddModel(sphere.GetOutput())
        model.GetDisplayNode().SetSliceIntersectionVisibility(True)
        model.GetDisplayNode().SetSliceIntersectionThickness(3)
        model.GetDisplayNode().SetColor(1, 1, 0)

centerPointCoord = [0, 0, 0]
radius = 10
sphere = vtk.vtkSphereSource()
sphere.SetCenter(centerPointCoord)
sphere.SetRadius(radius)

modelsLogic = slicer.modules.models.logic()
model = modelsLogic.AddModel(sphere.GetOutput())
model.GetDisplayNode().SetSliceIntersectionVisibility(True)
model.GetDisplayNode().SetSliceIntersectionThickness(3)
model.GetDisplayNode().SetColor(1, 1, 0)




viewPoint = slicer.app.layoutManager().threeDWidget(0).threeDView()



