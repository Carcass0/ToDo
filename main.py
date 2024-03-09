from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QMainWindow

from taskbox import Ui_Form
from mainwindow import Ui_MainWindow
from stylesheets import SCROLL_AREA_STYLESHEET, MAIN_WINDOW_STYLESHEET


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class TaskContainer(QWidget):

    def __init__(self):
        super(TaskContainer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__=="__main__":
    app = QApplication([])
    main_widget = MainWindow()
    #main_widget.setStyleSheet(MAIN_WINDOW_STYLESHEET)
    main_widget.setContentsMargins(0,0,0,0)
    scroll_widget = QWidget()
    scroll_layout = QVBoxLayout(scroll_widget)
    scroll_layout.setSpacing(0)
    scroll_layout.setContentsMargins(0,0,0,0)
    scroll_widget.setContentsMargins(0,0,0,0)
    for _ in range(5):
        widget = QWidget()
        ui = Ui_Form()
        ui.setupUi(widget)
        scroll_layout.addWidget(widget)
    scroll_area = QScrollArea()
    scroll_area.setWidget(scroll_widget)
    scroll_area.setWidgetResizable(True)
    scroll_area.setContentsMargins(0,0,0,0)
    scroll_area.setStyleSheet(SCROLL_AREA_STYLESHEET)
    main_widget.ui.centralLayout.addWidget(scroll_area)
    main_widget.show()
    app.exec()
