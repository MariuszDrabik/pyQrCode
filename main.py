import qrcode
from random import randint
import tkinter as tk

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/c/Codemycom')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

number = randint(250, 550) + randint(250, 550) + randint(250, 550)

print(number)
img.save("qr_code.png")


class MainProgram(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.font = ('helvetica', 12, 'bold')
        self.master = master
        self.create_widgets()
        self.layout()

    def create_widgets(self):
        self.data_to_code = tk.Entry(self.master, text="Import JSON")
        self.info_panel = tk.Label(self.master, text="")
        self.save_JSON = tk.Button(self.master, text="Save Exel", command="")
        self.quit = tk.Button(self.master, text="QUIT", 
                              command=self.master.destroy)

    def layout(self):
        self.master.geometry('400x210')
        self.master.config(bg='white')
        self.data_to_code.config(bg='#777', fg='white', relief='flat',
                                    font=self.font)
        self.save_JSON.config(bg='#777', fg='white', relief='flat',
                              width=15, height=1, font=self.font)
        self.quit.config(bg='#777', fg='white', relief='flat', width=15,
                         height=1, font=self.font)
        self.info_panel.config(bg='white', fg='#777', relief='flat', width=25,
                               height=1, font=self.font)
        self.data_to_code.grid(column=0, row=0, ipady=10)
        self.info_panel.grid(column=0, row=2, columnspan=2)
        self.save_JSON.grid(column=0, row=3)
        self.quit.grid(column=0, row=4,)
        self.master.grid()
        for widget in self.master.winfo_children():
            widget.grid(padx=10, pady=10,)


root = tk.Tk()
myapp = MainProgram(root)
myapp.mainloop()