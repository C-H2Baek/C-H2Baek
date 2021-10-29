import os
import random
from PyQt5.QtWidgets import \
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QEventLoop, QTimer, Qt
from PyQt5.QtGui import QPixmap


path = "Images/gif"  # 이미지 디렉토리
file_name = os.listdir(path)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._timer = QTimer()
        self._timer.timeout.connect(self.image_timer)
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._start_btn = QPushButton("시작", self)
        self._start_btn.setStyleSheet("background-color: #FFF;")
        self._start_btn.clicked.connect(self.start)
        self._image = QLabel(self)
        self._image.setStyleSheet("background-color: transparent;")
        self._image.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(self._start_btn)
        self._layout.addWidget(self._image)
        self.setStyleSheet("background-color: #000;")
        self.setLayout(self._layout)
        self.show()

    def start(self):
        self._start_btn.hide()
        self._timer.start(1)

    def update_image(self):
        pixmap = QPixmap()
        pixmap.load(f"{path}/{random.choice(file_name)}")
        w_ratio = self.height() / self.width()
        p_ratio = pixmap.height() / pixmap.width()
        if w_ratio < p_ratio:
            ratio = pixmap.width() / pixmap.height()
            pixmap = pixmap.scaled(int(self.height() * ratio), self.height())
        else:
            ratio = pixmap.height() / pixmap.width()
            pixmap = pixmap.scaled(self.width(), int(self.width() * ratio))
        self._image.setPixmap(pixmap)

    def image_timer(self):
        self._timer.stop()
        self.update_image()
        self._image.show()
        self.sleep(10000)
        self._image.hide()
        self._timer.start(5000)

    @staticmethod
    def sleep(time):
        loop = QEventLoop()
        QTimer.singleShot(time, loop.quit)
        loop.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()