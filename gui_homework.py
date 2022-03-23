import tkinter
import tkinter.messagebox


class PizzaGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame3.configure(background="light blue")
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame5.configure(background="light blue")
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame7.configure(background="light blue")
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)
        self.frame9.configure(background="light blue")
        self.frame10 = tkinter.Frame(self.main_window)
        self.frame10.configure(background="light blue")
        self.frame11 = tkinter.Frame(self.main_window)
        self.frame12 = tkinter.Frame(self.main_window)
        self.main_window.title("Pizza Price Calculator")
        self.main_window.configure(background="light gray")
        self.main_window.geometry("900x500")

        self.business = tkinter.Label(self.frame1, text="Josh's Pizza")
        self.business.configure(background="light blue", font="Arial")

        self.blank = tkinter.Label(self.frame2, text="\n")
        self.blank.configure(background="light gray")

        self.customer = tkinter.Label(self.frame3, text="Enter Customer Name:")
        self.customer.configure(background="light blue")
        self.cus_name = tkinter.Entry(self.frame3, width=10)

        self.customer.pack(side="left")
        self.cus_name.pack(side="right")

        self.blank2 = tkinter.Label(self.frame4, text="\n")
        self.blank2.configure(background="light gray")

        self.size = tkinter.Label(self.frame5, text="Size: ")
        self.size.configure(background="light blue")

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(6)

        self.size1 = tkinter.Radiobutton(
            self.frame5, text="Small ($6.00)", variable=self.radio_var, value=6.00
        )
        self.size1.configure(background="light blue")
        self.size2 = tkinter.Radiobutton(
            self.frame5, text="Medium ($8.00)", variable=self.radio_var, value=8.00
        )
        self.size2.configure(background="light blue")
        self.size3 = tkinter.Radiobutton(
            self.frame5, text="Large ($10.00)", variable=self.radio_var, value=10.00
        )
        self.size3.configure(background="light blue")

        self.size1.select()

        self.business.pack()
        self.blank.pack()
        self.blank2.pack()
        self.size.pack()
        self.size1.pack()
        self.size2.pack()
        self.size3.pack()

        self.blank3 = tkinter.Label(self.frame6, text="\n")
        self.blank3.configure(background="light gray")

        self.radio_var2 = tkinter.IntVar()
        self.radio_var2.set(0)

        self.crust = tkinter.Label(self.frame7, text="Crust: ")
        self.crust.configure(background="light blue")

        self.crust1 = tkinter.Radiobutton(
            self.frame7, text="Regular", variable=self.radio_var2, value=0
        )
        self.crust1.configure(background="light blue")
        self.crust2 = tkinter.Radiobutton(
            self.frame7, text="Thin (+$1.00)", variable=self.radio_var2, value=1
        )
        self.crust2.configure(background="light blue")
        self.crust3 = tkinter.Radiobutton(
            self.frame7, text="Stuffed (+$2.00)", variable=self.radio_var2, value=2
        )
        self.crust3.configure(background="light blue")

        self.crust1.select()

        self.blank3.pack()
        self.crust.pack()
        self.crust1.pack()
        self.crust2.pack()
        self.crust3.pack()

        self.blank4 = tkinter.Label(self.frame8, text="\n")
        self.blank4.configure(background="light gray")

        self.toppings = tkinter.Label(self.frame9, text="Toppings: ")
        self.toppings.configure(background="light blue")

        self.blank4.pack()
        self.toppings.pack()

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.frame10,
            text="Pepperoni",
            variable=self.cb_var1,
        )
        self.cb1.configure(background="light blue")
        self.cb2 = tkinter.Checkbutton(
            self.frame10,
            text="Tomatoes (+$0.25)",
            variable=self.cb_var2,
        )
        self.cb2.configure(background="light blue")
        self.cb3 = tkinter.Checkbutton(
            self.frame10,
            text="Pineapple (+$0.50)",
            variable=self.cb_var3,
        )
        self.cb3.configure(background="light blue")
        self.cb4 = tkinter.Checkbutton(
            self.frame10,
            text="Mushrooms (+$0.75)",
            variable=self.cb_var4,
        )
        self.cb4.configure(background="light blue")
        self.cb5 = tkinter.Checkbutton(
            self.frame10,
            text="Peppers (+$1.00)",
            variable=self.cb_var5,
        )
        self.cb5.configure(background="light blue")

        self.cb1.pack(side="left")
        self.cb2.pack(side="left")
        self.cb3.pack(side="left")
        self.cb4.pack(side="left")
        self.cb5.pack(side="left")

        self.frame1.pack(side="top")
        self.frame2.pack(side="top")
        self.frame3.pack(side="top")
        self.frame4.pack(side="top")
        self.frame5.pack(side="top")
        self.frame6.pack(side="top")
        self.frame7.pack(side="top")
        self.frame8.pack(side="top")
        self.frame9.pack(side="top")
        self.frame10.pack(side="top")
        self.frame11.pack(side="top")
        self.frame12.pack(side="top")

        self.calc_button = tkinter.Button(
            self.main_window, text="Calculate Price", command=self.price
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def price(self):
        print_name = self.cus_name.get()

        self.cb_values = 0

        if self.cb_var2.get() == 1:
            self.cb_values += 0.25

        if self.cb_var3.get() == 1:
            self.cb_values += 0.50

        if self.cb_var4.get() == 1:
            self.cb_values += 0.75

        if self.cb_var5.get() == 1:
            self.cb_values += 1.00

        total_price = float(self.radio_var.get()) + float(
            self.radio_var2.get() + float(self.cb_values)
        )

        tkinter.messagebox.showinfo(
            "Price", "Customer: " + print_name + "\n" + "Total: $" + str(total_price)
        )


pizza_cost = PizzaGUI()
