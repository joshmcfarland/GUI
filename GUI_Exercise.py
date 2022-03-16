from audioop import avg
from cgitb import text
from struct import pack
import tkinter
import tkinter.messagebox


class AvgScoreGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.configure(background="green")
        self.top_mid_frame = tkinter.Frame(self.main_window)
        self.top_mid_frame.configure(background="green")
        self.mid_frame = tkinter.Frame(self.main_window)
        self.mid_frame.configure(background="green")
        self.mid_bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.main_window.title("GUI Exercise Demo")
        self.main_window.configure(background="green")
        self.main_window.geometry("600x300")

        self.test1 = tkinter.Label(self.top_frame, text="Enter the score for test 1:")
        self.test2 = tkinter.Label(
            self.top_mid_frame, text="Enter the score for test 2:"
        )
        self.test3 = tkinter.Label(self.mid_frame, text="Enter the score for test 3:")
        self.score1 = tkinter.Entry(self.top_frame, width=5)
        self.score2 = tkinter.Entry(self.top_mid_frame, width=5)
        self.score3 = tkinter.Entry(self.mid_frame, width=5)

        self.test1.pack(side="left")
        self.test2.pack(side="left")
        self.test3.pack(side="left")
        self.score1.pack(side="right")
        self.score2.pack(side="right")
        self.score3.pack(side="right")

        self.average = tkinter.Label(self.mid_bottom_frame, text="Average: ")
        self.avg_score_var = tkinter.StringVar()
        self.avg_score_label = tkinter.Label(
            self.mid_bottom_frame, textvariable=self.avg_score_var
        )

        self.average.pack(side="left")
        self.avg_score_label.pack(side="right")

        self.top_frame.pack(side="top")
        self.top_mid_frame.pack(side="top")
        self.mid_frame.pack(side="top")
        self.mid_bottom_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.calc_button = tkinter.Button(
            self.main_window, text="Average", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def convert(self):
        ts1 = float(self.score1.get())
        ts2 = float(self.score2.get())
        ts3 = float(self.score3.get())

        avg_score = round((ts1 + ts2 + ts3) / 3, 2)

        self.avg_score_var.set(avg_score)


avg_score_conv = AvgScoreGUI()
