from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFrame, QLabel
from PyQt5.QtGui import QFont, QIcon, QPainterPath, QRegion
from PyQt5.QtCore import Qt, QPoint


class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setMouseTracking(True)
        self.mouse_pressed = False
        self.mouse_position = QPoint()
        self.edge_thickness = 10
        self.left_edge_dragging = False
        self.right_edge_dragging = False
        self.top_edge_dragging = False
        self.bottom_edge_dragging = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_position = event.globalPos() - self.parent().frameGeometry().topLeft()
            self.mouse_pressed = True

            # Redimensionnement des bords
            if self.edge_thickness >= event.x() >= 0:
                self.left_edge_dragging = True
            elif self.parent().width() - self.edge_thickness <= event.x() <= self.parent().width():
                self.right_edge_dragging = True

            if self.edge_thickness >= event.y() >= 0:
                self.top_edge_dragging = True
            elif self.parent().height() - self.edge_thickness <= event.y() <= self.parent().height():
                self.bottom_edge_dragging = True

            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False
            self.left_edge_dragging = False
            self.right_edge_dragging = False
            self.top_edge_dragging = False
            self.bottom_edge_dragging = False

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            if not (self.left_edge_dragging or self.right_edge_dragging or self.top_edge_dragging or self.bottom_edge_dragging):
                self.parent().move(event.globalPos() - self.mouse_position)
            else:
                if self.left_edge_dragging:
                    new_width = self.parent().width() - (event.globalPos().x() - self.parent().x())
                    if new_width > self.parent().minimumWidth():
                        self.parent().setGeometry(event.globalPos().x(), self.parent().y(), new_width, self.parent().height())
                elif self.right_edge_dragging:
                    new_width = event.globalPos().x() - self.parent().x()
                    if new_width > self.parent().minimumWidth():
                        self.parent().resize(new_width, self.parent().height())

                if self.top_edge_dragging:
                    new_height = self.parent().height() - (event.globalPos().y() - self.parent().y())
                    if new_height > self.parent().minimumHeight():
                        self.parent().setGeometry(self.parent().x(), event.globalPos().y(), self.parent().width(), new_height)
                elif self.bottom_edge_dragging:
                    new_height = event.globalPos().y() - self.parent().y()
                    if new_height > self.parent().minimumHeight():
                        self.parent().resize(self.parent().width(), new_height)

            event.accept()


# The rest of the CustomWindow class code remains the same


class CustomWindow(QMainWindow):
    def __init__(self, title, window_size, btn_close, btn_minimize=None, btn_show=None, stylesheet_path=None):
        super().__init__()
        self.init_UI(title, window_size, btn_close, btn_minimize, btn_show, stylesheet_path)

    def init_UI(self, title, window_size, btn_close, btn_minimize, btn_show, stylesheet_path):
        self.title = title
        self.btn_close = btn_close
        self.btn_minimize = btn_minimize
        self.btn_show = btn_show

        if stylesheet_path:
            with open(stylesheet_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)


        self.minimize_icon = QIcon(btn_minimize)
        self.show_icon = QIcon(btn_show)


        width, height = map(int, window_size.split("x"))


        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)


        self.central_widget = QFrame()
        self.setFixedSize(width, height)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setObjectName("centralFrame")

        self.set_hexagon_shape()

        self.title_bar = CustomTitleBar(self)
        self.title_bar.setGeometry(0, 0, self.width(), 30)

        self.hide_button = QPushButton(self.title_bar)
        if btn_minimize:
            self.hide_button.setIcon(QIcon(btn_minimize))
        self.hide_button.setGeometry(0, 5, 30, 20)
        self.hide_button.setStyleSheet("background-color: transparent;")
        self.hide_button.clicked.connect(self.toggle_window)

        self.title_label = QLabel(title, self.title_bar, objectName="title")
        self.title_label.setGeometry(28, 5, 200, 20)
        self.title_label.setStyleSheet("background-color: transparent;")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)

        self.close_button = QPushButton(self.title_bar)
        if btn_close:
            self.close_button.setIcon(QIcon(btn_close))
        self.close_button.setGeometry(width - 30, 5, 20, 20)
        self.close_button.setStyleSheet("background-color: transparent;")
        self.close_button.clicked.connect(self.close_application)






        # Create a new widget for the close button
        self.close_button_widget = QWidget()
        self.close_button_widget.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.close_button_widget.setAttribute(Qt.WA_NoSystemBackground, True)
        self.close_button_widget.setAttribute(Qt.WA_TranslucentBackground, True)

        # Move the close button to the new widget
        self.close_button.setParent(self.close_button_widget)
        self.close_button.setGeometry(0,2, 20, 20)
        self.close_button.clicked.connect(self.close)

        # Show the close button widget
        self.close_button_widget.show()



    def moveEvent(self, event):
        new_pos = self.mapToGlobal(QPoint(self.width() - 10, 0))
        self.close_button_widget.move(new_pos)



    def set_hexagon_shape(self):
        path = QPainterPath()
        path.moveTo(30, 0)
        path.lineTo(self.width() - 20, 0)
        path.lineTo(self.width(), 20)
        path.lineTo(self.width(), self.height() - 0)
        path.lineTo(self.width() - 20, self.height())
        path.lineTo(20, self.height())
        path.lineTo(0, self.height() - 20)
        path.lineTo(0, 0)
        path.closeSubpath()

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def toggle_window(self):
        if self.central_widget.isVisible():
            self.central_widget.hide()
            self.title_label.hide()
            self.close_button_widget.hide()
            self.hide_button.setIcon(self.show_icon) 
        else:
            self.central_widget.show()
            self.title_label.show()
            self.close_button_widget.show()
            self.hide_button.setIcon(self.minimize_icon)

    def close_application(self):
        self.close()

