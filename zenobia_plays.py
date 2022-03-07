import tkinter as tk
from constants import *
from word_object import The_Word_Class
from tkinter import font as font
from WidgetControls import font_return
from game_frame import game_frame_class


class Word_Not_Found_GUI_Class(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('475x150+0+0')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        tk.Label(self, font=font_return(16), text='Either you chose a word not in my dictionary').grid(row=1, column=1)
        tk.Label(self, font=font_return(16), text='or you made a mistake with asigning colors.').grid(
            row=2, column=1)

        tk.Button(self, font=font_return(16), command=self.destroy,
                  text='OK').grid(row=3, column=1)

        self.rowconfigure(4, weight=1)
        self.columnconfigure(2, weight=1)

class zenobia_play_class(game_frame_class):
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)

    def build_frame(self):
        super().build_frame()

        self.nametowidget('top_row').nametowidget(
            'frame_title')['text'] = 'Zenobia Plays'

    
    def remove_letter_labels(self):
        super().remove_letter_labels()

        the_guessing_frame = self.nametowidget('the_guessing_frame')

        for index in range(self.number_of_letters):
            the_guessing_frame.nametowidget(
                'button-green-' + str(index)).destroy()
            the_guessing_frame.nametowidget(
                'button-yellow-' + str(index)).destroy()
            the_guessing_frame.nametowidget(
                'button-gray-' + str(index)).destroy()


    def change_number_letters(self, direction):
        super().change_number_letters(direction)

    def add_guessing_widgets(self, new_number_of_letters):

        super().add_guessing_widgets(new_number_of_letters)

        the_guessing_frame = self.nametowidget('the_guessing_frame')
        for index in range(new_number_of_letters):

            tk.Button(the_guessing_frame, width=3, command=lambda m='lime-' + str(index): self.color_button_pressed(m),  bg=get_color(
                'lime'), height=2, text=' ', name='button-green-' + str(index)).grid(row=3, column=index+1, pady=10, padx=20)
            tk.Button(the_guessing_frame, width=3, command=lambda m='LightGoldenrodYellow-' + str(index): self.color_button_pressed(m), bg=get_color(
                'LightGoldenrodYellow'), height=2, text=' ', name='button-yellow-' + str(index), bd=0).grid(row=4, column=index+1, pady=10, padx=20)
            tk.Button(the_guessing_frame, width=3,  command=lambda m='lightgray-' + str(index): self.color_button_pressed(m), bg=get_color(
                'lightgray'), height=2, text=' ', name='button-gray-' + str(index), bd=0).grid(row=5, column=index+1, pady=10, padx=20)

    def next_guess(self):
        
        super().next_guess()

        if self.number_of_guesses>1:
            self.add_guess_to_scrollable_frame()
            self.mark_off_letters()

        the_guessing_frame = self.nametowidget('the_guessing_frame')

        if self.number_of_guesses > 1:
            self.this_word_object.filter(self.the_guess, self.the_colors)
        
        self.the_guess = self.this_word_object.get_next_guess(True).the_word

        if self.the_guess == 'ZZZZZ':
            self.Word_Not_Found()

        for index in range(self.number_of_letters):
            self.color_button_pressed('lightgray-'+str(index))
            the_guessing_frame.nametowidget(
                'letter-' + str(index))['text'] = self.the_guess[index]

    def Word_Not_Found(self):
        word_not_found_gui = Word_Not_Found_GUI_Class()
        word_not_found_gui.grab_set()

    def game_start_finish(self):

        super().game_start_finish()

        button_frame = self.nametowidget('button_row')
        the_guessing_frame = self.nametowidget('the_guessing_frame')

        if self.number_of_guesses > 0:
            self.this_word_object.filter(self.the_guess, self.the_colors)
        else:
            self.this_word_object = None
            self.this_word_object = The_Word_Class(self.number_of_letters)
            button_frame.nametowidget('start_finish').config(state=tk.DISABLED)

        self.next_guess()

        the_guess = self.this_word_object.get_next_guess(True).the_word

        for index in range(self.number_of_letters):
            self.color_button_pressed('lightgray-'+str(index))
            the_guessing_frame.nametowidget(
                'letter-' + str(index))['text'] = the_guess[index]

    def color_button_pressed(self, this_value):

        the_guessing_frame = self.nametowidget('the_guessing_frame')

        this_value = this_value.partition('-')
        self.the_colors[int(this_value[2])] = get_color(this_value[0])
        the_guessing_frame.nametowidget(
            'letter-' + this_value[2]).config(bg=self.the_colors[int(this_value[2])])

    def exit_game(self):

        super().exit_game()

    def game_start_over(self):
        super().game_start_over()
        self.clear_widgets()
