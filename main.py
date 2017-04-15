#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import sys
import PyQt5.uic as uic
import logging
import os.path

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton


def createDirIfNeed(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def initLog():
    print("Initialize logging...")
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    fileName = u'Lackey_log_{0}.txt'.format(str(datetime.datetime.now())).replace(':', '')
    fileDir = "log"
    createDirIfNeed(fileDir)
    fileHandler = logging.FileHandler("{0}/{1}.log".format(fileDir, fileName))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)


class Jacket:
    # def __init__(self, flags=Qt.WindowActive, min_width=500, min_height=500, *args, **kwargs):
    # super().__init__(flags, *args, **kwargs)
    jacketForm = None

    def __init__(self, jacketUIFile=None, min_width=500, min_height=500):
        initLog()
        logging.info("Jacket initialize starts.")
        if jacketUIFile is None or not os.path.isfile(jacketUIFile):
            errorMessage = "Ui form file {0} not found.".format(jacketUIFile)
            logging.error(errorMessage)
            raise FileNotFoundError(errorMessage)
        super().__init__()
        self.initUI(jacketUIFile, min_width, min_height)
        logging.info("Jacket initialized successfully.")

    def initUI(self, uiFilename, min_width, min_height):
        logging.info("UI initialize starts.")

        self.jacketForm = uic.loadUi(uifile=uiFilename)
        logging.info("Jacket main form loaded.")

        self.jacketForm.show()
        # QToolTip.setFont(QFont('SansSerif', 10))

        logging.info("UI initialized successfully.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jacket = Jacket('JacketUI.ui')
    sys.exit(app.exec_())
