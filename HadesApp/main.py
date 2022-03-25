import sys
import platform
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


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print("System: " + platform.system())
        print("Version: " + platform.release())

        UIFunctions.removeTitleBar(True)

        self.setWindowTitle("Hades")
        UIFunctions.labelTitle(self, "Hades")
        UIFunctions.labelDescription(self, "Vulnerabilities Scanner")

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

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
            "Settings",
            "btn_settings",
            "url(:/16x16/icons/16x16/cil-equalizer.png)",
            False,
        )

        UIFunctions.selectStandardMenu(self, "btn_home")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        UIFunctions.userIcon(self, "AK", "", True)

        def moveWindow(event):

            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

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

        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            UIFunctions.resetStyle(self, "btn_settings")
            UIFunctions.labelPage(self, "Settings")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")
        if event.buttons() == Qt.MidButton:
            print("Mouse click: MIDDLE BUTTON")

    def keyPressEvent(self, event):
        print("Key: " + str(event.key()) + " | Text Press: " + str(event.text()))

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print("Height: " + str(self.height()) + " | Width: " + str(self.width()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
