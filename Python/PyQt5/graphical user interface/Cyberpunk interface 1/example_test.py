import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout
from cypunk1 import cypunk1Window

class MyApp(cypunk1Window):
    def __init__(self):

        #You can set here the things
        super().__init__(
            title="Test",
            window_size="900x200",
            btn_close="ico/close.png",
            btn_minimize="ico/open.png",
            btn_show="ico/hide.png",
            stylesheet_path="style/style1.txt"
        )

        self.GUI()

    def GUI(self):
        layout = QVBoxLayout()

        button1 = QPushButton("Bouton 1")
        layout.addWidget(button1)

        button2 = QPushButton("Bouton 2")
        layout.addWidget(button2)

        button3 = QPushButton("Bouton 3")
        layout.addWidget(button3)

        self.central_widget.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
