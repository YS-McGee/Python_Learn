import tkinter as tk

window = tk.Tk()
window.title("GUI Program")
window.minsize(width=400, height=300)
window.config(padx=100, pady=200)

# Label
label = tk.Label(text="New Label", font=("Arial", 24, "bold"))
# label.pack()
# label.place(x=0, y=0)
label.grid(row=0, column=0, padx=20, pady=20)

# Btn
def btn_clicked():
    # label.config(text="Btn Clicked")
    # label["text"] = "Btn Clicked"
        # The same
    usr_input = input.get()
    label.config(text=usr_input)
btn = tk.Button(text="Button", command=btn_clicked)
# btn.pack()
btn.grid(row=1, column=1)
new_btn = tk.Button(text="New \nButton")
new_btn.grid(row=0, column=2)

# Entry
input = tk.Entry()
# input.pack()
input.grid(row=2, column=3)


window.mainloop()