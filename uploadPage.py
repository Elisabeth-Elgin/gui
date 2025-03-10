﻿
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fuzhe\OneDrive\Desktop\cs hw\gui\assets\frame1")

class UploadPage():
    def __init__(self, root):
            self.root = root

            #self.canvas = Canvas(self.root, height = 1000, width = 600, bg = "#FF8000")
            #self.canvas.pack(fill = "both", expand = False)

            self.fillWindow()

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def fillWindow(self):

        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 1041,
            width = 1455,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            1.0,
            235.0,
            1042.0,
            fill="#79BCF7",
            outline="")

        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=250.0,
            y=25.0,
            width=1177.0,
            height=211.0
        )

        canvas.create_text(
            481.0,
            299.0,
            anchor="nw",
            text="File name",
            fill="#094478",
            font=("Roboto Black", 20 * -1)
        )

        canvas.create_text(
            481.0,
            452.0,
            anchor="nw",
            text="File name",
            fill="#094478",
            font=("Roboto Black", 20 * -1)
        )

        canvas.create_text(
            482.0,
            615.0,
            anchor="nw",
            text="File name",
            fill="#094478",
            font=("Roboto Black", 20 * -1)
        )

        image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            372.0,
            322.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            372.0,
            467.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            372.0,
            633.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            1239.0,
            317.0,
            image=image_image_5
        )
        window.resizable(False, False)
        window.mainloop()
