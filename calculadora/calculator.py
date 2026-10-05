import tkinter as tk

class interface:
    def __init__(self):
        self.expr = ""

        self.root = tk.Tk()
        self.root.configure(bg="light green")
        self.root.title("Simple Calculator")
        self.root.geometry("270x150")

        self.display = tk.StringVar()

    def press(self, key):
        self.expr += str(key)
        self.display.set(self.expr)

    def equal(self):
        try:
            result = str(eval(self.expr))
            self.display.set(result)
            self.expr = ""
        except:
            self.display.set("error")
            self.expr = ""

    def clear(self):
        self.expr = ""
        self.display.set(self.expr)

    def run(self):
        
        entry = tk.Entry(self.root, textvariable=self.display)
        entry.grid(columnspan=4, ipadx=70)

        btn1 = tk.Button(self.root, text='1', fg='black', bg='red', command=lambda: self.press(1), height=1, width=7)
        btn1.grid(row=2, column=0)
        btn2 = tk.Button(self.root, text='2', fg='black', bg='red', command=lambda: self.press(2), height=1, width=7)
        btn2.grid(row=2, column=1)
        btn3 = tk.Button(self.root, text='3', fg='black', bg='red', command=lambda: self.press(3), height=1, width=7)
        btn3.grid(row=2, column=2)
        btn4 = tk.Button(self.root, text='4', fg='black', bg='red', command=lambda: self.press(4), height=1, width=7)
        btn4.grid(row=3, column=0)
        btn5 = tk.Button(self.root, text='5', fg='black', bg='red', command=lambda: self.press(5), height=1, width=7)
        btn5.grid(row=3, column=1)
        btn6 = tk.Button(self.root, text='6', fg='black', bg='red', command=lambda: self.press(6), height=1, width=7)
        btn6.grid(row=3, column=2)
        btn7 = tk.Button(self.root, text='7', fg='black', bg='red', command=lambda: self.press(7), height=1, width=7)
        btn7.grid(row=4, column=0)
        btn8 = tk.Button(self.root, text='8', fg='black', bg='red', command=lambda: self.press(8), height=1, width=7)
        btn8.grid(row=4, column=1)
        btn9 = tk.Button(self.root, text='9', fg='black', bg='red', command=lambda: self.press(9), height=1, width=7)
        btn9.grid(row=4, column=2)
        btn0 = tk.Button(self.root, text='0', fg='black', bg='red', command=lambda: self.press(0), height=1, width=7)
        btn0.grid(row=5, column=0)

        plus = tk.Button(self.root, text="+", fg='black', bg='red', command=lambda:self.press('+'), height=1, width=7)
        plus.grid(row=2, column=3)
        minus = tk.Button(self.root, text="-", fg='black', bg='red', command=lambda:self.press('-'), height=1, width=7)
        minus.grid(row=3, column=3)
        mult = tk.Button(self.root, text="*", fg='black', bg='red', command=lambda:self.press('*'), height=1, width=7)
        mult.grid(row=4, column=3)
        div = tk.Button(self.root, text="/", fg='black', bg='red', command=lambda:self.press('/'), height=1, width=7)
        div.grid(row=5, column=3)

        eq = tk.Button(self.root, text='=', fg='black', bg='red', command=self.equal, height=1, width=7)
        eq.grid(row=5, column=2)
        clr = tk.Button(self.root, text='Clear', fg='black', bg='red', command=self.clear, height=1, width=7)
        clr.grid(row=5, column=1)
        dot = tk.Button(self.root, text='.', fg='black', bg='red', command=lambda: self.press('.'), height=1, width=7)
        dot.grid(row=6, column=0)

        self.root.mainloop()

if __name__=="__main__":
    interface().run()