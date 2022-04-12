import sd

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from sd.api import SDType
from sd.api.sdproperty import SDPropertyCategory, SDProperty


class GetNodeParms(QDialog):
    def __init__(self):
        super().__init__(parent=sd.getContext().getSDApplication().getQtForPythonUIMgr().getMainWindow())
        self.ui = Ui_Parms()
        self.ui.setupUi(self)
        self.teTuple = (self.ui.te_anno, self.ui.te_input, self.ui.te_output)
        self.selChangedCbId = -1

        self.ui.bt_getAttrs.clicked.connect(self.__getAttrFromSelection)

    def __getAttrFromSelection(self):
        uiMgr = sd.getContext().getSDApplication().getUIMgr()
        selectedNodes = uiMgr.getCurrentGraphSelectedNodes()
        if len(selectedNodes) == 0:
            return
        mainNode = selectedNodes[0]
        prop: SDProperty

        # anno, input, output
        props = ([], [], [])
        for i, cat in enumerate(SDPropertyCategory):
            for prop in mainNode.getProperties(cat):
                propId = prop.getId()
                propT: SDType = prop.getType()
                propConnectable = prop.isConnectable()
                listStr = f"{propId} : {propT.getId()} : {propConnectable}"
                props[i].append(listStr)

        for catAttr, te in zip(props, self.teTuple):
            toPrint = '\n'.join(catAttr)
            te.setText(toPrint)

    def ClearAllTextEdit(self):
        for te in self.teTuple:
            te.clear()


class Ui_Parms(object):
    def setupUi(self, Parms):
        if not Parms.objectName():
            Parms.setObjectName(u"Parms")
        Parms.resize(318, 441)
        self.__lo_main = QVBoxLayout(Parms)
        self.__lo_main.setObjectName(u"__lo_main")
        self.bt_getAttrs = QPushButton(Parms)
        self.bt_getAttrs.setObjectName(u"bt_getAttrs")

        self.__lo_main.addWidget(self.bt_getAttrs)

        self.__lb_annotaiton = QLabel(Parms)
        self.__lb_annotaiton.setObjectName(u"__lb_annotaiton")

        self.__lo_main.addWidget(self.__lb_annotaiton)

        self.te_anno = QTextEdit(Parms)
        self.te_anno.setObjectName(u"te_anno")

        self.__lo_main.addWidget(self.te_anno)

        self.__lb_input = QLabel(Parms)
        self.__lb_input.setObjectName(u"__lb_input")

        self.__lo_main.addWidget(self.__lb_input)

        self.te_input = QTextEdit(Parms)
        self.te_input.setObjectName(u"te_input")

        self.__lo_main.addWidget(self.te_input)

        self.__lb_output = QLabel(Parms)
        self.__lb_output.setObjectName(u"__lb_output")

        self.__lo_main.addWidget(self.__lb_output)

        self.te_output = QTextEdit(Parms)
        self.te_output.setObjectName(u"te_output")

        self.__lo_main.addWidget(self.te_output)

        self.retranslateUi(Parms)

        QMetaObject.connectSlotsByName(Parms)

    # setupUi

    def retranslateUi(self, Parms):
        Parms.setWindowTitle(QCoreApplication.translate("Parms", u"Parameters by category", None))
        self.bt_getAttrs.setText(QCoreApplication.translate("Parms", u"Get Parameters", None))
        self.__lb_annotaiton.setText(QCoreApplication.translate("Parms", u"Annotation", None))
        self.__lb_input.setText(QCoreApplication.translate("Parms", u"Input", None))
        self.__lb_output.setText(QCoreApplication.translate("Parms", u"Output", None))
    # retranslateUi
