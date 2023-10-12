import tkinter as tk
from math import *

btn_params = {'padx': 62, 'pady': 1, 'bd': 4, 'fg': 'white', 'bg': 'black', 'font': ('arial', 18),
              'width': 2, 'height': 2, 'relief': 'flat', 'activebackground': "black"}

class Calculator:
    def __init__(self, master):

        self.expression = ""
        self.recall = ""
        self.sum_up = ""
        self.text_input = tk.StringVar()
        self.master = master

        top_frame = tk.Frame(master, width=660, height=10, bd=2, relief='flat', bg='grey')
        top_frame.pack(side=tk.TOP)

        bottom_frame = tk.Frame(
            master, width=660, height=500, bd=2, relief='flat', bg='black')
        bottom_frame.pack(side=tk.BOTTOM)
        txt_display = tk.Entry(top_frame, font=('arial', 36), relief='flat', bg='black', fg='white', textvariable=self.text_input, width=40, bd=12, justify='right')
        txt_display.pack()

        self.btn_left_brack = tk.Button(
            bottom_frame, **btn_params, text="(", border=1, command=lambda: self.btn_click('('))
        self.btn_left_brack.grid(row=0, column=0)
        self.btn_right_brack = tk.Button(
            bottom_frame, **btn_params, text=")", command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=0, column=1)
        self.btn_clear = tk.Button(
            bottom_frame, **btn_params, text="AC", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=2)
        self.btn_del = tk.Button(
            bottom_frame, **btn_params, text="DEL", command=self.btn_clear1)
        self.btn_del.grid(row=0, column=3)
        self.btn_7 = tk.Button(bottom_frame, **btn_params, text="7", command=lambda: self.btn_click(7))
        self.btn_7.configure(activebackground="black", bg='black')
        self.btn_7.grid(row=1, column=0, columnspan=1)
        self.btn_8 = tk.Button(bottom_frame, **btn_params, text="8", command=lambda: self.btn_click(8))
        self.btn_8.configure(activebackground="black", bg='black')
        self.btn_8.grid(row=1, column=1, columnspan=1)
        self.btn_9 = tk.Button(bottom_frame, **btn_params, text="9", command=lambda: self.btn_click(9))
        self.btn_9.configure(activebackground="black", bg='black')
        self.btn_9.grid(row=1, column=2, columnspan=1)
        self.btn_mult = tk.Button(bottom_frame, **btn_params, text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=1, column=3, columnspan=1)
        self.btn_4 = tk.Button(bottom_frame, **btn_params, text="4", command=lambda: self.btn_click(4))
        self.btn_4.configure(activebackground="black", bg='black')
        self.btn_4.grid(row=2, column=0, columnspan=1)
        self.btn_5 = tk.Button(bottom_frame, **btn_params, text="5", command=lambda: self.btn_click(5))
        self.btn_5.configure(activebackground="black", bg='black')
        self.btn_5.grid(row=2, column=1, columnspan=1)
        self.btn_6 = tk.Button(bottom_frame, **btn_params, text="6", command=lambda: self.btn_click(6))
        self.btn_6.configure(activebackground="black", bg='black')
        self.btn_6.grid(row=2, column=2, columnspan=1)
        self.btnSub = tk.Button(bottom_frame, **btn_params, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=2, column=3, columnspan=1)
        self.btn_1 = tk.Button(bottom_frame, **btn_params, text="1", command=lambda: self.btn_click(1))
        self.btn_1.configure(activebackground="black", bg='black')
        self.btn_1.grid(row=3, column=0, columnspan=1)
        self.btn_2 = tk.Button(bottom_frame, **btn_params, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure(activebackground="black", bg='black')
        self.btn_2.grid(row=3, column=1, columnspan=1)
        self.btn_3 = tk.Button(bottom_frame, **btn_params, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure(activebackground="black", bg='black')
        self.btn_3.grid(row=3, column=2, columnspan=1)
        self.btn_add = tk.Button(
            bottom_frame, **btn_params, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=3, columnspan=1)
        self.btn_0 = tk.Button(bottom_frame, **btn_params, text="0", command=lambda: self.btn_click(0))
        self.btn_0.configure(activebackground="black", bg='black')
        self.btn_0.grid(row=4, column=0)
        self.btn_dec = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=1)
        self.btn_eq = tk.Button(bottom_frame, **btn_params, text="=", command=self.btn_equal)
        self.btn_eq.configure(bg='Red', activebackground='#009999')
        self.btn_eq.grid(row=4, column=2)
        self.btn_div = tk.Button(
            bottom_frame, **btn_params, text="/", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=4, column=3)

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)

    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        try:
            self.sum_up = str(eval(self.expression))
            self.text_input.set(self.sum_up)
            self.expression = self.sum_up
        except Exception as e:
            self.text_input.set("Error")

root = tk.Tk()
b = Calculator(root)
root.geometry("660x480+50+50")
root.resizable(False, False)
root.title("Basic Calculator!")

root.mainloop()
