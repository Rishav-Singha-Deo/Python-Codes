import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.entry = tk.Entry(self.master, width=23, font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button("C", lambda: self.clear(), 1, 0)
        self.create_button("CE", lambda: self.clear_entry(), 1, 1)
        self.create_button("/", lambda: self.add_to_input("/"), 1, 2)
        self.create_button("*", lambda: self.add_to_input("*"), 1, 3)
        self.create_button("7", lambda: self.add_to_input("7"), 2, 0)
        self.create_button("8", lambda: self.add_to_input("8"), 2, 1)
        self.create_button("9", lambda: self.add_to_input("9"), 2, 2)
        self.create_button("-", lambda: self.add_to_input("-"), 2, 3)
        self.create_button("4", lambda: self.add_to_input("4"), 3, 0)
        self.create_button("5", lambda: self.add_to_input("5"), 3, 1)
        self.create_button("6", lambda: self.add_to_input("6"), 3, 2)
        self.create_button("+", lambda: self.add_to_input("+"), 3, 3)
        self.create_button("1", lambda: self.add_to_input("1"), 4, 0)
        self.create_button("2", lambda: self.add_to_input("2"), 4, 1)
        self.create_button("3", lambda: self.add_to_input("3"), 4, 2)
        self.create_button("=", lambda: self.calculate(), 4, 3, rowspan=2)
        self.create_button("0", lambda: self.add_to_input("0"), 5, 0, columnspan=2)
        self.create_button(".", lambda: self.add_to_input("."), 5, 2)

    def create_button(self, text, command, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, width=3, height=2, font=("Arial", 20), command=command)
        button.grid(row=row, column=column, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan)

    def clear(self):
        self.entry.delete(0, tk.END)

    def clear_entry(self):
        self.entry.delete(len(self.entry.get())-1, tk.END)

    def add_to_input(self, text):
        self.entry.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()