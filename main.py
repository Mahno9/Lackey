#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import logging
import os.path
import sys
from PyQt5.QtWidgets import QApplication

from Lackey import Lackey

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



if __name__ == '__main__':
    initLog()
    app = QApplication(sys.argv)
    jacket = Lackey('JacketUI.ui')
    sys.exit(app.exec_())
