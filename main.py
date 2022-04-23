import sys
import platform
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

from app_modules import *

from HadesFunctions import HadesFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunctions.setTitleBar(True)

        self.setWindowTitle("Hades")
        UIFunctions.labelTitle(self, "Hades")
        UIFunctions.labelDescription(self, "Vulnerabilities Scanner")

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        UIFunctions.toggleMenu(self, 220, True)

        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True)
        )

        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(
            self, "Home", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True
        )
        UIFunctions.addNewMenu(
            self,
            "Scan",
            "btn_scan",
            "url(:/16x16/icons/16x16/cil-speedometer.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "Help",
            "btn_help",
            "url(:/16x16/icons/16x16/cil-equalizer.png)",
            False,
        )

        UIFunctions.selectStandardMenu(self, "btn_home")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        UIFunctions.userIcon(self, os.getlogin().upper()[:2], "", True)

        def moveWindow(event):

            if UIFunctions.getStatus() == 1:
                UIFunctions.maximize(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.show()

    def Button(self):

        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_scan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_scan)
            UIFunctions.resetStyle(self, "btn_scan")
            UIFunctions.labelPage(self, "Scan")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_help":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_help)
            UIFunctions.resetStyle(self, "btn_help")
            UIFunctions.labelPage(self, "Help")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

 
if __name__ == "__main__":
    if not os.path.exists(os.path.expanduser('~') + "\\HadesFiles\\User.json"):
        HadesFunctions().firstRun()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    