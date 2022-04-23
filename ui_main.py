from re import S
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from HadesFunctions import HadesFunctions

import files_rc

class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 830)
        MainWindow.setMinimumSize(QSize(1280, 800))
        self.HadesFunctions = HadesFunctions()
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_credits = QLabel(self.centralwidget)
        self.label_credits.setObjectName(u"label_credits")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout.addWidget(self.label_credits)

        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_title_bar_top.setFont(font2)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns_right)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy2.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy2)
        self.btn_maximize.setMinimumSize(QSize(40, 0))
        self.btn_maximize.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        self.label_top_info_1.setFont(font1)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(32)
        self.label_3.setFont(font5)

        self.horizontalLayout_14.addWidget(self.label_3)

        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)

        self.horizontalLayout_14.addWidget(self.label_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.stackedWidget.addWidget(self.page_home)
        self.page_scan = QWidget()
        self.page_scan.setObjectName(u"page_scan")
        self.verticalLayout_7 = QVBoxLayout(self.page_scan)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_scan = QPushButton(self.page_scan, clicked = lambda: self.runScan())
        self.btn_scan.setObjectName(u"btn_scan")
        self.btn_scan.setMinimumSize(QSize(871, 93))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(17)
        self.btn_scan.setFont(font6)
        self.btn_scan.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-media-play.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_scan)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget = QTableWidget(self.page_scan)
        self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setPointSize(13)
        self.tableWidget.setFont(font7)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.tableWidget)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.total_files = QLabel(self.page_scan)
        self.total_files.setObjectName(u"total_files")
        self.total_files.setEnabled(True)
        self.total_files.setFont(font1)
        self.total_files.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.total_files.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.total_files)

        self.winver = QLabel(self.page_scan)
        self.winver.setObjectName(u"winver")
        self.winver.setFont(font1)
        self.winver.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.verticalLayout_8.addWidget(self.winver)

        self.total_vulnerablities = QLabel(self.page_scan)
        self.total_vulnerablities.setObjectName(u"total_vulnerablities")
        self.total_vulnerablities.setFont(font1)
        self.total_vulnerablities.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.verticalLayout_8.addWidget(self.total_vulnerablities)
        self.btn_viewscore = QPushButton(self.page_scan, clicked = lambda: self.viewScore())
        self.btn_viewscore.setObjectName(u"btn_viewscore")
        self.btn_viewscore.setMinimumSize(QSize(179, 50))
        self.btn_viewscore.setFont(font4)
        self.btn_viewscore.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-chart-line.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_viewvulnerablefilenames = QPushButton(self.page_scan, clicked = lambda: self.viewVulnerablefilenames())
        self.btn_viewvulnerablefilenames.setObjectName(u"btn_viewvulnerablefilenames")
        self.btn_viewvulnerablefilenames.setMinimumSize(QSize(179, 50))
        fontv = QFont()
        fontv.setPointSize(8)
        self.btn_viewvulnerablefilenames.setFont(fontv)
        self.btn_viewvulnerablefilenames.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-chart-line.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_viewscore)
        self.verticalLayout_8.addWidget(self.btn_viewvulnerablefilenames)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.page_scan)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.verticalLayout_6 = QVBoxLayout(self.page_help)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.page_help)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.page_help1 = QWidget()
        self.page_help1.setObjectName(u"page_help")
        self.verticalLayout_6 = QVBoxLayout(self.page_help1)

        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_help)
        self.stackedWidget.addWidget(self.page_help1)
        self.page_score = QWidget()
        self.page_score.setObjectName(u"page_score")
        self.gridLayoutWidget = QWidget(self.page_score)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1280, 720))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        font8 = QFont()
        font8.setPointSize(12)

        self.IntegrityImage = QLabel(self.gridLayoutWidget)
        self.IntegrityImage.setObjectName(u"IntegrityImage")
        self.IntegrityImage.setFont(font8)
        self.IntegrityImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.IntegrityImage, 0, 0, 1, 1)

        self.AvailabilityImage = QLabel(self.gridLayoutWidget)
        self.AvailabilityImage.setObjectName(u"AvailabilityImage")
        self.AvailabilityImage.setFont(font8)
        self.AvailabilityImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.AvailabilityImage, 0, 1, 1, 1)

        self.ComplexityImage = QLabel(self.gridLayoutWidget)
        self.ComplexityImage.setObjectName(u"ComplexityImage")
        self.ComplexityImage.setFont(font8)
        self.ComplexityImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ComplexityImage, 0, 2, 1, 1)

        self.ConfidentialityImage = QLabel(self.gridLayoutWidget)
        self.ConfidentialityImage.setObjectName(u"ConfidentialityImage")
        self.ConfidentialityImage.setFont(font8)
        self.ConfidentialityImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ConfidentialityImage, 2, 0, 1, 1)

        self.AccessImage = QLabel(self.gridLayoutWidget)
        self.AccessImage.setObjectName(u"AccessImage")
        self.AccessImage.setFont(font8)
        self.AccessImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.AccessImage, 2, 1, 1, 1)

        self.AuthenticationImage = QLabel(self.gridLayoutWidget)
        self.AuthenticationImage.setObjectName(u"AuthenticationImage")
        self.AuthenticationImage.setFont(font8)
        self.AuthenticationImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.AuthenticationImage, 2, 2, 1, 1)

        self.Integrity = QLabel(self.gridLayoutWidget)
        self.Integrity.setObjectName(u"Integrity")
        self.Integrity.setFont(font8)
        self.Integrity.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Integrity, 1, 0, 1, 1)

        self.Availability = QLabel(self.gridLayoutWidget)
        self.Availability.setObjectName(u"Availability")
        self.Availability.setFont(font8)
        self.Availability.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Availability, 1, 1, 1, 1)

        self.Complexity = QLabel(self.gridLayoutWidget)
        self.Complexity.setObjectName(u"Complexity")
        self.Complexity.setFont(font8)
        self.Complexity.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Complexity, 1, 2, 1, 1)

        self.Confidentiality = QLabel(self.gridLayoutWidget)
        self.Confidentiality.setObjectName(u"Confidentiality")
        self.Confidentiality.setFont(font8)
        self.Confidentiality.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Confidentiality, 3, 0, 1, 1)

        self.Access = QLabel(self.gridLayoutWidget)
        self.Access.setObjectName(u"Access")
        self.Access.setFont(font8)
        self.Access.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Access, 3, 1, 1, 1)

        self.Authentication = QLabel(self.gridLayoutWidget)
        self.Authentication.setObjectName(u"Authentication")
        self.Authentication.setFont(font8)
        self.Authentication.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Authentication, 3, 2, 1, 1)

        

        self.stackedWidget.addWidget(self.page_score)

        ############################ Vuln PAGE ##################################
        self.page_vuln = QWidget()
        self.page_vuln.setObjectName(u"page_score")
        self.stackedWidget.addWidget(self.page_vuln)
        self.tableWidgetVuln = QTableWidget(self.page_vuln)
        self.tableWidgetVuln.setColumnCount(2)
		
        __qtablewidgetitemFlaggedString = QTableWidgetItem()
        self.tableWidgetVuln.setHorizontalHeaderItem(0, __qtablewidgetitemFlaggedString)
		
        __qtablewidgetitemPath = QTableWidgetItem()
        self.tableWidgetVuln.setHorizontalHeaderItem(1, __qtablewidgetitemPath)
		
        self.tableWidgetVuln.setObjectName(u"tableWidget")
        self.tableWidgetVuln.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setPointSize(13)
        self.tableWidgetVuln.setFont(font7)
        self.tableWidgetVuln.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        

        __qtablewidgetitemFlaggedString = self.tableWidgetVuln.horizontalHeaderItem(0)  
        __qtablewidgetitemFlaggedString.setText(QCoreApplication.translate("MainWindow", u"Flagged String", None));
        __qtablewidgetitemPath = self.tableWidgetVuln.horizontalHeaderItem(1)
        __qtablewidgetitemPath.setText(QCoreApplication.translate("MainWindow", u"Path", None));

        self.tableWidgetVuln.setMinimumSize(QSize(1000, 500))
        self.tableWidgetVuln.setColumnWidth(1,750)
        
        ############################ Vuln PAGE ##################################

        ############################ HELP PAGE ##################################
        self.gridLayoutHelpWidgetHelp = QWidget(self.page_help)
        self.gridLayoutHelpWidgetHelp.setObjectName(u"gridLayoutHelpWidgetHelp")
        self.gridLayoutHelpWidgetHelp.setGeometry(QRect(10, 10, 1200, 700))
        self.gridLayoutHelp = QGridLayout(self.gridLayoutHelpWidgetHelp)
        self.gridLayoutHelp.setObjectName(u"gridLayoutHelp")
        self.gridLayoutHelp.setContentsMargins(0, 0, 0, 0)
        
        self.gridLayoutHelpWidgetHelp1 = QWidget(self.page_help1)
        self.gridLayoutHelpWidgetHelp1.setObjectName(u"gridLayoutHelpWidgetHelp1")
        self.gridLayoutHelpWidgetHelp1.setGeometry(QRect(10, 10, 1200, 700))
        self.gridLayoutHelp1 = QGridLayout(self.gridLayoutHelpWidgetHelp1)
        self.gridLayoutHelp1.setObjectName(u"gridLayoutHelp")
        self.gridLayoutHelp1.setContentsMargins(0, 0, 0, 0)

        font8 = QFont()
        font8.setPointSize(10)
        
        self.CVSSHelp = QLabel(self.gridLayoutHelpWidgetHelp)
        self.CVSSHelp.setObjectName(u"CVSSHelp")
        self.CVSSHelp.setFont(font8)
        self.CVSSHelp.setAlignment(Qt.AlignCenter)

        self.CVSSHelp.setText("""CVSS score
        The Common Vulnerability Scoring System (also known as CVSS Scores) assigns a number value (0-10) to the severity of a security vulnerability.""")

        self.gridLayoutHelp.addWidget(self.CVSSHelp)

        self.IntegrityHelp = QLabel(self.gridLayoutHelpWidgetHelp)
        self.IntegrityHelp.setObjectName(u"IntegrityHelp")
        self.IntegrityHelp.setFont(font8)
        self.IntegrityHelp.setAlignment(Qt.AlignCenter)

        self.IntegrityHelp.setText("""Integrity
The Integrity metric describes the impact on the victims data

        None=There is no impact.
Partial=Modification of some data or system files is possible.
Complete=There is total loss of integrity; the attacker can modify any files or information on the target system.	""")

        self.gridLayoutHelp.addWidget(self.IntegrityHelp)

        self.AvailabilityHelp = QLabel(self.gridLayoutHelpWidgetHelp)
        self.AvailabilityHelp.setObjectName(u"AvailabilityHelp")
        self.AvailabilityHelp.setFont(font8)
        self.AvailabilityHelp.setAlignment(Qt.AlignCenter)

        self.AvailabilityHelp.setText("""Availability
The availability metric describes the impact on the availability of the target system. Attacks that consume network bandwidth, processor cycles, memory or any other resources

None=There is no impact
Partial=There is reduced performance or loss of some functionality.
Complete=There is total loss of availability of the attacked resource.""")

        self.gridLayoutHelp.addWidget(self.AvailabilityHelp)

        self.ComplexityHelp = QLabel(self.gridLayoutHelpWidgetHelp)
        self.ComplexityHelp.setObjectName(u"ComplexityHelp")
        self.ComplexityHelp.setFont(font8)
        self.ComplexityHelp.setAlignment(Qt.AlignCenter)

        self.ComplexityHelp.setText("""Complexity
The complexity metric describes how difficult it is to exploit a vulnerability.

High=Difficult to exploit or requires social engineering methods that would be easily noticed by people.
Medium=There are some additional requirements for the attack
Low=There are no special conditions for exploiting the vulnerability making it easy to exploit""")

        self.gridLayoutHelp.addWidget(self.ComplexityHelp)

        self.btn_nextPageHelp = QPushButton(self.page_help, clicked = lambda: self.stackedWidget.setCurrentWidget(self.page_help1))
        self.btn_nextPageHelp.setObjectName(u"btn_nextPageHelp")
        self.btn_nextPageHelp.setMinimumSize(QSize(179, 50))
        self.btn_nextPageHelp.setFont(font4)
        self.btn_nextPageHelp.setStyleSheet(u"QPushButton {\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_nextPageHelp.setText("Next Page")
        
        self.gridLayoutHelp1.addWidget(self.ComplexityHelp)

        self.ConfidentialityHelp = QLabel(self.gridLayoutHelpWidgetHelp1)
        self.ConfidentialityHelp.setObjectName(u"ConfidentialityHelp")
        self.ConfidentialityHelp.setFont(font8)
        self.ConfidentialityHelp.setAlignment(Qt.AlignCenter)

        self.ConfidentialityHelp.setText("""Confidentiality
The confidentiality metric describes the impact on the confidentiality of data processed by the system.

None=There is no impact.
Partial=There is considerable disclosure of information.	
Complete=There is total information disclosure, providing access to any / all data on the system.""")

        self.gridLayoutHelp1.addWidget(self.ConfidentialityHelp)

        self.AccessHelp = QLabel(self.gridLayoutHelpWidgetHelp1)
        self.AccessHelp.setObjectName(u"AccessHelp")
        self.AccessHelp.setFont(font8)
        self.AccessHelp.setAlignment(Qt.AlignCenter)

        self.AccessHelp.setText("""Access Vector
The access vector depicts how a security flaw can be exploited.


Local = must either have physical access to the vulnerable system or a local account
Local Network = must have access to the broadcast or collision domain of the vulnerable system 	
Remote = an attacker can gain access through a network connection from a geographical  distance""")

        self.gridLayoutHelp1.addWidget(self.AccessHelp)

        self.AuthenticationHelp = QLabel(self.gridLayoutHelpWidgetHelp1)
        self.AuthenticationHelp.setObjectName(u"AuthenticationHelp")
        self.AuthenticationHelp.setFont(font8)
        self.AuthenticationHelp.setAlignment(Qt.AlignCenter)

        self.AuthenticationHelp.setText("""Authentication
The authentication metric describes the number of times that an attacker must authenticate to a target to exploit it. 

Multiple=Exploitation of the vulnerability requires that the attacker authenticate two or more times
Single=The attacker must authenticate once
Not required=There is no requirement required""")

        self.gridLayoutHelp1.addWidget(self.AuthenticationHelp)

        self.btn_nextPageHelp1 = QPushButton(self.page_help1, clicked = lambda: self.stackedWidget.setCurrentWidget(self.page_help))
        self.btn_nextPageHelp1.setObjectName(u"btn_nextPageHelp1")
        self.btn_nextPageHelp1.setMinimumSize(QSize(179, 50))
        self.btn_nextPageHelp1.setFont(font4)
        self.btn_nextPageHelp1.setStyleSheet(u"QPushButton {\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_nextPageHelp1.setText("Back")
        

        self.stackedWidget.addWidget(self.page_help)
         ############################ HELP PAGE ##################################

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font1)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize)
        QWidget.setTabOrder(self.btn_maximize, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_credits.setText("")
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Hades", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"AK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/Logo/icons/logo/hadestransparent.png\"/><span style=\" font-size:48pt;\">Hades</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Last Scan:" + self.HadesFunctions.updateLastScan() + "</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Scan Count:" + self.HadesFunctions.updateScanCount() + "</p></body></html>", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Run Scan", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)  
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CVSS Score", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Number Of Vulnerabilities", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Percentage", None));
        self.tableWidget.setColumnWidth(1,750)

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.total_files.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Total Files Scanned: </p></body></html>", None))
        self.winver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Windows Version:</p></body></html>", None))
        self.total_vulnerablities.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Vulnerable File Names:</p></body></html>", None))
        self.btn_viewscore.setText(QCoreApplication.translate("MainWindow", u"View Score", None))
        self.btn_viewvulnerablefilenames.setText(QCoreApplication.translate("MainWindow", u"View Vulnerable Files", None))

    def runScan(self):
        self.btn_scan.setText("Scanning")
        QCoreApplication.processEvents()
        self.HadesFunctions.scan()
        self.btn_scan.setText("Run Scan")
        self.loadData()
        

    def viewScore(self):
        try:
                
                self.IntegrityImage.setText(self.HadesFunctions.getScoreColourFile("Integrity"))
                self.AvailabilityImage.setText(self.HadesFunctions.getScoreColourFile("Availability"))
                self.ComplexityImage.setText(self.HadesFunctions.getScoreColourFile("Complexity"))
                self.ConfidentialityImage.setText(self.HadesFunctions.getScoreColourFile("Confidentiality"))
                self.AccessImage.setText(self.HadesFunctions.getScoreColourFile("Access"))
                self.AuthenticationImage.setText(self.HadesFunctions.getScoreColourFile("Authentication"))

                self.Integrity.setText(self.HadesFunctions.getScoreColourInfo("Integrity"))
                self.Availability.setText(self.HadesFunctions.getScoreColourInfo("Availability"))
                self.Complexity.setText(self.HadesFunctions.getScoreColourInfo("Complexity"))
                self.Confidentiality.setText(self.HadesFunctions.getScoreColourInfo("Confidentiality"))
                self.Access.setText(self.HadesFunctions.getScoreColourInfo("Access"))
                self.Authentication.setText(self.HadesFunctions.getScoreColourInfo("Authentication"))
                self.stackedWidget.setCurrentWidget(self.page_score)
        
        except:
                print("Press scan first")
    
    def loadData(self):
        tableData = self.HadesFunctions.getTableData()
        row = 0
        self.tableWidget.setRowCount(len(tableData))
        self.tableWidget.verticalHeader().setVisible(False)
        for data in tableData:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(data["scoreRange"]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(data["noOfVulnerabilities"])))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(data["percentageOfTotal"])))
                row += 1
        scanInfo = self.HadesFunctions.getScanInfo()
        self.total_files.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Total Files Scanned: {}</p></body></html>".format(scanInfo[0]), None))
        self.winver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Windows Version: {}</p></body></html>".format(scanInfo[1]), None))
        self.total_vulnerablities.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Vulnerable File Names: {}</p></body></html>".format(scanInfo[2]), None))
    
    def viewVulnerablefilenames(self):
        tableData = self.HadesFunctions.getVulnerableNames()
        row = 0
        self.tableWidgetVuln.setRowCount(len(tableData))
        self.tableWidgetVuln.verticalHeader().setVisible(False)
        for data in tableData:
                self.tableWidgetVuln.setItem(row, 0, QTableWidgetItem(str(data[0][0])))
                self.tableWidgetVuln.setItem(row, 1, QTableWidgetItem(data[1]))
                row += 1
        self.stackedWidget.setCurrentWidget(self.page_vuln)