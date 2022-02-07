import gi
from itsdangerous import json
import yapa_main

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class main_window(Gtk.Window):

    def __init__(self) -> None:
        Gtk.Window.__init__(self, title="Yet Another Podcast App")

        self.search_box = Gtk.Box(spacing=6)
        self.add(self.search_box)

        self.search_label = Gtk.Label()
        self.search_label.set_text("Search for Podcast")
        self.search_box.pack_start(self.search_label, True, True, 0)

        self.search_input = Gtk.Entry()
        self.search_box.pack_start(self.search_input, True, True, 0)
        
        self.search_button = Gtk.Button.new_with_label("Search!")
        self.search_button.connect("clicked", self.on_search_clicked)
        self.search_box.pack_start(self.search_button, True, True, 0)


    def on_search_clicked(self, search_button) -> json:
        output = self.search_input.get_text()
        json_data = yapa_main.rss_manipulator().find_cast(output)

        return json_data
        

def main():
    window = main_window()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__=="__main__":
    main()