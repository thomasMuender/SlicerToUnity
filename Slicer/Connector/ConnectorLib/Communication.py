import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import zmq
import numpy as np
import logging

class CommunicationHandler:

    isRunning = False

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
                logging.info(msg)
            except zmq.Again:
                pass

            try:
                msg2 = self.REP.recv(zmq.DONTWAIT)
                logging.info(msg2)
                #getDataPackage
                self.REP.send_string("Reply")
            except zmq.Again:
                pass

            qt.QTimer.singleShot(16, self.run)
