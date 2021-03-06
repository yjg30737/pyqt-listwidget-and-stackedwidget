from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidget, QListView, QVBoxLayout, \
    QStackedWidget
from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


class ListWidgetAndStackedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__listWidget = QListWidget()
        self.__listWidget.setFlow(QListView.LeftToRight)
        PyQtResourceHelper.setStyleSheet([self.__listWidget], ['style/list_widget.css'])
        self.__listWidget.setMaximumHeight(self.__listWidget.fontMetrics().boundingRect('M').height() * 2)
        self.__listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.__stackedWidget = QStackedWidget()

        lay = QVBoxLayout()
        lay.addWidget(self.__listWidget)
        lay.addWidget(self.__stackedWidget)

        self.setLayout(lay)

        self.__listWidget.currentRowChanged.connect(self.__stackedWidget.setCurrentIndex)

    def addTab(self, widget: QWidget, text: str):
        self.__listWidget.addItem(text)
        self.__stackedWidget.addWidget(widget)

