import tkinter as tk

window = tk.Tk()
window.minsize(width=220, height=80)
window.config(padx=10, pady=20)
window.title("Mile to Km Converter")

input = tk.Entry(width=10)
input.grid(row=0, column=1)

l = tk.Label(text="Miles")
l.grid(row=0, column=2)
# ----------------------------------------------------
l_is_equal_to = tk.Label(text="is equal to")
l_is_equal_to.grid(row=1, column=0)

l_0 = tk.Label(text="0")
l_0.grid(row=1, column=1)

l_km = tk.Label(text="Km")
l_km.grid(row=1, column=2)
# ----------------------------------------------------
def calculate():
    mile = float(input.get())
    km = mile * 1.61
    l_0.config(text=km)

btn = tk.Button(text="Calculate", command=calculate)
btn.grid(row=2, column=1)



window.mainloop()