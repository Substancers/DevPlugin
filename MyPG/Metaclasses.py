import os.path

import sd
from sd.api import SDSBSCompGraph, SDPackage, SDResource, SDValueString
from sd.api.sdapplication import SDApplicationPath


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class API(metaclass=Singleton):
    def __init__(self):
        self.mainContext = sd.getContext()
        self.mainApp = self.mainContext.getSDApplication()
        self.mainUI = self.mainApp.getQtForPythonUIMgr()
        self.onGraphCreatedCB = -1
        mainResourceDir = self.mainApp.getPath(SDApplicationPath.DefaultResourcesDir)
        fullPath = os.path.normpath(os.path.join(__file__, "../Node/NCPCurveSystem.sbs"))
        pkgMgr = self.mainApp.getPackageMgr()
        self.NCP_PACKAGE = pkgMgr.loadUserPackage(fullPath)

