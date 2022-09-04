from tkinter import *
import lorem
from modules import modules

modules = modules()

class app:
    def __init__(self, master):
        note_names = modules.get_note_list()
        settings = modules.load_settings()
        self.bg_color = settings['bg']
        self.bt_color = settings['bt']
        self.fg_color = settings['fg']
        fm = Frame(master)
        Label(fm, text="Notes", font=('Aerial 14'), background=self.bg_color).pack(anchor=CENTER)
        self.listbox = Listbox(fm, height=15,
                          width=30,
                          bg=self.bg_color,
                          fg=self.fg_color,
                          activestyle='dotbox',
                          font="Helvetica")
        self.textBox = Text(fm, height=1, width=30, bg=self.bg_color, wrap='none', fg=self.fg_color)
        buttonCommit = Button(fm, height=1, width=5, text="Add",
                              command=lambda: self.retrieve_input(), bg=self.bt_color)
        buttonOpen = Button(fm, height=1, width=6, text="Open",
                              command=lambda: self.selected_item(), bg=self.bt_color)
        buttonDelete = Button(fm, height=1, width=6, text="Delete", background=self.bt_color,
                              command=lambda: self.selected_item("delete"))
        buttonSettings = Button(fm, height=1, width=7, text="Settings",
                              command=lambda: self.settings_window(), bg=self.bt_color)
        self.listbox.pack(side=TOP, anchor=W)
        self.textBox.pack(side=TOP, anchor=W)
        buttonCommit.pack(side='left')
        buttonOpen.pack(side='left')
        buttonDelete.pack(side='left')
        buttonSettings.pack(side='left')
        fm.configure(background=self.bg_color)
        x = 1
        for a in note_names:
            self.listbox.insert(x, a.strip())
            x += 1
        fm.pack(fill=BOTH)

    def note_window(self, content, name):
        print(content)
        master = Tk()
        master.withdraw()
        self.newWindow = Toplevel(master)
        self.newWindow.title(name)
        self.newWindow.geometry("250x300")
        self.newWindow.configure(bg=self.bg_color)
        self.newWindow.resizable(False, False)
        self.textBoxN = Text(self.newWindow, height=17, width=30, bg=self.bg_color, wrap=WORD, fg=self.fg_color)
        self.textBoxN.insert(INSERT, content)
        self.textBoxN.pack()
        self.buttonSave = Button(self.newWindow, height=1, width=4, text="Save",
                              command=lambda: self.save_note(name), bg=self.bt_color).pack(side="left")
        self.buttonSavenClose = Button(self.newWindow, height=1, width=10, text="Save&Close",
                              command=lambda: self.save_note(name, 'close'), bg=self.bt_color).pack(side="left")
        self.buttonClose = Button(self.newWindow, height=1, width=5, text="Close",
                              command=lambda: self.newWindow.destroy(), bg=self.bt_color).pack(side="left")
        self.buttonAOT = Button(self.newWindow, height=1, width=11, text="AlwaysOnTop",
                              command=lambda: self.newWindow.attributes('-topmost', True), bg=self.bt_color).pack(side="left")

    def settings_window(self):
        master = Tk()
        master.withdraw()
        self.newWindowS = Toplevel(master)
        self.newWindowS.geometry("200x250")
        self.newWindowS.title("Settings")
        self.newWindowS.configure(bg=self.bg_color)
        self.newWindowS.resizable(False, False)
        Label(self.newWindowS, text="Settings", font=('Aerial 14'), background=self.bg_color).pack(anchor=CENTER)
        Label(self.newWindowS, text="Background color", font=('Aerial 12'), background=self.bg_color).pack()
        self.textBoxBG = Text(self.newWindowS, height=1, width=10, bg=self.bg_color, wrap='none', fg=self.fg_color)
        self.textBoxBG.pack()
        self.textBoxBG.insert(INSERT, self.bg_color)
        Label(self.newWindowS, text="Buttons color", font=('Aerial 12'), background=self.bg_color).pack()
        self.textBoxBT = Text(self.newWindowS, height=1, width=10, bg=self.bg_color, wrap='none', fg=self.fg_color)
        self.textBoxBT.pack()
        self.textBoxBT.insert(INSERT, self.bt_color)
        Label(self.newWindowS, text="Font color", font=('Aerial 12'), background=self.bg_color).pack()
        self.textBoxFG = Text(self.newWindowS, height=1, width=10, bg=self.bg_color, wrap='none', fg=self.fg_color)
        self.textBoxFG.pack()
        self.textBoxFG.insert(INSERT, self.fg_color)
        Label(self.newWindowS, text="Notes app by Ndiyathdanda\nVersion 1.0", font=('Aerial 10'), background=self.bg_color).pack(side='bottom')
        self.buttonSave = Button(self.newWindowS, height=1, width=10, text="Save",
                              command=lambda: self.save_settings(), bg=self.bt_color).pack(side='bottom')

    def save_settings(self):
        inputValueBG = self.textBoxBG.get("1.0", "end-1c")
        inputValueBT = self.textBoxBT.get("1.0", "end-1c")
        inputValueFG = self.textBoxFG.get("1.0", "end-1c")
        modules.save_settings(inputValueBG, inputValueBT, inputValueFG)

    def save_note(self, name, context=None):
        inputValue = self.textBoxN.get("1.0", "end-1c")
        modules.save_note(name, inputValue)
        if context == "close":
            self.newWindow.destroy()
            self.refresh_listbox()
        self.refresh_listbox()

    def retrieve_input(self):
        inputValue = self.textBox.get("1.0", "end-1c")
        modules.add_note(inputValue)
        self.refresh_listbox()

    def selected_item(self, context=None):
        for i in self.listbox.curselection():
            content = modules.open(self.listbox.get(i))
            name = self.listbox.get(i)
            self.refresh_listbox()
        if context == "delete":
            modules.delete_note(name)
            self.refresh_listbox()
            return
        self.note_window(content, name)
        self.refresh_listbox()

    def refresh_listbox(self):
        note_names = modules.get_note_list()
        self.listbox.delete(0, END)
        x = 1
        for a in note_names:
            self.listbox.insert(x, a.strip())
            x += 1

root = Tk()
root.option_add('*font', ('sans', 12))
root.title("NNOTES DEV")
root.geometry("250x370")
display = app(root)
root.resizable(False,False)
root.configure(background='black')
root.mainloop()