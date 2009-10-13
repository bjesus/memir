#!/usr/bin/env python

import gtk
import gobject
import pygtk
import locale

class mygui:
    def on_window1_destroy(self, widget, data=None):
        gtk.main_quit()

    def quit_btn_clicked_cb(self, widget, data=None):
        gtk.main_quit()

    def mk_source_clicked_cb(self, widget, data=None):
        self.input.set_text(self.result.get_text())
        
    def input_changed(self, widget, data=None):
        self.convert()
        
    def result_changed(self, widget, data=None):
        self.output = self.encodings[widget.get_active()]
        self.convert()

    def source_changed(self, widget, data=None):
        self.source = self.encodings[widget.get_active()]
        self.convert()
        
    def convert(self):
        try:
            self.result.set_text(self.input.get_text().encode(self.source).decode(self.output))
        except:
            self.result.set_text(self.input.get_text() + " can't be encoded from "+self.source+" to "+self.output)

    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("memir.glade")
        self.window = builder.get_object("memir")
        self.combo_source = builder.get_object("from_encoding_combo")
        self.combo_output = builder.get_object("to_encoding_combo")
        self.result = builder.get_object("result_output")
        self.input = builder.get_object("source_input")
        self.model = gtk.ListStore(gobject.TYPE_STRING)
        cell = gtk.CellRendererText()
        self.encodings = []
        for code in locale.encodings.aliases.aliases:
            self.model.append([locale.encodings.aliases.aliases[code]])
            self.encodings.append(locale.encodings.aliases.aliases[code])
        self.source = self.encodings[0]
        self.output = self.encodings[0]
        for w in [self.combo_source, self.combo_output]:            
            w.set_model(self.model)
            w.set_active(0)
            w.pack_start(cell, True) 
            w.add_attribute(cell, 'text', 0)
        builder.connect_signals(self)

if __name__ == "__main__":
        gui = mygui()
        gui.window.show()
        gtk.main()
