import tkinter as tk
from tkinter import *

root = tk.Tk()

#root.overrideredirect(True)
root.config(bg='#21232c')
root.wait_visibility(root)
root.wm_attributes("-alpha", 0.5)
root.geometry("250x250")

#win = Frame(root, height=250, width=250, color='#21232c').pack()

Label(root, text="Hello", fg='white', 
        bg='#21232c').pack(fill=BOTH, expand=YES)
but=Button(root, text='Quit', command=root.quit, 
        bg='#21232c', fg='white')
but.pack(fill=BOTH, expand=YES)

#canvas = tk.Canvas(root, width=300, height=300)
#canvas.pack()
#canvas.create_rectangle(50, 25, 150, 75, fill="red")

root.mainloop()
