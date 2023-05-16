import customtkinter as ck
import tkinter as tk
import calendar


class Calender(ck.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calender")
        self.resizable(False, False)
        ck.set_appearance_mode("dark")
        ck.set_default_color_theme("green")

        self.frame_text = ck.CTkFrame(self)
        self.frame_text.grid(row=0, column=0, padx=50, pady=10)

        self.label = ck.CTkLabel(self.frame_text, text="SIMPLE CALENDAR APP", font=("Arial", 50), anchor="center")
        self.label.grid(row=0, column=0, padx=30)

        self.frame = ck.CTkFrame(self)
        self.frame.grid(row=1)

        self.label1 = ck.CTkLabel(self.frame, text="Month")
        self.label1.grid(row=0, column=0, pady=15, padx=15)

        self.month = tk.Spinbox(self.frame, from_=1, to=12, width=8, font=("Arial", 20))
        self.month.grid(row=0, column=1, pady=15, padx=15)

        self.label2 = ck.CTkLabel(self.frame, text="Year")
        self.label2.grid(row=0, column=2, pady=15, padx=15)

        self.year = tk.Spinbox(self.frame, from_=2000, to=3000, width=8, font=("Arial", 20))
        self.year.grid(row=0, column=3, pady=15, padx=15)

        self.text_box = tk.Text(self, width=45, height=17)
        self.text_box.grid(row=2, pady=15)

        self.search = ck.CTkButton(self, text="Search", command=self.calc, width=350, height=50, font=("Arial", 25))
        self.search.grid(row=3, pady=15)

        self.clear = ck.CTkButton(self, text="Clear", command=self.clear, width=350, height=50, font=("Arial", 25))
        self.clear.grid(row=4, pady=15)

    def calc(self):
        month = self.month.get()
        year = self.year.get()
        cal = calendar.month(theyear = int(year), themonth = int(month), w=5, l=2)
        self.text_box.delete(1.0, 'end')
        self.text_box.insert('end', cal)

    def clear(self):
        self.text_box.delete(1.0, 'end')


def main():
    App = Calender()
    App.mainloop()


if __name__ == "__main__":
    main()
