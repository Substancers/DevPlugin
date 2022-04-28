from functools import partial

from PySide2 import QtWidgets
from sd.api import SDGraph, SDType, SDSBSCompNode, SDValueFloat2, SDDefinition
from sd.api.sdbasetypes import float2
from sd.api.sdproperty import SDPropertyCategory

from MyPG.Enums import *
from .CurveMainUI_C import Ui_CurveSystem
from MyPG.Deco import NCPUndo

__NCP_TAG = "NCP"


def Get_FIR(node: SDSBSCompNode, category: SDPropertyCategory, order: int = 0):
    fName = "cpf" if order == 0 else f"cpf{order}"
    iName = "cpi" if order == 0 else f"cpi{order}"
    rName = "cpr" if order == 0 else f"cpr{order}"

    cpf = node.getPropertyFromId(fName, category)
    cpi = node.getPropertyFromId(iName, category)
    cpr = node.getPropertyFromId(rName, category)

    return cpf, cpi, cpr


class CurveSystem(QtWidgets.QDialog):
    def __init__(self):
        super().__init__(parent=mc.API().mainUI.getMainWindow())
        ui = Ui_CurveSystem()
        self.ui = ui
        ui.setupUi(self)

        self.ui.bt_c_00.clicked.connect(partial(CurveSystem.__alone, CreateCurve.Dots_8))
        self.ui.bt_c_01.clicked.connect(partial(CurveSystem.__alone, CreateCurve.Start))
        self.ui.bt_c_02.clicked.connect(partial(CurveSystem.__1to1, CreateCurve.Body))
        self.ui.bt_c_03.clicked.connect(partial(CurveSystem.__alone, CreateCurve.Circle))
        self.ui.bt_c_04.clicked.connect(partial(CurveSystem.__alone, CreateCurve.Spiral))
        self.ui.bt_c_05.clicked.connect(partial(CurveSystem.__alone, CreateCurve.Polygon))
        self.ui.bt_c_06.clicked.connect(partial(CurveSystem.__alone, CreateCurve.PolySpiral))
        self.ui.bt_c_07.clicked.connect(partial(CurveSystem.__2to1, CreateCurve.Connect))
        self.ui.bt_c_08.clicked.connect(partial(CurveSystem.__1to1, CreateCurve.Close))

        self.ui.bt_e_01.clicked.connect(partial(CurveSystem.__1to1, EditCurve.AssignAttrib))
        self.ui.bt_e_02.clicked.connect(partial(CurveSystem.__1to1, EditCurve.AssignAttribSimple))
        self.ui.bt_e_03.clicked.connect(partial(CurveSystem.__1to1, EditCurve.InvertU))
        self.ui.bt_e_04.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Carve))
        self.ui.bt_e_05.clicked.connect(partial(CurveSystem.__2to1, EditCurve.BlendShape))
        self.ui.bt_e_06.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Smooth))

        self.ui.bt_e_07.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Transform))
        self.ui.bt_e_08.clicked.connect(partial(CurveSystem.__1to1, EditCurve.DirectionalWarp))
        self.ui.bt_e_09.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Centroid))
        self.ui.bt_e_10.clicked.connect(partial(CurveSystem.__1to1, EditCurve.ShiftU))
        self.ui.bt_e_11.clicked.connect(partial(CurveSystem.__2to1, EditCurve.Switch))
        self.ui.bt_e_12.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Fit))

        self.ui.bt_e_13.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Repeat))
        self.ui.bt_e_14.clicked.connect(partial(CurveSystem.__1to1, EditCurve.VectorMorph))
        self.ui.bt_e_15.clicked.connect(partial(CurveSystem.__1to1, EditCurve.Split))

        self.ui.bt_r_01.clicked.connect(partial(CurveSystem.__1to1_R, RenderCurve.Gray))
        self.ui.bt_r_02.clicked.connect(partial(CurveSystem.__1to1_R, RenderCurve.Color))
        self.ui.bt_r_03.clicked.connect(partial(CurveSystem.__1to1, RenderCurve.Flow))
        self.ui.bt_r_04.clicked.connect(partial(CurveSystem.__1to1, RenderCurve.Preview))
        self.ui.bt_r_05.clicked.connect(partial(CurveSystem.__1to1, RenderCurve.SingleGray))
        self.ui.bt_r_06.clicked.connect(partial(CurveSystem.__1to1, RenderCurve.SingleColor))

        self.ui.bt_r_07.clicked.connect(partial(CurveSystem.__1to1, RenderCurve.Area))
        self.ui.bt_r_08.clicked.connect(partial(CurveSystem.__1to1, RenderCurve.Ladder1))
        self.ui.bt_r_09.clicked.connect(partial(CurveSystem.__2to1, RenderCurve.Ladder2))

        self.ui.bt_p_00.clicked.connect(partial(CurveSystem.__alone, Polynomial.Start))
        self.ui.bt_p_01.clicked.connect(partial(CurveSystem.__1to1, Polynomial.Ax_B))
        self.ui.bt_p_02.clicked.connect(partial(CurveSystem.__2to1, Polynomial.Blend))
        self.ui.bt_p_03.clicked.connect(partial(CurveSystem.__1to1, Polynomial.Tri))
        self.ui.bt_p_04.clicked.connect(partial(CurveSystem.__1to1, Polynomial.Pow))
        self.ui.bt_p_05.clicked.connect(partial(CurveSystem.__1to1, Polynomial.Exp))

        self.ui.bt_p_06.clicked.connect(partial(CurveSystem.__1to1, Polynomial.Abs))
        self.ui.bt_p_07.clicked.connect(partial(CurveSystem.__1to1, Polynomial.Mod))
        self.ui.bt_p_08.clicked.connect(partial(CurveSystem.__alone, Polynomial.Const))

    @staticmethod
    @NCPUndo
    def __alone(nodeToMake: CurveEnumBase):
        currGraph, isCompGraph = CurveSystem.__IsCompGraph()
        if not isCompGraph:
            return
        selection = mc.API().mainUI.getCurrentGraphSelectedNodes()
        node: SDSBSCompNode
        if len(selection) > 0:
            for node in selection:
                if node.getDefinition().getId() == "sbs::compositing::passthrough":
                    pos = node.getPosition()
                    newNode: SDSBSCompNode = currGraph.newInstanceNode(nodeToMake.Resource)
                    newNode.setPosition(pos)
                    currGraph.deleteNode(node)

    @staticmethod
    @NCPUndo
    def __1to1(nodeToMake: CurveEnumBase):
        currGraph, isCompGraph = CurveSystem.__IsCompGraph()
        if not isCompGraph:
            return
        selection = mc.API().mainUI.getCurrentGraphSelectedNodes()
        selLen = len(selection)

        if selLen > 0:
            node: SDSBSCompNode
            for node in selection:
                tag = CurveSystem.__GetDesc(node)
                if tag == "NCP":
                    pos = node.getPosition()
                    newNode: SDSBSCompNode = currGraph.newInstanceNode(nodeToMake.Resource)
                    newNode.setPosition(float2(pos[0] + 128, pos[1]))
                    CurveSystem.__MakeNewConnection(node, newNode)

    @staticmethod
    @NCPUndo
    def __1to1_R(nodeToMake: CurveEnumBase):
        currGraph, isCompGraph = CurveSystem.__IsCompGraph()
        if not isCompGraph:
            return
        selection = mc.API().mainUI.getCurrentGraphSelectedNodes()
        selLen = len(selection)

        if selLen > 0:
            node: SDSBSCompNode
            for node in selection:
                tag = CurveSystem.__GetDesc(node)
                if tag == "NCP":
                    label = node.getDefinition().getLabel().split(' ')[0]
                    if label != "AA":
                        pos = node.getPosition()
                        aaNode: SDSBSCompNode = currGraph.newInstanceNode(EditCurve.AssignAttrib.Resource)
                        aaNode.setPosition(float2(pos[0] + 128, pos[1]))
                        CurveSystem.__MakeNewConnection(node, aaNode)
                        node = aaNode

                    pos = node.getPosition()
                    newNode: SDSBSCompNode = currGraph.newInstanceNode(nodeToMake.Resource)
                    newNode.setPosition(float2(pos[0] + 128, pos[1]))
                    CurveSystem.__MakeNewConnection(node, newNode)

    @staticmethod
    @NCPUndo
    def __2to1(nodeToMake: CurveEnumBase):
        currGraph, isCompGraph = CurveSystem.__IsCompGraph()
        if not isCompGraph:
            return

        selection = mc.API().mainUI.getCurrentGraphSelectedNodes()
        filteredNCPNodes = list(filter(CurveSystem.NCPFilter, selection))
        filteredNCPNodes.sort(key=CurveSystem.SortKey)
        selLen = len(filteredNCPNodes)
        ncpNodes = []

        if selLen > 0:
            node: ncpNodes
            for node in filteredNCPNodes:
                if CurveSystem.NCPFilter(node):
                    ncpNodes.append(node)

                if len(ncpNodes) == 2:
                    node1 = ncpNodes[0]
                    node2 = ncpNodes[1]
                    newNode: SDSBSCompNode = currGraph.newInstanceNode(nodeToMake.Resource)
                    CurveSystem.__MakeNewConnection_2Nodes(node1, node2, newNode)
                    pos1 = node1.getPosition()
                    pos2 = node2.getPosition()
                    newX = max((pos1[0], pos2[0])) + 128
                    newY = (pos1[1] + pos2[1]) / 2.0
                    newNode.setPosition(float2(newX, newY))
                    ncpNodes.clear()

            if len(ncpNodes) == 1:
                node = ncpNodes[0]
                prevFIR = Get_FIR(node, SDPropertyCategory.Output)
                newNode: SDSBSCompNode = currGraph.newInstanceNode(nodeToMake.Resource)
                newFIR = Get_FIR(newNode, SDPropertyCategory.Input, 1)
                for prev, new in zip(prevFIR, newFIR):
                    if prev is not None and new is not None:
                        node.newPropertyConnection(prev, newNode, new)
                pos = node.getPosition()
                newNode.setPosition(float2(pos[0] + 128, pos[1]))

    @staticmethod
    @NCPUndo
    def __nonNCP_to1(nodeToMake: CurveEnumBase):
        pass

    @staticmethod
    def __IsCompGraph():
        currGraph: SDGraph = mc.API().mainUI.getCurrentGraph()
        graphType: SDType = currGraph.getType()
        return currGraph, graphType.getId() == "SDSBSCompGraph"

    @staticmethod
    def __GetDesc(node: SDSBSCompNode):
        nodeDef: SDDefinition = node.getDefinition()
        return nodeDef.getDescription()

    @staticmethod
    def __MakeNewConnection(node1: SDSBSCompNode, node2: SDSBSCompNode):
        prevFIR = Get_FIR(node1, SDPropertyCategory.Output)
        newFIR = Get_FIR(node2, SDPropertyCategory.Input)
        for prev, new in zip(prevFIR, newFIR):
            if prev is not None and new is not None:
                node1.newPropertyConnection(prev, node2, new)

    @staticmethod
    def __MakeNewConnection_2Nodes(node1: SDSBSCompNode, node2: SDSBSCompNode, lastNode: SDSBSCompNode):
        prevFIR = Get_FIR(node1, SDPropertyCategory.Output)
        newFIR = Get_FIR(lastNode, SDPropertyCategory.Input, 1)

        for prev, new in zip(prevFIR, newFIR):
            if prev is not None and new is not None:
                node1.newPropertyConnection(prev, lastNode, new)

        prevFIR2 = Get_FIR(node2, SDPropertyCategory.Output)
        newFIR2 = Get_FIR(lastNode, SDPropertyCategory.Input, 2)

        for prev, new in zip(prevFIR2, newFIR2):
            if prev is not None and new is not None:
                node2.newPropertyConnection(prev, lastNode, new)

    @staticmethod
    def SortKey(node: SDSBSCompNode):
        return node.getPosition()[1]

    @staticmethod
    def NCPFilter(node: SDSBSCompNode):
        nodeDef: SDDefinition = node.getDefinition()
        desc = nodeDef.getDescription()
        return desc == "NCP"
