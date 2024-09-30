import tkinter as tk
from Hover2ClickButton import Hover2ClickButton, blinkdecorator

# Inherit Hover2ClickButton and override click_function.
class UpButton(Hover2ClickButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        global text_var

        text_var.set(int(text_var.get()) + 1)

        return

root = tk.Tk()
root.title(f'Hover2Click Demo')

text_var = tk.StringVar()
text_var.set('0')

label = tk.Label(root, textvariable = text_var)
label.pack(pady = 10)

# Create instance and pack.
button = UpButton(root, text = 'Increase')
button.pack(pady = 10)

# Bind events and set stay time.
button.bind_event()
button.set_stay_time(1.25) # If you hover your cursor on the button for this secs, click_function would be called.

root.mainloop()