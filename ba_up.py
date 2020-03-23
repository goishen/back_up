#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:21:22 2020

@author: zunus
"""


import tkinter as tk
from tkinter import ttk
import os
#import datetime
import tkinter.font as font
from datetime import date
import tarfile
from tkinter import filedialog

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Deploy or retrieve a backup")

        # Frames that are inside of MainWindow
        
        self.input_frame = ttk.Frame(self, borderwidth=(5) ,cursor="hand2", height="400")
        self.input_frame.grid(row=0, column=0)

        
        #  These are buttons inside of the input_frame
        
        dep_bck_button = ttk.Button(self.input_frame, text="Deploy a backup", command=self.Deploy)
        ret_bck_button = ttk.Button(self.input_frame, text="Retrieve a backup", command=self.Retrieve)
        dep_bck_button.grid(row=1, column= 0, padx=10, pady=(5,5))
        ret_bck_button.grid(row=2, column=0, padx=10, pady=(5,5))
        quit_button = ttk.Button(self.input_frame, text="Quit", command=self.destroy)
        quit_button.grid(row=3, column=0, padx=5, pady=(5,5))
        
        
    def Deploy(self):
        self.dir = os.chdir(filedialog.askdirectory(initialdir='.', title="Select a directory"))

        self.files = os.listdir('.')
        self.today = date.today() 
        with tarfile.open(f"{self.today}.tar.gz", mode="w:gz") as tar:
            for i in self.files: 
               # print("Tarred and zip : ", i)
                tar.add(i)               
            taf_label = ttk.Label(self, text=f"Tarred and and zipped : {i}")
            taf_label.grid(row=2, column=0)
                       

    def Retrieve(self):
        #os.chdir("/home/zunus/Pictures")
        self.files_selected = filedialog.askopenfilename(initialdir='.', title="Select a file", filetypes=(("tar.gz files", "*.tar.gz"),))
        if tarfile.is_tarfile(self.files_selected) == True:  # doesn't appear to be needed
            new_file = tarfile.open(f"{self.files_selected}")
            new_file.extractall()
            new_file.close()
            dec_label = ttk.Label(self.input_frame, text=f"Decompressing : {self.files_selected}")
            dec_label.grid()
        else: 
            pass
        
       
root = MainWindow()
font.nametofont("TkDefaultFont").configure(size=12)
root.mainloop()

