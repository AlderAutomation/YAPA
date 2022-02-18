import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from itsdangerous import json
import yapa_main

logo = "/home/matthew/Share/Code/Python/yapa/Static/Images/temp_logo.png"

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
        self.search_results_list.setAlternatingRowColors(True)
        self.search_results_list.itemClicked.connect(self.cast_item_clicked)

        self.episodes = QListWidget()
        self.episodes.setAlternatingRowColors(True)

        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.search_label, 0, 0)
        self.main_layout.addWidget(self.search_input, 0, 1)
        self.main_layout.addWidget(self.search_button, 0, 2)
        self.main_layout.addWidget(self.search_results_list, 1, 0, 1, 2)
        self.main_layout.addWidget(self.episodes, 1, 2, 1, 2)

        self.setGeometry(0,0,600,400)
        self.setWindowTitle("YAPA")
        self.setWindowIcon(QtGui.QIcon(logo))
        self.show()


    def cast_item_clicked(self, item):
        json_data = yapa_main.rss_manipulator().find_cast(item.text())

        id_val = json_data['feeds'][0]['id']

        feed_data = yapa_main.rss_manipulator().get_episodes(id_val)

        i = 0 
        for element in feed_data['items']:
            for key, value in element.items():
                if key == 'title':
                    title = value

                    self.episodes.addItem(title)
                    self.episodes.repaint()
                    i += 1 


    def on_search_clicked(self, search_button) -> None:
        output = self.search_input.text()

        json_data = yapa_main.rss_manipulator().find_cast(output)

        i = 0

        for element in json_data['feeds']:
            for key, value in element.items():
                if key == 'title':
                    title = value

                    self.search_results_list.addItem(title)
                    self.search_results_list.repaint()
                    i += 1 


def main():
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())   

if __name__=="__main__":
    main()
