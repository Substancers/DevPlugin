import pydevd_pycharm
import sd
from PySide2 import QtWidgets
from sd.api import SDApplication
from DevBooster import sdNodeParameters_UI as parmUI


def connectPyCharm():
    pydevd_pycharm.settrace('localhost', port=9001, stdoutToServer=True, stderrToServer=True)


sdParmUi = None


def readAttribs():
    global sdParmUi
    if sdParmUi is None:
        sdParmUi = parmUI.GetNodeParms()
    if sdParmUi.isVisible():
        sdParmUi.close()
    sdParmUi.ClearAllTextEdit()
    sdParmUi.show()


def initializeSDPlugin():
    app: SDApplication = sd.getContext().getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()
    menu = uiMgr.newMenu(menuTitle="Debugger", objectName="debugger")

    act = QtWidgets.QAction("Connect", menu)
    act.triggered.connect(connectPyCharm)

    act2 = QtWidgets.QAction("Parm UI", menu)
    act2.triggered.connect(readAttribs)
    menu.addAction(act)
    menu.addAction(act2)


def uninitializeSDPlugin():
    app = sd.getContext().getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()
    uiMgr.deleteMenu("debugger")
