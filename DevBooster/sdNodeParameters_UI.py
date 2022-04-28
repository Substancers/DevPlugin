import sd

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from sd.api import SDType, SDDefinition
from sd.api.sdproperty import SDPropertyCategory, SDProperty


class GetNodeParms(QDialog):
    def __init__(self):
        super().__init__(parent=sd.getContext().getSDApplication().getQtForPythonUIMgr().getMainWindow())
        self.ui = Ui_Parms()
        self.ui.setupUi(self)
        self.teTuple = (self.ui.te_anno, self.ui.te_input, self.ui.te_output)
        self.conTuple = (self.ui.te_inputCon, self.ui.te_outputCon)
        self.selChangedCbId = -1

        self.ui.bt_getAttrs.clicked.connect(self.__getAttrFromSelection)

    def __getAttrFromSelection(self):
        uiMgr = sd.getContext().getSDApplication().getUIMgr()
        selectedNodes = uiMgr.getCurrentGraphSelectedNodes()
        if len(selectedNodes) == 0:
            return
        mainNode = selectedNodes[0]
        nodeDef: SDDefinition = mainNode.getDefinition()
        nodeId = nodeDef.getId()
        self.ui.le_id.setText(nodeId)
        if nodeId == "sbs::compositing::sbscompgraph_instance":
            self.ui.le_label = nodeDef.getLabel()

            pass
        else:
            pass

        prop: SDProperty

        props = ([], [], [])
        conProps = ([], [])
        for i, cat in enumerate(SDPropertyCategory):
            for prop in mainNode.getProperties(cat):
                propId = prop.getId()
                propT: SDType = prop.getType()
                propConnectable = prop.isConnectable()
                listStr = f"{propId:<20} :: {propT.getId():}"
                if propConnectable:
                    conProps[i - 1].append(listStr)
                else:
                    props[i].append(listStr)

        for catAttr, te in zip(props, self.teTuple):
            toPrint = '\n'.join(catAttr)
            te.setText(toPrint)

        for catAttr, te in zip(conProps, self.conTuple):
            toPrint = '\n'.join(catAttr)
            te.setText(toPrint)

    def ClearAllTextEdit(self):
        for te in self.teTuple:
            te.clear()
        for te in self.conTuple:
            te.clear()


class Ui_Parms:
    def setupUi(self, Parms):
        if not Parms.objectName():
            Parms.setObjectName(u"Parms")
        Parms.resize(448, 691)
        self.gridLayout = QGridLayout(Parms)
        self.gridLayout.setObjectName(u"gridLayout")
        self.__lb_annotaiton = QLabel(Parms)
        self.__lb_annotaiton.setObjectName(u"__lb_annotaiton")

        self.gridLayout.addWidget(self.__lb_annotaiton, 1, 0, 1, 1)

        self.te_input = QTextEdit(Parms)
        self.te_input.setObjectName(u"te_input")

        self.gridLayout.addWidget(self.te_input, 4, 0, 1, 1)

        self.__lb_output = QLabel(Parms)
        self.__lb_output.setObjectName(u"__lb_output")

        self.gridLayout.addWidget(self.__lb_output, 5, 0, 1, 1)

        self.__lb_input = QLabel(Parms)
        self.__lb_input.setObjectName(u"__lb_input")

        self.gridLayout.addWidget(self.__lb_input, 3, 0, 1, 1)

        self.te_output = QTextEdit(Parms)
        self.te_output.setObjectName(u"te_output")

        self.gridLayout.addWidget(self.te_output, 6, 0, 1, 1)

        self.__lb_inputCon = QLabel(Parms)
        self.__lb_inputCon.setObjectName(u"__lb_inputCon")

        self.gridLayout.addWidget(self.__lb_inputCon, 3, 1, 1, 1)

        self.te_inputCon = QTextEdit(Parms)
        self.te_inputCon.setObjectName(u"te_inputCon")

        self.gridLayout.addWidget(self.te_inputCon, 4, 1, 1, 1)

        self.te_outputCon = QTextEdit(Parms)
        self.te_outputCon.setObjectName(u"te_outputCon")

        self.gridLayout.addWidget(self.te_outputCon, 6, 1, 1, 1)

        self.__lb_outCon = QLabel(Parms)
        self.__lb_outCon.setObjectName(u"__lb_outCon")

        self.gridLayout.addWidget(self.__lb_outCon, 5, 1, 1, 1)

        self.te_anno = QTextEdit(Parms)
        self.te_anno.setObjectName(u"te_anno")

        self.gridLayout.addWidget(self.te_anno, 2, 0, 1, 1)

        self.__lo_etc = QVBoxLayout()
        self.__lo_etc.setObjectName(u"__lo_etc")
        self.__lb_id = QLabel(Parms)
        self.__lb_id.setObjectName(u"__lb_id")

        self.__lo_etc.addWidget(self.__lb_id)

        self.le_id = QLineEdit(Parms)
        self.le_id.setObjectName(u"le_id")

        self.__lo_etc.addWidget(self.le_id)

        self.__lb_label = QLabel(Parms)
        self.__lb_label.setObjectName(u"__lb_label")

        self.__lo_etc.addWidget(self.__lb_label)

        self.le_label = QLineEdit(Parms)
        self.le_label.setObjectName(u"le_label")

        self.__lo_etc.addWidget(self.le_label)

        self.__lb_url = QLabel(Parms)
        self.__lb_url.setObjectName(u"__lb_url")

        self.__lo_etc.addWidget(self.__lb_url)

        self.le_url = QLineEdit(Parms)
        self.le_url.setObjectName(u"le_url")

        self.__lo_etc.addWidget(self.le_url)

        self.__sp = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.__lo_etc.addItem(self.__sp)

        self.gridLayout.addLayout(self.__lo_etc, 1, 1, 2, 1)

        self.bt_getAttrs = QPushButton(Parms)
        self.bt_getAttrs.setObjectName(u"bt_getAttrs")

        self.gridLayout.addWidget(self.bt_getAttrs, 0, 0, 1, 2)

        self.retranslateUi(Parms)

        QMetaObject.connectSlotsByName(Parms)

    # setupUi

    def retranslateUi(self, Parms):
        Parms.setWindowTitle(QCoreApplication.translate("Parms", u"Parameters by category", None))
        self.__lb_annotaiton.setText(QCoreApplication.translate("Parms", u"Annotation", None))
        self.__lb_output.setText(QCoreApplication.translate("Parms", u"Output", None))
        self.__lb_input.setText(QCoreApplication.translate("Parms", u"Input", None))
        self.__lb_inputCon.setText(QCoreApplication.translate("Parms", u"Input Connectable", None))
        self.__lb_outCon.setText(QCoreApplication.translate("Parms", u"Output Connectable", None))
        self.__lb_id.setText(QCoreApplication.translate("Parms", u"Node ID", None))
        self.__lb_label.setText(QCoreApplication.translate("Parms", u"Label", None))
        self.le_label.setText("")
        self.__lb_url.setText(QCoreApplication.translate("Parms", u"TextLabel", None))
        self.bt_getAttrs.setText(QCoreApplication.translate("Parms", u"Get Parameters", None))
    # retranslateUi
