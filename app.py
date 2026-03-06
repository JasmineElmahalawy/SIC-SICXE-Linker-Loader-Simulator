from tkinter import *
from tkinter import filedialog, messagebox, ttk
from sic import Sic
from sicxe import SicXE

class App:
    def __init__(self, master) -> None:
        self.menu = None
        self.master = master
        label_frame1 = LabelFrame(master, text="LOADER-LINKER APP", font=("Arial", 25, "bold"))
        label_frame1.pack(pady=200, padx=200)
        label_frame1.config(bg="YELLOW", fg="GREEN")
        lb = Label(label_frame1, text="Choose SIC or SIC-XE")
        lb.pack(side=TOP)
        lb.config(bg="YELLOW", fg="BLACK")
        self.radio = StringVar()
        R1 = Radiobutton(label_frame1, text="SIC", variable=self.radio, value="sic", command=self.handleSelect)
        R1.pack(anchor=CENTER)
        R1.config(bg="YELLOW", fg="BLACK")
        R2 = Radiobutton(label_frame1, text="SIC-XE", variable=self.radio, value="sicxe", command=self.handleSelect)
        R2.pack(anchor=CENTER)
        R2.config(bg="YELLOW", fg="BLACK")
        self.label = Label(label_frame1)
        self.label.pack()

    def handleSelect(self):
        selection = self.radio.get()
        print(selection)
        if selection == "sic":
            sic = Sic(self.menu)
        if selection == "sicxe":
            sic_xe = SicXE()
