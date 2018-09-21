#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 24, 2018 5:52:38 AM$"

import sqlite3, tkinter

class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set

class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)
        self.linked_box = None
        self.link_field = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.addl_link_value = None
        self.addl_link_field = None
        self.ids = []

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ', '.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field, addl_link_field=None):
        self.linked_box = widget
        widget.link_field = link_field
        if addl_link_field:
            self.addl_link_field = addl_link_field

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + " = ?" + self.sql_sort
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])
            self.ids.append(value[1])
        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            index = self.curselection()[0]
            value = self.get(index),
            self.linked_box.addl_link_value = self.ids[index]
            if self.addl_link_field:
                values = (value[0],self.addl_link_value)
                link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + " = ? AND " + self.addl_link_field + " = ?", values).fetchone()[1]
            else:
                link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + " = ?", value).fetchone()[1]
            self.linked_box.requery(link_id)


if __name__ == "__main__":
    conn = sqlite3.connect("music.db")

    mainWindow = tkinter.Tk()
    mainWindow.title("Music DB Browser")
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)  # spacer column on the right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
    artistList.config(border=2, relief='sunken')
    artistList.requery()

    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
    albumList.config(border=2, relief='sunken')
    artistList.link(albumList, "artist")

    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainWindow, conn, "songs", "title", sort_order=("track", "title"))
    songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
    songList.config(border=2, relief='sunken')
    albumList.link(songList, "album", addl_link_field="artist")

    mainWindow.mainloop()
    conn.close()
