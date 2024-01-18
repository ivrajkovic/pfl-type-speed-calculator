import tkinter as tk
import string
from typer import Typer

# Colors

# Variables
alphabet = list(string.ascii_lowercase)
sample_text = ('damage somehow weak operation knife looking photo guy imagine fate lay '
               'main soldiers fortune truly program cannot ears check murdered heading depends short hoping')


# Keypress event
def keypress(event):
    global typ
    # Allow input only if there are words left
    if typ.current_word != '':
        # Start timer on keypress
        if typ.time_start == 0:
            typ.timer_start()
        txt = input_lbl.cget("text")
        # Only allow alphabet letters
        if event.keysym in alphabet:
            txt += event.keysym
            typ.set_user_input(txt)
        # Delete letter on backspace
        elif event.keysym == 'BackSpace':
            txt = txt[:-1]
            typ.set_user_input(txt)
        elif event.keysym == 'Escape':
            typ.reset()
        # If SPACE is pressed compare words, load next, reset type_lbl
        elif event.keysym == 'space':
            if txt == typ.current_word:
                typ.word_is_correct()
            else:
                typ.word_is_incorrect()
            txt = ''
            typ.set_user_input(txt)
            typ.next_word()


# Window init
window = tk.Tk()
window.title("Type Speed Test")
window.config(padx=30, pady=30, bg='white')
window.bind("<Key>", keypress)
typ = Typer(sample_text)

# Labels
title_lbl = tk.Label(window, text="Test your typing speed", font=("Arial", 20), bg='white', fg='black', pady=10)
input_lbl = tk.Label(window, text='', font=("Arial", 16), bg='white', fg='red', pady=20)

# Canvas
words_canvas = tk.Canvas(window, width=400, height=200, highlightthickness=0, bg='white')
typ.set_widgets(words_canvas, input_lbl)

# Buttons
reset_btn = tk.Button(window, text="Reset", font=("Arial", 16), command=typ.reset)
exit_btn = tk.Button(window, text="Exit", font=("Arial", 16), command=exit)

# Grid
title_lbl.grid(row=0, column=0, columnspan=2)
words_canvas.grid(row=1, column=0, columnspan=2)
input_lbl.grid(row=2, column=0, columnspan=2)
reset_btn.grid(row=3, column=0)
exit_btn.grid(row=3, column=1)

# Init words on canvas
typ.add_all_words()

# Stay on screen
window.mainloop()
