import time
import threading
import queue
import os
import logging

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QEventLoop

from PyQt5.QtWidgets import QListWidgetItem

from monitoring.node_widget import NodeWidget

monitoring_queue = queue.Queue()

Main_form = None


def log(data):
    if Main_form==None:
        logging.debug(data)
    else:
        Main_form.add_queue_data(data)


def add_peer(title, subtitle, iconfilename):
    # Main_form.add_queue_data("log."+title + " peer is added.")
    if Main_form == None:
        logging.debug(title + "("+subtitle+") peer is added.")
    else:
        Main_form.add_node(title, subtitle, iconfilename)


class Form(QtWidgets.QDialog):
    def __init__(self, size=None, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        if size == 'mini':
            self.ui = uic.loadUi("monitoring" + os.sep + "monitoring_mini.ui")
        elif size == 'ex':
            self.ui = uic.loadUi("monitoring" + os.sep + "monitoring_ex.ui")
        else:
            self.ui = uic.loadUi("monitoring" + os.sep + "monitoring.ui")

        self.ui.setWindowFlags(Qt.SplashScreen)                          # 윈도우 타이틀 없애기

        self.ui.listWidget_4.setSpacing(30)

        queue_thread = threading.Thread(target=self.read_queue)
        queue_thread.daemon = True
        queue_thread.start()

        self.ui.show()

    def add_node(self, title, subtitle, iconfilename):
        # Create QCustomQWidget
        myQCustomQWidget = NodeWidget()
        myQCustomQWidget.setTextUp(title)
        myQCustomQWidget.setTextDown(subtitle)
        myQCustomQWidget.setIcon(iconfilename)

        # Create QListWidgetItem
        myQListWidgetItem = QListWidgetItem(self.ui.listWidget_4)

        # Set size hint
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

        # Add QListWidgetItem into QListWidget
        self.ui.listWidget_4.addItem(myQListWidgetItem)
        self.ui.listWidget_4.setItemWidget(myQListWidgetItem, myQCustomQWidget)

    def remove_node(self, index):
        self.ui.listWidget_4.removeItemWidget(self.ui.listWidget_4.takeItem(index))

    def change_status_text(self, message):
        self.ui.label_7.setText(""+message)

    def add_log_item(self, log):
        item = QListWidgetItem(log)
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.scrollToBottom()

    def add_block_item(self, log):
        item = QListWidgetItem(log)
        self.ui.listWidget_3.addItem(item)
        self.ui.listWidget_3.scrollToBottom()

    def add_transaction_item(self, log):
        item = QListWidgetItem(log)
        self.ui.listWidget_2.addItem(item)
        self.ui.listWidget_2.scrollToBottom()

    def reset_transaction_items(self):
        self.ui.listWidget_2.clear()

    def add_voting_item(self, log):
        item = QListWidgetItem(log)
        self.ui.listWidget_5.addItem(item)
        self.ui.listWidget_5.scrollToBottom()

    def change_frame_color(self, r, g, b):
        stylesheet = "background-color: rgb({0}, {1}, {2})".format(r, g, b)
        widget_list = [self.ui.widget, self.ui.widget_2, self.ui.widget_3, self.ui.widget_4, self.ui.widget_5]
        
        for widget in widget_list:
            widget.setStyleSheet(stylesheet)

    def add_queue_data(self, data):
        monitoring_queue.put(data)

    def read_queue(self):
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()
        while True:
            self.change_status_text('Server Status : NOMAL            ' + time.strftime('%H:' + '%M:' + '%S'))

            if monitoring_queue.qsize() > 0:
                datas = monitoring_queue.get()

                data = datas.split('.')

                if data[0] == 'log':
                    add_msg = data[1]
                    for index in range(2, len(data)):
                        add_msg += "." + data[index]
                    self.add_log_item(add_msg)
                elif data[0] == 'block':
                    self.add_block_item(data[1])
                    self.change_frame_color(231, 76, 60)
                    loop = QEventLoop()
                    QTimer.singleShot(1200, loop.quit)
                    loop.exec_()
                    self.change_frame_color(44, 132, 238)
                elif data[0] == 'transaction':
                    add_msg = data[1]
                    for index in range(2, len(data)):
                        add_msg += "." + data[index]
                    self.add_transaction_item(add_msg)
                    self.change_frame_color(241, 196, 15)
                    loop = QEventLoop()
                    QTimer.singleShot(1200, loop.quit)
                    loop.exec_()
                    self.change_frame_color(44, 132, 238)
                elif data[0] == 'voting':
                    add_msg = data[1]
                    for index in range(2, len(data)):
                        add_msg += "." + data[index]
                    self.add_voting_item(add_msg)
                    self.change_frame_color(240, 66, 153)
                    loop = QEventLoop()
                    QTimer.singleShot(1200, loop.quit)
                    loop.exec_()
                    self.change_frame_color(44, 132, 238)
                elif data[0] == 'reset':
                    self.reset_transaction_items()
