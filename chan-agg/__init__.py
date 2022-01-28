from fourchan import FourChan, Post
from design import BoardDesign
import random
import sys
from PySide6 import QtCore, QtWidgets, QtGui


class BoardTab(QtWidgets.QWidget):
    def __init__(self, post: list):
        super().__init__(None)
        layout = QtWidgets.QVBoxLayout()
        for i in post:
            label = QtWidgets.QLabel(self)
            label.setText(i.post_msg)
            label.setWordWrap(True)
            layout.addWidget(label)
        self.setLayout(layout)


class Tabs(QtWidgets.QTabWidget):
    def __init__(self, parent, four_chan: FourChan):
        super().__init__(parent)
        self.board = four_chan
        posts = self.board.get_board("g")
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(BoardTab(posts))
        self.addTab(self.scroll_area, "g")


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        four_chan = FourChan()

        tabs = Tabs(self, four_chan)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Windows")

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
