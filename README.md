# pyqt-listwidget-and-stackedwidget
PyQt QStackedWidget which can be set current widget by clicking QListWidget's item.

## Requirements
PyQt5 >= 5.8

## Included pacakges
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-listwidget-and-stackedwidget.git --upgrade```

## Usage
* ```addTab(widget: QWidget, text: str)``` to add item and widget corresponded with item

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_listwidget_and_stackedwidget import ListWidgetAndStackedWidget

from pyqt_date_table_widget import DateTableWidget
from pyqt_top_left_right_file_list_widget import TopLeftRightFileListWidget
from pyqt_top_menu_bottom_widget import TopMenuBottomWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = ListWidgetAndStackedWidget()
    mainWindow.addTab(DateTableWidget(), 'DateTableWidget')
    mainWindow.addTab(TopLeftRightFileListWidget(), 'TopLeftRightFileListWidget')
    mainWindow.addTab(TopMenuBottomWidget(), 'TopMenuBottomWidget')
    mainWindow.show()
    app.exec_()
```

Used packages in the example
* <a href="https://github.com/yjg30737/pyqt-date-table-widget.git">pyqt-date-table-widget</a>
* <a href="https://github.com/yjg30737/pyqt-top-left-right-file-list-widget.git">pyqt-top-left-right-file-list-widget</a>
* <a href="https://github.com/yjg30737/pyqt-top-menu-bottom-widget.git">pyqt-top-menu-bottom-widget</a>

Result

https://user-images.githubusercontent.com/55078043/150667031-ab3df36c-1ed4-4e57-ac83-a03fdffd138e.mp4


