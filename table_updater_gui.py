import tkinter as tk
import tkinter.ttk as ttk

class UpdaterGui():
    def __init__(self, master=None):
        # simple GUI created with tkinter and pygubu
        self.pag = tk.Tk() if master is None else tk.Toplevel(master)

        self.pag_title = ttk.Label(self.pag)

        self.pag_title.configure(text='Table Update:')

        self.pag_title.grid(column='1', padx='5', pady='3', row='0')

        self.master_frame = ttk.Frame(self.pag)

        self.frame_data1 = ttk.Frame(self.master_frame)

        self.name_data1 = ttk.Label(self.frame_data1)

        self.name_data1.configure(text=' Data 1:')

        self.name_data1.grid(column='0', row='0', padx='5')

        self.entry_data1 = ttk.Entry(self.frame_data1)

        self.entry_data1.configure(font='TkDefaultFont')

        self.entry_data1.grid(column='1', padx='10', row='0')

        self.frame_data1.grid(column='0', padx='5', pady='5', row='0')

        self.button = ttk.Button(self.master_frame)

        self.button.configure(text='Submit')

        self.button.grid(column='0', columnspan='2', pady='6', row='4')

        self.frame_data2 = ttk.Frame(self.master_frame)

        self.entry_data2 = ttk.Entry(self.frame_data2)

        self.entry_data2.grid(column='1', padx='10', row='0')

        self.name_data2 = ttk.Label(self.frame_data2)

        self.name_data2.configure(text=' Data 2:')

        self.name_data2.grid(column='0', row='0', sticky='e', padx='5')

        self.frame_data2.grid(column='0', padx='5', pady='5', row='1')

        self.frame_data3 = ttk.Frame(self.master_frame)

        self.name_data3 = ttk.Label(self.frame_data3)

        self.name_data3.configure(text=' Data 3:')

        self.name_data3.grid(column='0', row='0', padx='5')

        self.entry_data3 = ttk.Entry(self.frame_data3)

        self.entry_data3.configure(font='TkDefaultFont')

        self.entry_data3.grid(column='1', padx='10', row='0')

        self.frame_data3.grid(column='0', padx='5', pady='5', row='2')

        self.master_frame.configure(height='200', width='200')

        self.master_frame.grid(column='1', row='1')

        self.pag.configure(pady='5', takefocus=False)

        self.pag.resizable(False, False)

        self.pag.title('Updater')

        self.mainwindow = self.pag

    def run(self):
        self.mainwindow.mainloop()
