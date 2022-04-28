# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CurveMainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from MyPG.Metaclasses import Singleton

import MyPG.UI.uiresource_rc as uiresource_rc


class Ui_CurveSystem:
    def setupUi(self, CurveSystem):
        if not CurveSystem.objectName():
            CurveSystem.setObjectName(u"CurveSystem")
        CurveSystem.resize(410, 916)
        CurveSystem.setMinimumSize(QSize(410, 916))
        CurveSystem.setMaximumSize(QSize(410, 916))
        self.lo_main = QVBoxLayout(CurveSystem)
        self.lo_main.setObjectName(u"lo_main")
        self.__lb_create = QLabel(CurveSystem)
        self.__lb_create.setObjectName(u"__lb_create")
        self.__lb_create.setMaximumSize(QSize(16777215, 15))

        self.lo_main.addWidget(self.__lb_create)

        self.__lo00 = QHBoxLayout()
        self.__lo00.setObjectName(u"__lo00")
        self.bt_c_00 = QToolButton(CurveSystem)
        self.bt_c_00.setObjectName(u"bt_c_00")
        self.bt_c_00.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icon/c_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_00.setIcon(icon)
        self.bt_c_00.setIconSize(QSize(55, 55))

        self.__lo00.addWidget(self.bt_c_00)

        self.bt_c_01 = QToolButton(CurveSystem)
        self.bt_c_01.setObjectName(u"bt_c_01")
        self.bt_c_01.setMaximumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/c_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_01.setIcon(icon1)
        self.bt_c_01.setIconSize(QSize(55, 55))

        self.__lo00.addWidget(self.bt_c_01)

        self.bt_c_02 = QToolButton(CurveSystem)
        self.bt_c_02.setObjectName(u"bt_c_02")
        self.bt_c_02.setMaximumSize(QSize(60, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/c_02.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_02.setIcon(icon2)
        self.bt_c_02.setIconSize(QSize(55, 55))

        self.__lo00.addWidget(self.bt_c_02)

        self.bt_c_03 = QToolButton(CurveSystem)
        self.bt_c_03.setObjectName(u"bt_c_03")
        self.bt_c_03.setMaximumSize(QSize(60, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/c_03.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_03.setIcon(icon3)
        self.bt_c_03.setIconSize(QSize(55, 55))

        self.__lo00.addWidget(self.bt_c_03)

        self.bt_c_04 = QToolButton(CurveSystem)
        self.bt_c_04.setObjectName(u"bt_c_04")
        self.bt_c_04.setMaximumSize(QSize(60, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/c_04.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_04.setIcon(icon4)
        self.bt_c_04.setIconSize(QSize(55, 55))

        self.__lo00.addWidget(self.bt_c_04)

        self.bt_c_05 = QToolButton(CurveSystem)
        self.bt_c_05.setObjectName(u"bt_c_05")
        self.bt_c_05.setMaximumSize(QSize(60, 60))
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/c_05.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_05.setIcon(icon5)
        self.bt_c_05.setIconSize(QSize(55, 55))

        self.__lo00.addWidget(self.bt_c_05)

        self.lo_main.addLayout(self.__lo00)

        self.__lo01 = QHBoxLayout()
        self.__lo01.setObjectName(u"__lo01")
        self.bt_c_06 = QToolButton(CurveSystem)
        self.bt_c_06.setObjectName(u"bt_c_06")
        self.bt_c_06.setMaximumSize(QSize(60, 60))
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/c_06.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_06.setIcon(icon6)
        self.bt_c_06.setIconSize(QSize(55, 55))

        self.__lo01.addWidget(self.bt_c_06)

        self.bt_c_07 = QToolButton(CurveSystem)
        self.bt_c_07.setObjectName(u"bt_c_07")
        self.bt_c_07.setMaximumSize(QSize(60, 60))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/c_07.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_07.setIcon(icon7)
        self.bt_c_07.setIconSize(QSize(55, 55))

        self.__lo01.addWidget(self.bt_c_07)

        self.bt_c_08 = QToolButton(CurveSystem)
        self.bt_c_08.setObjectName(u"bt_c_08")
        self.bt_c_08.setMaximumSize(QSize(60, 60))
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/c_08.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_08.setIcon(icon8)
        self.bt_c_08.setIconSize(QSize(55, 55))

        self.__lo01.addWidget(self.bt_c_08)

        self.bt_c_09 = QToolButton(CurveSystem)
        self.bt_c_09.setObjectName(u"bt_c_09")
        self.bt_c_09.setMaximumSize(QSize(60, 60))
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/c_09.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_09.setIcon(icon9)
        self.bt_c_09.setIconSize(QSize(55, 55))

        self.__lo01.addWidget(self.bt_c_09)

        self.bt_c_10 = QToolButton(CurveSystem)
        self.bt_c_10.setObjectName(u"bt_c_10")
        self.bt_c_10.setMaximumSize(QSize(60, 60))
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/c_10.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_10.setIcon(icon10)
        self.bt_c_10.setIconSize(QSize(55, 55))

        self.__lo01.addWidget(self.bt_c_10)

        self.bt_c_11 = QToolButton(CurveSystem)
        self.bt_c_11.setObjectName(u"bt_c_11")
        self.bt_c_11.setMaximumSize(QSize(60, 60))
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/c_11.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_c_11.setIcon(icon11)
        self.bt_c_11.setIconSize(QSize(55, 55))

        self.__lo01.addWidget(self.bt_c_11)

        self.lo_main.addLayout(self.__lo01)

        self.__line = QFrame(CurveSystem)
        self.__line.setObjectName(u"__line")
        self.__line.setFrameShape(QFrame.HLine)
        self.__line.setFrameShadow(QFrame.Sunken)

        self.lo_main.addWidget(self.__line)

        self.__lb_edit = QLabel(CurveSystem)
        self.__lb_edit.setObjectName(u"__lb_edit")
        self.__lb_edit.setMaximumSize(QSize(16777215, 15))

        self.lo_main.addWidget(self.__lb_edit)

        self.__lo02 = QHBoxLayout()
        self.__lo02.setObjectName(u"__lo02")
        self.bt_e_01 = QToolButton(CurveSystem)
        self.bt_e_01.setObjectName(u"bt_e_01")
        self.bt_e_01.setMaximumSize(QSize(60, 60))
        icon12 = QIcon()
        icon12.addFile(u":/icon/icon/e_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_01.setIcon(icon12)
        self.bt_e_01.setIconSize(QSize(55, 55))

        self.__lo02.addWidget(self.bt_e_01)

        self.bt_e_02 = QToolButton(CurveSystem)
        self.bt_e_02.setObjectName(u"bt_e_02")
        self.bt_e_02.setMaximumSize(QSize(60, 60))
        icon13 = QIcon()
        icon13.addFile(u":/icon/icon/e_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_02.setIcon(icon13)
        self.bt_e_02.setIconSize(QSize(55, 55))

        self.__lo02.addWidget(self.bt_e_02)

        self.bt_e_03 = QToolButton(CurveSystem)
        self.bt_e_03.setObjectName(u"bt_e_03")
        self.bt_e_03.setMaximumSize(QSize(60, 60))
        icon14 = QIcon()
        icon14.addFile(u":/icon/icon/e_02.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_03.setIcon(icon14)
        self.bt_e_03.setIconSize(QSize(55, 55))

        self.__lo02.addWidget(self.bt_e_03)

        self.bt_e_04 = QToolButton(CurveSystem)
        self.bt_e_04.setObjectName(u"bt_e_04")
        self.bt_e_04.setMaximumSize(QSize(60, 60))
        icon15 = QIcon()
        icon15.addFile(u":/icon/icon/e_03.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_04.setIcon(icon15)
        self.bt_e_04.setIconSize(QSize(55, 55))

        self.__lo02.addWidget(self.bt_e_04)

        self.bt_e_05 = QToolButton(CurveSystem)
        self.bt_e_05.setObjectName(u"bt_e_05")
        self.bt_e_05.setMaximumSize(QSize(60, 60))
        icon16 = QIcon()
        icon16.addFile(u":/icon/icon/e_04.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_05.setIcon(icon16)
        self.bt_e_05.setIconSize(QSize(55, 55))

        self.__lo02.addWidget(self.bt_e_05)

        self.bt_e_06 = QToolButton(CurveSystem)
        self.bt_e_06.setObjectName(u"bt_e_06")
        self.bt_e_06.setMaximumSize(QSize(60, 60))
        icon17 = QIcon()
        icon17.addFile(u":/icon/icon/e_05.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_06.setIcon(icon17)
        self.bt_e_06.setIconSize(QSize(55, 55))

        self.__lo02.addWidget(self.bt_e_06)

        self.lo_main.addLayout(self.__lo02)

        self.__lo03 = QHBoxLayout()
        self.__lo03.setObjectName(u"__lo03")
        self.bt_e_07 = QToolButton(CurveSystem)
        self.bt_e_07.setObjectName(u"bt_e_07")
        self.bt_e_07.setMaximumSize(QSize(60, 60))
        icon18 = QIcon()
        icon18.addFile(u":/icon/icon/e_06.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_07.setIcon(icon18)
        self.bt_e_07.setIconSize(QSize(55, 55))

        self.__lo03.addWidget(self.bt_e_07)

        self.bt_e_08 = QToolButton(CurveSystem)
        self.bt_e_08.setObjectName(u"bt_e_08")
        self.bt_e_08.setMaximumSize(QSize(60, 60))
        icon19 = QIcon()
        icon19.addFile(u":/icon/icon/e_07.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_08.setIcon(icon19)
        self.bt_e_08.setIconSize(QSize(55, 55))

        self.__lo03.addWidget(self.bt_e_08)

        self.bt_e_09 = QToolButton(CurveSystem)
        self.bt_e_09.setObjectName(u"bt_e_09")
        self.bt_e_09.setMaximumSize(QSize(60, 60))
        icon20 = QIcon()
        icon20.addFile(u":/icon/icon/e_08.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_09.setIcon(icon20)
        self.bt_e_09.setIconSize(QSize(55, 55))

        self.__lo03.addWidget(self.bt_e_09)

        self.bt_e_10 = QToolButton(CurveSystem)
        self.bt_e_10.setObjectName(u"bt_e_10")
        self.bt_e_10.setMaximumSize(QSize(60, 60))
        icon21 = QIcon()
        icon21.addFile(u":/icon/icon/e_09.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_10.setIcon(icon21)
        self.bt_e_10.setIconSize(QSize(55, 55))

        self.__lo03.addWidget(self.bt_e_10)

        self.bt_e_11 = QToolButton(CurveSystem)
        self.bt_e_11.setObjectName(u"bt_e_11")
        self.bt_e_11.setMaximumSize(QSize(60, 60))
        icon22 = QIcon()
        icon22.addFile(u":/icon/icon/e_10.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_11.setIcon(icon22)
        self.bt_e_11.setIconSize(QSize(55, 55))

        self.__lo03.addWidget(self.bt_e_11)

        self.bt_e_12 = QToolButton(CurveSystem)
        self.bt_e_12.setObjectName(u"bt_e_12")
        self.bt_e_12.setMaximumSize(QSize(60, 60))
        icon23 = QIcon()
        icon23.addFile(u":/icon/icon/e_11.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_12.setIcon(icon23)
        self.bt_e_12.setIconSize(QSize(55, 55))

        self.__lo03.addWidget(self.bt_e_12)

        self.lo_main.addLayout(self.__lo03)

        self.__lo04 = QHBoxLayout()
        self.__lo04.setObjectName(u"__lo04")
        self.bt_e_13 = QToolButton(CurveSystem)
        self.bt_e_13.setObjectName(u"bt_e_13")
        self.bt_e_13.setMaximumSize(QSize(60, 60))
        icon24 = QIcon()
        icon24.addFile(u":/icon/icon/e_12.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_13.setIcon(icon24)
        self.bt_e_13.setIconSize(QSize(55, 55))

        self.__lo04.addWidget(self.bt_e_13)

        self.bt_e_14 = QToolButton(CurveSystem)
        self.bt_e_14.setObjectName(u"bt_e_14")
        self.bt_e_14.setMaximumSize(QSize(60, 60))
        icon25 = QIcon()
        icon25.addFile(u":/icon/icon/e_13.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_14.setIcon(icon25)
        self.bt_e_14.setIconSize(QSize(55, 55))

        self.__lo04.addWidget(self.bt_e_14)

        self.bt_e_15 = QToolButton(CurveSystem)
        self.bt_e_15.setObjectName(u"bt_e_15")
        self.bt_e_15.setMaximumSize(QSize(60, 60))
        icon26 = QIcon()
        icon26.addFile(u":/icon/icon/e_14.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_e_15.setIcon(icon26)
        self.bt_e_15.setIconSize(QSize(55, 55))

        self.__lo04.addWidget(self.bt_e_15)

        self.__sp_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.__lo04.addItem(self.__sp_2)

        self.lo_main.addLayout(self.__lo04)

        self.__line_5 = QFrame(CurveSystem)
        self.__line_5.setObjectName(u"__line_5")
        self.__line_5.setFrameShape(QFrame.HLine)
        self.__line_5.setFrameShadow(QFrame.Sunken)

        self.lo_main.addWidget(self.__line_5)

        self.__lb_render = QLabel(CurveSystem)
        self.__lb_render.setObjectName(u"__lb_render")

        self.lo_main.addWidget(self.__lb_render)

        self.__lo05 = QHBoxLayout()
        self.__lo05.setObjectName(u"__lo05")
        self.bt_r_01 = QToolButton(CurveSystem)
        self.bt_r_01.setObjectName(u"bt_r_01")
        self.bt_r_01.setMaximumSize(QSize(60, 60))
        icon27 = QIcon()
        icon27.addFile(u":/icon/icon/r_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_01.setIcon(icon27)
        self.bt_r_01.setIconSize(QSize(55, 55))

        self.__lo05.addWidget(self.bt_r_01)

        self.bt_r_02 = QToolButton(CurveSystem)
        self.bt_r_02.setObjectName(u"bt_r_02")
        self.bt_r_02.setMaximumSize(QSize(60, 60))
        icon28 = QIcon()
        icon28.addFile(u":/icon/icon/r_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_02.setIcon(icon28)
        self.bt_r_02.setIconSize(QSize(55, 55))

        self.__lo05.addWidget(self.bt_r_02)

        self.bt_r_03 = QToolButton(CurveSystem)
        self.bt_r_03.setObjectName(u"bt_r_03")
        self.bt_r_03.setMaximumSize(QSize(60, 60))
        icon29 = QIcon()
        icon29.addFile(u":/icon/icon/r_02.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_03.setIcon(icon29)
        self.bt_r_03.setIconSize(QSize(55, 55))

        self.__lo05.addWidget(self.bt_r_03)

        self.bt_r_04 = QToolButton(CurveSystem)
        self.bt_r_04.setObjectName(u"bt_r_04")
        self.bt_r_04.setMaximumSize(QSize(60, 60))
        icon30 = QIcon()
        icon30.addFile(u":/icon/icon/r_03.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_04.setIcon(icon30)
        self.bt_r_04.setIconSize(QSize(55, 55))

        self.__lo05.addWidget(self.bt_r_04)

        self.bt_r_05 = QToolButton(CurveSystem)
        self.bt_r_05.setObjectName(u"bt_r_05")
        self.bt_r_05.setMaximumSize(QSize(60, 60))
        icon31 = QIcon()
        icon31.addFile(u":/icon/icon/r_04.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_05.setIcon(icon31)
        self.bt_r_05.setIconSize(QSize(55, 55))

        self.__lo05.addWidget(self.bt_r_05)

        self.bt_r_06 = QToolButton(CurveSystem)
        self.bt_r_06.setObjectName(u"bt_r_06")
        self.bt_r_06.setMaximumSize(QSize(60, 60))
        icon32 = QIcon()
        icon32.addFile(u":/icon/icon/r_05.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_06.setIcon(icon32)
        self.bt_r_06.setIconSize(QSize(55, 55))

        self.__lo05.addWidget(self.bt_r_06)

        self.lo_main.addLayout(self.__lo05)

        self.__lo06 = QHBoxLayout()
        self.__lo06.setObjectName(u"__lo06")
        self.bt_r_07 = QToolButton(CurveSystem)
        self.bt_r_07.setObjectName(u"bt_r_07")
        self.bt_r_07.setMaximumSize(QSize(60, 60))
        icon33 = QIcon()
        icon33.addFile(u":/icon/icon/r_06.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_07.setIcon(icon33)
        self.bt_r_07.setIconSize(QSize(55, 55))

        self.__lo06.addWidget(self.bt_r_07)

        self.bt_r_08 = QToolButton(CurveSystem)
        self.bt_r_08.setObjectName(u"bt_r_08")
        self.bt_r_08.setMaximumSize(QSize(60, 60))
        icon34 = QIcon()
        icon34.addFile(u":/icon/icon/r_07.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_r_08.setIcon(icon34)
        self.bt_r_08.setIconSize(QSize(55, 55))

        self.__lo06.addWidget(self.bt_r_08)

        self.bt_r_09 = QToolButton(CurveSystem)
        self.bt_r_09.setObjectName(u"bt_r_09")
        self.bt_r_09.setMaximumSize(QSize(60, 60))
        self.bt_r_09.setIconSize(QSize(55, 55))

        self.__lo06.addWidget(self.bt_r_09)

        self.__sp_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.__lo06.addItem(self.__sp_3)

        self.lo_main.addLayout(self.__lo06)

        self.__line_4 = QFrame(CurveSystem)
        self.__line_4.setObjectName(u"__line_4")
        self.__line_4.setFrameShape(QFrame.HLine)
        self.__line_4.setFrameShadow(QFrame.Sunken)

        self.lo_main.addWidget(self.__line_4)

        self.__lb_surface = QLabel(CurveSystem)
        self.__lb_surface.setObjectName(u"__lb_surface")

        self.lo_main.addWidget(self.__lb_surface)

        self.__lo07 = QHBoxLayout()
        self.__lo07.setObjectName(u"__lo07")
        self.bt_s_00 = QToolButton(CurveSystem)
        self.bt_s_00.setObjectName(u"bt_s_00")
        self.bt_s_00.setMaximumSize(QSize(60, 60))
        icon35 = QIcon()
        icon35.addFile(u":/icon/icon/s_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_s_00.setIcon(icon35)
        self.bt_s_00.setIconSize(QSize(55, 55))

        self.__lo07.addWidget(self.bt_s_00)

        self.bt_s_01 = QToolButton(CurveSystem)
        self.bt_s_01.setObjectName(u"bt_s_01")
        self.bt_s_01.setMaximumSize(QSize(60, 60))
        icon36 = QIcon()
        icon36.addFile(u":/icon/icon/s_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_s_01.setIcon(icon36)
        self.bt_s_01.setIconSize(QSize(55, 55))

        self.__lo07.addWidget(self.bt_s_01)

        self.bt_s_02 = QToolButton(CurveSystem)
        self.bt_s_02.setObjectName(u"bt_s_02")
        self.bt_s_02.setMaximumSize(QSize(60, 60))
        icon37 = QIcon()
        icon37.addFile(u":/icon/icon/s_02.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_s_02.setIcon(icon37)
        self.bt_s_02.setIconSize(QSize(55, 55))

        self.__lo07.addWidget(self.bt_s_02)

        self.bt_s_03 = QToolButton(CurveSystem)
        self.bt_s_03.setObjectName(u"bt_s_03")
        self.bt_s_03.setMaximumSize(QSize(16777213, 16777215))
        icon38 = QIcon()
        icon38.addFile(u":/icon/icon/s_03.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_s_03.setIcon(icon38)
        self.bt_s_03.setIconSize(QSize(55, 55))

        self.__lo07.addWidget(self.bt_s_03)

        self.__sp_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.__lo07.addItem(self.__sp_4)

        self.lo_main.addLayout(self.__lo07)

        self.__line_2 = QFrame(CurveSystem)
        self.__line_2.setObjectName(u"__line_2")
        self.__line_2.setFrameShape(QFrame.HLine)
        self.__line_2.setFrameShadow(QFrame.Sunken)

        self.lo_main.addWidget(self.__line_2)

        self.__lb_utils = QLabel(CurveSystem)
        self.__lb_utils.setObjectName(u"__lb_utils")

        self.lo_main.addWidget(self.__lb_utils)

        self.__lo08 = QHBoxLayout()
        self.__lo08.setObjectName(u"__lo08")
        self.bt_u_00 = QToolButton(CurveSystem)
        self.bt_u_00.setObjectName(u"bt_u_00")
        self.bt_u_00.setMaximumSize(QSize(60, 60))
        icon39 = QIcon()
        icon39.addFile(u":/icon/icon/u_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_u_00.setIcon(icon39)
        self.bt_u_00.setIconSize(QSize(55, 55))

        self.__lo08.addWidget(self.bt_u_00)

        self.bt_u_01 = QToolButton(CurveSystem)
        self.bt_u_01.setObjectName(u"bt_u_01")
        self.bt_u_01.setMaximumSize(QSize(60, 60))
        icon40 = QIcon()
        icon40.addFile(u":/icon/icon/u_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_u_01.setIcon(icon40)
        self.bt_u_01.setIconSize(QSize(55, 55))

        self.__lo08.addWidget(self.bt_u_01)

        self.bt_u_02 = QToolButton(CurveSystem)
        self.bt_u_02.setObjectName(u"bt_u_02")
        self.bt_u_02.setMaximumSize(QSize(60, 60))
        icon41 = QIcon()
        icon41.addFile(u":/icon/icon/u_02.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_u_02.setIcon(icon41)
        self.bt_u_02.setIconSize(QSize(55, 55))

        self.__lo08.addWidget(self.bt_u_02)

        self.bt_u_03 = QToolButton(CurveSystem)
        self.bt_u_03.setObjectName(u"bt_u_03")
        self.bt_u_03.setMaximumSize(QSize(60, 60))
        icon42 = QIcon()
        icon42.addFile(u":/icon/icon/u_03.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_u_03.setIcon(icon42)
        self.bt_u_03.setIconSize(QSize(55, 55))

        self.__lo08.addWidget(self.bt_u_03)

        self.bt_a_00 = QToolButton(CurveSystem)
        self.bt_a_00.setObjectName(u"bt_a_00")
        self.bt_a_00.setMaximumSize(QSize(60, 60))
        icon43 = QIcon()
        icon43.addFile(u":/icon/icon/a_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_a_00.setIcon(icon43)
        self.bt_a_00.setIconSize(QSize(55, 55))

        self.__lo08.addWidget(self.bt_a_00)

        self.bt_a_01 = QToolButton(CurveSystem)
        self.bt_a_01.setObjectName(u"bt_a_01")
        self.bt_a_01.setMaximumSize(QSize(60, 60))
        icon44 = QIcon()
        icon44.addFile(u":/icon/icon/a_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_a_01.setIcon(icon44)
        self.bt_a_01.setIconSize(QSize(55, 55))

        self.__lo08.addWidget(self.bt_a_01)

        self.lo_main.addLayout(self.__lo08)

        self.__line_3 = QFrame(CurveSystem)
        self.__line_3.setObjectName(u"__line_3")
        self.__line_3.setFrameShape(QFrame.HLine)
        self.__line_3.setFrameShadow(QFrame.Sunken)

        self.lo_main.addWidget(self.__line_3)

        self.__lb_poly = QLabel(CurveSystem)
        self.__lb_poly.setObjectName(u"__lb_poly")

        self.lo_main.addWidget(self.__lb_poly)

        self.__lo09 = QHBoxLayout()
        self.__lo09.setObjectName(u"__lo09")
        self.bt_p_00 = QToolButton(CurveSystem)
        self.bt_p_00.setObjectName(u"bt_p_00")
        self.bt_p_00.setMaximumSize(QSize(60, 60))
        icon45 = QIcon()
        icon45.addFile(u":/icon/icon/p_00.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_00.setIcon(icon45)
        self.bt_p_00.setIconSize(QSize(55, 55))

        self.__lo09.addWidget(self.bt_p_00)

        self.bt_p_01 = QToolButton(CurveSystem)
        self.bt_p_01.setObjectName(u"bt_p_01")
        self.bt_p_01.setMaximumSize(QSize(60, 60))
        icon46 = QIcon()
        icon46.addFile(u":/icon/icon/p_01.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_01.setIcon(icon46)
        self.bt_p_01.setIconSize(QSize(55, 55))

        self.__lo09.addWidget(self.bt_p_01)

        self.bt_p_02 = QToolButton(CurveSystem)
        self.bt_p_02.setObjectName(u"bt_p_02")
        self.bt_p_02.setMaximumSize(QSize(60, 60))
        icon47 = QIcon()
        icon47.addFile(u":/icon/icon/p_02.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_02.setIcon(icon47)
        self.bt_p_02.setIconSize(QSize(55, 55))

        self.__lo09.addWidget(self.bt_p_02)

        self.bt_p_03 = QToolButton(CurveSystem)
        self.bt_p_03.setObjectName(u"bt_p_03")
        self.bt_p_03.setMaximumSize(QSize(60, 60))
        icon48 = QIcon()
        icon48.addFile(u":/icon/icon/p_03.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_03.setIcon(icon48)
        self.bt_p_03.setIconSize(QSize(55, 55))

        self.__lo09.addWidget(self.bt_p_03)

        self.bt_p_04 = QToolButton(CurveSystem)
        self.bt_p_04.setObjectName(u"bt_p_04")
        self.bt_p_04.setMaximumSize(QSize(60, 60))
        icon49 = QIcon()
        icon49.addFile(u":/icon/icon/p_04.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_04.setIcon(icon49)
        self.bt_p_04.setIconSize(QSize(55, 55))

        self.__lo09.addWidget(self.bt_p_04)

        self.bt_p_05 = QToolButton(CurveSystem)
        self.bt_p_05.setObjectName(u"bt_p_05")
        self.bt_p_05.setMaximumSize(QSize(60, 60))
        icon50 = QIcon()
        icon50.addFile(u":/icon/icon/p_05.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_05.setIcon(icon50)
        self.bt_p_05.setIconSize(QSize(55, 55))

        self.__lo09.addWidget(self.bt_p_05)

        self.lo_main.addLayout(self.__lo09)

        self.__lo10 = QHBoxLayout()
        self.__lo10.setObjectName(u"__lo10")
        self.bt_p_06 = QToolButton(CurveSystem)
        self.bt_p_06.setObjectName(u"bt_p_06")
        self.bt_p_06.setMaximumSize(QSize(60, 60))
        icon51 = QIcon()
        icon51.addFile(u":/icon/icon/p_06.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_06.setIcon(icon51)
        self.bt_p_06.setIconSize(QSize(55, 55))

        self.__lo10.addWidget(self.bt_p_06)

        self.bt_p_07 = QToolButton(CurveSystem)
        self.bt_p_07.setObjectName(u"bt_p_07")
        self.bt_p_07.setMaximumSize(QSize(60, 60))
        icon52 = QIcon()
        icon52.addFile(u":/icon/icon/p_07.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_07.setIcon(icon52)
        self.bt_p_07.setIconSize(QSize(55, 55))

        self.__lo10.addWidget(self.bt_p_07)

        self.bt_p_08 = QToolButton(CurveSystem)
        self.bt_p_08.setObjectName(u"bt_p_08")
        self.bt_p_08.setMaximumSize(QSize(60, 60))
        icon53 = QIcon()
        icon53.addFile(u":/icon/icon/p_08.png", QSize(), QIcon.Normal, QIcon.On)
        self.bt_p_08.setIcon(icon53)
        self.bt_p_08.setIconSize(QSize(55, 55))

        self.__lo10.addWidget(self.bt_p_08)

        self.__sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.__lo10.addItem(self.__sp)

        self.lo_main.addLayout(self.__lo10)

        self.retranslateUi(CurveSystem)

        QMetaObject.connectSlotsByName(CurveSystem)

    # setupUi

    def retranslateUi(self, CurveSystem):
        CurveSystem.setWindowTitle(QCoreApplication.translate("CurveSystem", u"Curve System", None))
        self.__lb_create.setText(QCoreApplication.translate("CurveSystem", u"Create", None))
        self.bt_c_00.setText("")
        self.bt_c_01.setText("")
        self.bt_c_02.setText("")
        self.bt_c_03.setText("")
        self.bt_c_04.setText("")
        self.bt_c_05.setText("")
        self.bt_c_06.setText("")
        self.bt_c_07.setText("")
        self.bt_c_08.setText("")
        self.bt_c_09.setText("")
        self.bt_c_10.setText("")
        self.bt_c_11.setText("")
        self.__lb_edit.setText(QCoreApplication.translate("CurveSystem", u"Edit", None))
        self.bt_e_01.setText("")
        self.bt_e_02.setText("")
        self.bt_e_03.setText("")
        self.bt_e_04.setText("")
        self.bt_e_05.setText("")
        self.bt_e_06.setText("")
        self.bt_e_07.setText("")
        self.bt_e_08.setText("")
        self.bt_e_09.setText("")
        self.bt_e_10.setText("")
        self.bt_e_11.setText("")
        self.bt_e_12.setText("")
        self.bt_e_13.setText("")
        self.bt_e_14.setText("")
        self.bt_e_15.setText("")
        self.__lb_render.setText(QCoreApplication.translate("CurveSystem", u"Render", None))
        self.bt_r_01.setText("")
        self.bt_r_02.setText("")
        self.bt_r_03.setText("")
        self.bt_r_04.setText("")
        self.bt_r_05.setText("")
        self.bt_r_06.setText("")
        self.bt_r_07.setText("")
        self.bt_r_08.setText("")
        self.bt_r_09.setText("")
        self.__lb_surface.setText(QCoreApplication.translate("CurveSystem", u"Surface", None))
        self.bt_s_00.setText("")
        self.bt_s_01.setText("")
        self.bt_s_02.setText("")
        self.bt_s_03.setText("")
        self.__lb_utils.setText(QCoreApplication.translate("CurveSystem", u"Utils and Analysis", None))
        self.bt_u_00.setText("")
        self.bt_u_01.setText("")
        self.bt_u_02.setText("")
        self.bt_u_03.setText("")
        self.bt_a_00.setText("")
        self.bt_a_01.setText("")
        self.__lb_poly.setText(QCoreApplication.translate("CurveSystem", u"Polynomial", None))
        self.bt_p_00.setText("")
        self.bt_p_01.setText("")
        self.bt_p_02.setText("")
        self.bt_p_03.setText("")
        self.bt_p_04.setText("")
        self.bt_p_05.setText("")
        self.bt_p_06.setText("")
        self.bt_p_07.setText("")
        self.bt_p_08.setText("")
    # retranslateUi
