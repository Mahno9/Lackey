import logging
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction

import PyQt5.uic as uic


class Lackey:
    _jacket = None
    _menu = None

    def __init__(self, jacketUIFile=None):
        logging.debug("Jacket initialize starts.")

        if (jacketUIFile is None) or (not os.path.isfile(jacketUIFile)):
            errorMessage = "Ui form file {0} not found.".format(jacketUIFile)
            logging.error(errorMessage)
            raise FileNotFoundError(errorMessage)

        super().__init__()
        self.initUI(jacketUIFile)

        logging.debug("Jacket initialized successfully.")


    def initUI(self, uiFilename):
        logging.debug("UI initialize starts.")

        self._jacket = uic.loadUi(uifile=uiFilename)
        self._jacket.closeEvent = self.closeEvent
        logging.debug("Jacket main form loaded.")

        iconFilename = 'icon.png'
        self.initTrayIcon(self._jacket, iconFilename)
        self.initTrayMenu(self._jacket)

        self._jacket.show()
        # QToolTip.setFont(QFont('SansSerif', 10))

        logging.debug("UI initialized successfully.")

    def closeEvent(self, event):
        logging.debug("UI close event called.")
        self.deinitTrayIcon()
        event.accept()
        logging.debug("UI close event finished successfully.")

    def initTrayIcon(self, parent, iconFilename):
        logging.debug("Tray icon initialize starts.")

        trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(iconFilename), parent)
        self._menu = QtWidgets.QMenu(parent)
        trayIcon.setContextMenu(self._menu)
        self._jacket.tray_icon = trayIcon
        self._jacket.tray_icon.show()

        logging.debug("Tray icon initialized successfully.")

    def deinitTrayIcon(self):
        self._jacket.tray_icon.hide()
        logging.debug("Tray icon deinit finished successfully.")

    def initTrayMenu(self, parent):
        logging.debug("Tray menu initialize starts.")

        # TODO: Add more actions
        self.exitAction = parent.findChild(QAction, 'action_exit')
        self._menu.addAction(parent.findChild(QAction, 'action_exit'))

        self.aboutAction = parent.findChild(QAction, 'action_about')
        self._menu.addAction(parent.findChild(QAction, 'action_about'))

        logging.debug("Tray menu initialized successfully.")

