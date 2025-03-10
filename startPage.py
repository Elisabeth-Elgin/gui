
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fuzhe\OneDrive\Desktop\cs hw\gui\assets\frame2")

class StartPage():

    def __init__(self):
        self.root = root

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

        canvas.create_rectangle(
            918.0,
            1.0,
            1458.0,
            1042.0,
            fill="#DAEBF9",
            outline="")

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=942.0,
            y=36.0,
            width=206.0,
            height=101.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=1224.0,
            y=36.0,
            width=200.0,
            height=112.0
        )

        canvas.create_text(
            1158.0,
            169.0,
            anchor="nw",
            text="Status:",
            fill="#094478",
            font=("Jomolhari Regular", 20 * -1)
        )

        canvas.create_rectangle(
            935.0,
            339.0,
            1435.0,
            818.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            1064.0,
            339.0,
            anchor="nw",
            text="Conflict  Summary：",
            fill="#094478",
            font=("Jomolhari Regular", 20 * -1)
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=1206.0,
            y=737.0,
            width=200.0,
            height=65.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=972.0,
            y=741.0,
            width=200.0,
            height=61.0
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        button_10.place(
            x=942.0,
            y=893.0,
            width=200.0,
            height=101.0
        )

        button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        button_11.place(
            x=1224.0,
            y=893.0,
            width=200.0,
            height=101.0
        )

        canvas.create_text(
            931.0,
            201.0,
            anchor="nw",
            text="status info",
            fill="#000000",
            font=("Jomolhari Regular", 15 * -1)
        )

        canvas.create_rectangle(
            916.9881591796875,
            153.47650146484375,
            1455.0114135742188,
            154.47650146484375,
            fill="#094478",
            outline="")

        canvas.create_rectangle(
            918.0,
            314.0,
            1456.0232543945312,
            315.0,
            fill="#094478",
            outline="")
        window.resizable(False, False)
        window.mainloop()
