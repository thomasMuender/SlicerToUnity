import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import zmq
import numpy as np
import logging
import struct

class CommunicationHandler:

    isRunning = False
    id = vtk.vtkMatrix4x4()

    def __init__(self):
        self.context = zmq.Context()

        self.PUB = self.context.socket(zmq.PUB)
        self.PUB.bind("tcp://*:5555")

        self.SUB = self.context.socket(zmq.SUB)
        self.SUB.bind("tcp://*:5556")
        self.SUB.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

        self.REP = self.context.socket(zmq.REP)
        self.REP.bind("tcp://*:5557")

        self.run()
        logging.info('Connection establihed')

        self.id.Identity()
        cube = vtk.vtkCubeSource()
        centerPointCoord = [0.0, 0.0, 0.0]
        cube.SetCenter(centerPointCoord)
        cube.SetXLength(20)
        cube.SetYLength(5)
        cube.SetZLength(10)
        cube.Update()
        modelsLogic = slicer.modules.models.logic()
        model = modelsLogic.AddModel(cube.GetOutput())
        model.GetDisplayNode().SetSliceIntersectionVisibility(True)
        model.GetDisplayNode().SetSliceIntersectionThickness(3)
        model.GetDisplayNode().SetColor(1, 0, 0)

    def stop(self):
        self.isRunning = False

        self.PUB.close()
        self.SUB.close()
        self.REP.close()

        self.context.destroy()

    def running(self):
        return self.isRunning

    def run(self):
        self.isRunning = True
        if self.isRunning:
            self.PUB.send_string("SlicerData")

            try:
                msg = self.SUB.recv(zmq.DONTWAIT)
                transform = np.frombuffer(msg, dtype=np.float32)
                transform = transform.reshape((4, 4))
                mtx = vtk.vtkMatrix4x4()
                mtx.DeepCopy(transform.ravel())
                node = slicer.mrmlScene.GetNodesByName("Model")
                node = node.GetItemAsObject(0)
                node.ApplyTransformMatrix(self.id)
                node.ApplyTransformMatrix(mtx)

                self.id = mtx
                self.id.Invert()

            except zmq.Again:
                pass

            try:
                msg2 = self.REP.recv(zmq.DONTWAIT)

                if msg2 == "volume":

                    volume = np.random.rand(320, 240, 200)
                    volume = volume.astype(np.float32)
                    dim = volume.shape
                    dimL = len(dim)
                    b = struct.pack('=%ii'%dimL, *dim)
                    data = b + volume.tobytes()

                    reply = "/Users/thomas/Documents/tmpdata"
                    f = open(reply, "w")
                    f.write(data)
                    f.close()

                else:
                    reply = "reply"

                self.REP.send_string(reply)
            except zmq.Again:
                pass

            qt.QTimer.singleShot(16, self.run)
