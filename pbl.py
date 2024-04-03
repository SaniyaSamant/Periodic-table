symbols = ['H', 'Li', 'Be', 'Na', 'Mg', 'K', 'Ca', 'Rb', 'Sr', 'Cs', 'Ba', 'Fr', 'Ra']
keywords = ['name', 'index', 'elementkategorie', 'gruppe', 'periode', 'block',
            'atommasse', 'aggregatzustand', 'dichte', 'elektronegativität']

values = [['Hydrogen', 1, 'Nichtmetalle', 1, 1, 's', 1.01, 'gasförmig', 0.08, 2.2],  # H
          ['Lithium', 3, 'Alkalimetalle', 1, 2, 's', 6.94, 'fest', 0.53, 0.98],  # Li
          ['Beryllium', 4, 'Erdalkalimetalle', 2, 2, 's', 9.01, 'fest', 1.84, 1.57],  # Be
          ['Sodium', 11, 'Alkalimetalle', 1, 3, 's', 22.99, 'fest', 0.97, 0.93],  # Na
          ['Magnesium', 12, 'Erdalkalimetalle', 2, 3, 's', 24.31, 'fest', 1.74, 1.31],  # Mg
          ['potassium', 19, 'Alkalimetalle', 1, 4, 's', 39.09, 'fest', 0.86, 0.82],  # K
          ['Calcium', 20, 'Erdalkalimetalle', 2, 4, 's', 40.08, 'fest', 1.55, 1.00],  # Ca
          ['Rubidium', 37, 'Alkalimetalle', 1, 5, 's', 85.47, 'fest', 1.53, 0.82],  # Rb
          ['Strontium', 38, 'Erdalkalimetalle', 2, 5, 's', 87.62, 'fest', 2.63, 0.95],  # Sr
          ['Caesium', 55, 'Alkalimetalle', 1, 6, 's', 132.91, 'fest', 1.90, 0.79],  # Cs
          ['Barium', 56, 'Erdalkalimetalle', 2, 6, 's', 137.33, 'fest', 3.62, 0.89],  # Ba
          ['Francium', 87, 'Alkalimetalle', 1, 7, 's', 223.02, 'fest', 'n.A', 0.7],  # Fr
          ['Radium', 88, 'Erdalkalimetalle', 2, 7, 's', 226.03, 'fest', 5.5, 0.9],  # Ra
          ]
kategorie_farben = {'Alkalimetalle': '#fe6f61',
                    'Erdalkalimetalle': '#6791a7',
                    'Nichtmetalle': '#ffde66',
                    }

import tkinter as tk

root = tk.Tk()


class Element(tk.Frame):
    la_offset = 2;
    ac_offset = 2;
    offset = 2

    def __init__(self, master, symbol, **kwargs):
        tk.Frame.__init__(self, master,
                          relief='raised')
        self.kwargs = kwargs
        self.command = kwargs.pop('command', lambda: print('No command'))
        self.WIDTH, self.HEIGHT, self.BD = 100, 100, 3
        self.CMP = self.BD * 2
        bg = kategorie_farben.get(kwargs.get('elementkategorie'))
        self.configure(width=self.WIDTH, height=self.HEIGHT, bd=self.BD,
                       bg=bg)
        self.grid_propagate(0)
        self.idx = tk.Label(self, text=kwargs.get('index'), bg=bg)
        self.u = tk.Label(self, text=kwargs.get('atommasse'), bg=bg)

        self.name = tk.Label(self, text=kwargs.get('name'), bg=bg)
        self.symb = tk.Label(self, text=symbol, font=('bold'), fg=self.get_fg(), bg=bg)

        self.e = tk.Label(self, text=kwargs.get('elektronegativität'), bg=bg)
        self.d = tk.Label(self, text=kwargs.get('dichte'), bg=bg)

        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=2)

        self.idx.grid(row=0, column=0, sticky='w')
        self.u.grid(row=0, column=2, sticky='e')

        mid_x = self.WIDTH / 2 - self.name.winfo_reqwidth() / 2
        mid_y = self.HEIGHT / 2 - self.name.winfo_reqheight() / 2
        offset = 15
        self.name.place(in_=self, x=mid_x - self.CMP, y=mid_y - self.CMP + offset)

        mid_x = self.WIDTH / 2 - self.symb.winfo_reqwidth() / 2
        mid_y = self.HEIGHT / 2 - self.symb.winfo_reqheight() / 2
        self.symb.place(in_=self, x=mid_x - self.CMP, y=mid_y - self.CMP - offset / 2)

        self.e.grid(row=2, column=0, sticky='w')
        self.d.grid(row=2, column=2, sticky='e')

        r, c = kwargs.pop('periode'), kwargs.pop('gruppe')

        self.grid(row=r, column=c, sticky='nswe')
        self.bind('<Enter>', self.in_active)
        self.bind('<Leave>', self.in_active)
        self.bind('<ButtonPress-1>', self.indicate)
        self.bind('<ButtonRelease-1>', self.execute)
        [child.bind('<ButtonPress-1>', self.indicate) for child in self.winfo_children()]
        [child.bind('<ButtonRelease-1>', self.execute) for child in self.winfo_children()]

    def in_active(self, event):
        if str(event.type) == 'Enter': self.flag = True
        if str(event.type) == 'Leave':
            self.flag = False;
            self.configure(relief='raised')

    def indicate(self, event):
        self.configure(relief='sunken')

    def execute(self, event):
        if self.flag:
            self.command();self.configure(relief='raised')
        else:
            self.configure(relief='raised')

    def get_fg(self):
        if self.kwargs.get('aggregatzustand') == 'fest': return 'black'
        if self.kwargs.get('aggregatzustand') == 'flüssig': return 'blue'
        if self.kwargs.get('aggregatzustand') == 'gasförmig': return 'red'
        if self.kwargs.get('aggregatzustand') == 'n.A': return 'grey'


def test():
    print('testing..')


for idx, symbol in enumerate(symbols):
    kwargs = {}
    for k, v in zip(keywords, values[idx]):
        kwargs.update({k: v})
    Element(root, symbol, command=test, **kwargs)
root.mainloop()
