import sys
from PyQt5.QtWidgets import *
from itsdangerous import json
import yapa_main

class main_window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initUI()


    def initUI(self):      
        self.search_label = QLabel("Search for Podcast")

        self.search_input = QLineEdit()
        
        self.search_button = QPushButton("Search!")
        self.search_button.clicked.connect(self.on_search_clicked)

        self.search_results_list = QListWidget()
        # TODO self.search_results_list.itemClicked(self.list_item_clicked)

        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.search_label, 0, 0)
        self.main_layout.addWidget(self.search_input, 0, 1)
        self.main_layout.addWidget(self.search_button, 0, 2)
        self.main_layout.addWidget(self.search_results_list, 1, 0, 1, 3)



        self.setGeometry(0,0,600,400)
        self.setWindowTitle("YAPAr")
        # self.setWindowIcon(QIcon(''))
        self.show()


    def list_item_clicked(self):
        pass


    def on_search_clicked(self, search_button) -> None:
        output = self.search_input.text()

        json_data = yapa_main.rss_manipulator().find_cast(output)

        i = 0

        for element in json_data['feeds']:
            for key, value in element.items():
                if key == 'title':
                    self.search_results_list.insertItem(i, value)
                    self.search_results_list.repaint()
                    i += 1 


def main():
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
