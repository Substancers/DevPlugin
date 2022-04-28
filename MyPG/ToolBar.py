import os.path as path
from importlib import reload
from typing import Optional

from PySide2 import QtWidgets, QtGui
from sd.api import SDSBSCompNode, SDValueInt
from sd.api.sdbasetypes import int2
from sd.api.sdproperty import SDPropertyInheritanceMethod
from sd.api.sdvalueint2 import SDValueInt2

import MyPG.Metaclasses as Mc
from MyPG.UI.UIConnection import CurveSystem

reload(Mc)
CurveSystemUI: Optional[CurveSystem] = None


class NCPToolBar(QtWidgets.QToolBar):

    def __init__(self):
        super().__init__(parent=Mc.API().mainUI.getMainWindow())
        self.setObjectName("NCPToolBar")
        dirName = path.dirname(__file__)
        rampIcon = path.join(dirName, "rampMaker.png")
        makeRampActionIcon = QtGui.QIcon(rampIcon)

        makeRampAction = self.addAction(makeRampActionIcon, "Make Ramp")
        makeRampAction.triggered.connect(self.__MakeRampBuilder)

        test = self.addAction("Open Curve System")
        test.triggered.connect(self.__OpenUI)

    def __MakeRampBuilder(self):
        api = Mc.API()
        selNodes = api.mainUI.getCurrentGraphSelectedNodes()
        cmpNode: SDSBSCompNode
        for cmpNode in selNodes:
            if not cmpNode.getDefinition().getId() == "sbs::compositing::curve":
                continue
            cmpNode.setInputPropertyInheritanceMethodFromId("$outputsize", SDPropertyInheritanceMethod.Absolute)
            cmpNode.setInputPropertyValueFromId("$outputsize", SDValueInt2.sNew(int2(13, 4)))
            cmpNode.setInputPropertyInheritanceMethodFromId("$format", SDPropertyInheritanceMethod.Absolute)
            cmpNode.setInputPropertyValueFromId("$format", SDValueInt.sNew(1))

    def __OpenUI(self):
        global CurveSystemUI
        if CurveSystemUI is None:
            CurveSystemUI = CurveSystem()

        if CurveSystemUI.isVisible():
            CurveSystemUI.setVisible(False)

        CurveSystemUI.show()
