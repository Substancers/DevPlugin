import os
from importlib import reload

from PySide2 import QtGui

import MyPG.Metaclasses as mc
import MyPG.ToolBar as tb

def addToolbarToGraphView(passed):
    api = mc.API()
    dirName = os.path.dirname(__file__)
    iconFile = os.path.join(dirName, "ncpPluginIcon.png")
    api.mainUI.addToolbarToGraphView(passed, tb.NCPToolBar(), QtGui.QIcon(iconFile), "NCP Tool Bar")


def initializeSDPlugin():
    api = mc.API()
    api.onGraphCreatedCB = api.mainUI.registerGraphViewCreatedCallback(addToolbarToGraphView)


def uninitializeSDPlugin():
    api = mc.API()
    api.mainUI.unregisterCallback(api.onGraphCreatedCB)
