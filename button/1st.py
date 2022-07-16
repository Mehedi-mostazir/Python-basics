import tkinter as tk
a=tk.Tk()

b=tk.Button(a,text='hello',fg='red')
b.pack(side='left')
b.place(x=10,y=10)
b.grid(row=0,column=0)

d=tk.Button(a,text='Shoroni',fg='red')
d.pack(side='left')
d.place(x=10,y=10)
d.grid(row=0,column=0)

c=tk.Button(a,text='hi',fg='green')
#c.pack(side='right')
b.grid(row=0,column=1)
d.grid(row=0,column=1)

a.mainloop()
