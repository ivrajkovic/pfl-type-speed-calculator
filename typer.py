import tkinter as tk
import random
import time


class Typer:
    def __init__(self, text):
        self.words_list = text.split(' ')
        self.current_position = 0
        self.current_word = self.words_list[self.current_position]
        self.words_bounds = [(10, 10)]
        self.total_characters = 0
        self.time_start = 0
        self.time_end = 0
        self.canvas = None
        self.input = None

    def set_widgets(self, canvas, user_input):
        self.canvas = canvas
        self.input = user_input

    def next_word(self):
        self.current_position += 1
        if self.current_position < len(self.words_list):
            self.current_word = self.words_list[self.current_position]
        else:
            self.current_word = ''
            self.timer_end()
            t = round(self.time_end-self.time_start, 2)
            # Characters Typed in One Minute / 5 = WPM
            w = round((self.total_characters / t * 60) / 5, 2)
            end_text = f"Time: {t}sec, WPM: {w}"
            self.input.config(text=end_text)

    def reset(self):
        random.shuffle(self.words_list)
        self.current_position = 0
        self.current_word = self.words_list[0]
        self.words_bounds = [(10, 10)]
        self.total_characters = 0
        self.time_start = 0
        self.time_end = 0
        self.add_all_words()
        self.input.config(text='')

    def add_all_words(self):
        self.canvas.delete('all')
        x, y = 10, 10  # Initial position on the canvas
        for word in self.words_list:
            # Add word to canvas
            add_text = self.canvas.create_text(x, y, text=word, anchor=tk.NW, fill='black', font="Tahoma 16")
            # Update the x-coordinate for the next word
            bounds = self.canvas.bbox(add_text)
            width = bounds[2] - bounds[0]
            x += width + 10
            # Goto next row to wrap text
            if x >= 300:
                y += 30
                x = 10
            self.words_bounds.append((x, y))
            self.canvas.update()

    def add_one_word(self, color):
        x = self.words_bounds[self.current_position][0]
        y = self.words_bounds[self.current_position][1]
        self.canvas.create_text(x, y, text=self.current_word, anchor=tk.NW, fill=color, font="Tahoma 16")
        self.canvas.update()

    def set_user_input(self, txt):
        self.input.config(text=txt)

    def word_is_correct(self):
        self.total_characters += len(self.current_word) + 1
        self.add_one_word('green')

    def word_is_incorrect(self):
        self.add_one_word('red')

    def timer_start(self):
        self.time_start = time.time()

    def timer_end(self):
        self.time_end = time.time()


