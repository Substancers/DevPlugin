import pydevd_pycharm
import sd
from PySide2 import QtWidgets
from sd.api import SDApplication


def connectPyCharm():
    pydevd_pycharm.settrace('localhost', port=9001, stdoutToServer=True, stderrToServer=True)


def initializeSDPlugin():
    app: SDApplication = sd.getContext().getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()
    menu = uiMgr.newMenu(menuTitle="Debugger", objectName="debugger")
    act = QtWidgets.QAction("Connect", menu)
    act.triggered.connect(connectPyCharm)
    menu.addAction(act)


def uninitializeSDPlugin():
    app = sd.getContext().getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()
    uiMgr.deleteMenu("debugger")
