from mailcap import findmatch
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import uic
import yapa_main

logo = "/home/matthew/Share/Code/Python/yapa/Static/Images/temp_logo.png"

class main_window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initUI()


    def initUI(self):  
        uic.loadUi("main.ui", self)

        self.search_input = self.findChild(QLineEdit, "search_input")
        self.search_button = self.findChild(QPushButton, "search_button")
        self.podcast_search_results_list = self.findChild(QListWidget, "podcast_search_results_list")
        self.episodes = self.findChild(QListWidget, "episode_list")

        self.search_button.clicked.connect(self.on_search_clicked)
        self.podcast_search_results_list.itemClicked.connect(self.cast_item_clicked)

        self.show()


    def cast_item_clicked(self, item):
        self.episodes.clear()
        
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

                    self.podcast_search_results_list.addItem(title)
                    self.podcast_search_results_list.repaint()
                    i += 1 


def main():
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())   

if __name__=="__main__":
    main()
