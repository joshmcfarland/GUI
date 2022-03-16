from cgitb import text
from struct import pack
import tkinter
import tkinter.messagebox


class RadioButtonGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.main_window.title("Radio Buttons Demo")

        self.radio_var = tkinter.IntVar()

        # set the IntVar object to 1
        self.radio_var.set(10)

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Option1", variable=self.radio_var, value=10
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Option2", variable=self.radio_var, value=20
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="Option3", variable=self.radio_var, value=30
        )

        self.rb1.select()

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.ok_button = tkinter.Button(
            self.bottom_frame, text="Ok", command=self.show_choice
        )

        self.reset_button = tkinter.Button(
            self.bottom_frame, text="Reset", command=self.rb1.select
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.ok_button.pack(side="left")
        self.reset_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "You have selected option " + str(self.radio_var.get())
        )


radio_button = RadioButtonGUI()
