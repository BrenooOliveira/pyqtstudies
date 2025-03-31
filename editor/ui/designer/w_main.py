# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.f_menu = QFrame(self.centralwidget)
        self.f_menu.setObjectName(u"f_menu")
        self.f_menu.setGeometry(QRect(0, 60, 120, 481))
        self.f_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.f_header = QFrame(self.centralwidget)
        self.f_header.setObjectName(u"f_header")
        self.f_header.setGeometry(QRect(120, 0, 671, 61))
        self.f_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.f_header)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 10, 352, 41))
        self.nav = QHBoxLayout(self.horizontalLayoutWidget)
        self.nav.setObjectName(u"nav")
        self.nav.setContentsMargins(0, 0, 0, 0)
        self.bt_new = QCommandLinkButton(self.horizontalLayoutWidget)
        self.bt_new.setObjectName(u"bt_new")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.bt_new.setIcon(icon)

        self.nav.addWidget(self.bt_new)

        self.bt_open = QCommandLinkButton(self.horizontalLayoutWidget)
        self.bt_open.setObjectName(u"bt_open")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.bt_open.setIcon(icon1)

        self.nav.addWidget(self.bt_open)

        self.f_logo = QFrame(self.centralwidget)
        self.f_logo.setObjectName(u"f_logo")
        self.f_logo.setGeometry(QRect(0, 0, 121, 61))
        self.f_logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_logo.setFrameShadow(QFrame.Shadow.Raised)
        self.img_logo = QLabel(self.f_logo)
        self.img_logo.setObjectName(u"img_logo")
        self.img_logo.setGeometry(QRect(10, 10, 101, 41))
        self.img_logo.setPixmap(QPixmap(u"../../assets/logo.png"))
        self.img_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.f_logo_2 = QFrame(self.centralwidget)
        self.f_logo_2.setObjectName(u"f_logo_2")
        self.f_logo_2.setGeometry(QRect(120, 60, 671, 481))
        self.f_logo_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_logo_2.setFrameShadow(QFrame.Shadow.Raised)
        self.img_bg_logo = QLabel(self.f_logo_2)
        self.img_bg_logo.setObjectName(u"img_bg_logo")
        self.img_bg_logo.setGeometry(QRect(10, 10, 651, 461))
        self.img_bg_logo.setPixmap(QPixmap(u"../../assets/logo_bg.png"))
        self.img_bg_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_new.setText(QCoreApplication.translate("MainWindow", u"Novo Arquivo", None))
        self.bt_open.setText(QCoreApplication.translate("MainWindow", u"Abrir Arquivo", None))
        self.img_logo.setText("")
        self.img_bg_logo.setText("")
    # retranslateUi

