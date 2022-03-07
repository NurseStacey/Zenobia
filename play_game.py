import tkinter as tk
from constants import *
from word_object import The_Word_Class
from tkinter import font as font
from game_frame import game_frame_class
from WidgetControls import ScrollableFrame
from WidgetControls import font_return

class game_play_frame(game_frame_class):
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.letters_pressed_count = 0
        self.game_started = False
        self.the_answer = ''

    def exit_game(self):
        super().exit_game()
    
    def game_start_over(self):
        
        for index in range(self.number_of_letters):
            self.the_colors[index]=get_color('DeepSkyBlue')

        self.number_of_guesses +=1
        self.the_guess = self.the_answer
        self.add_guess_to_scrollable_frame()

        self.number_of_guesse=0
        
        self.nametowidget('button_row').nametowidget(
            'start_over').config(state=tk.DISABLED)

        super().game_start_over()

    def build_play_game_frame(self):
        super().build_frame()
        self.winfo_toplevel().bind('<KeyPress>', self.playing_game_key_pressed)

        self.nametowidget('top_row').nametowidget(
            'frame_title')['text'] = 'Play Against Zenobia'

        self.nametowidget(
            'button_row').nametowidget('start_over')['text'] = 'I give up'

        self.nametowidget('button_row').nametowidget('next_guess')['text']='Check Word'

    def playing_game_key_pressed(self, the_key):
        
        button_frame = self.nametowidget('button_row')
        the_guessing_frame = self.nametowidget('the_guessing_frame')

        if not self.game_started:
            return

        if the_key.keysym == 'BackSpace':
            if self.letters_pressed_count == 0:
                return
            else:
                self.letters_pressed_count -= 1
                self.the_guess = self.the_guess[:self.letters_pressed_count]
                the_guessing_frame.nametowidget(
                    'letter-' + str(self.letters_pressed_count))['text'] = ' '
                button_frame.nametowidget('next_guess')[
                    'state'] = tk.DISABLED
                return

        if self.letters_pressed_count == self.number_of_letters:
            return

        new_letter = the_key.char.upper()
        if not(new_letter >= 'A' and new_letter <= 'Z'):
            return
        else:
            the_guessing_frame.nametowidget(
                'letter-' + str(self.letters_pressed_count))['text'] = new_letter
            self.the_guess = self.the_guess + new_letter
            self.letters_pressed_count += 1
            if self.letters_pressed_count == self.number_of_letters:
                button_frame.nametowidget('next_guess')['state'] = tk.NORMAL

    def next_guess(self):
        super().next_guess()

        self.the_colors = self.this_word_object.compare_words(self.the_guess, self.the_answer)
        
        if self.add_guess_to_scrollable_frame():  #returns True with a win
            the_answer_lable = self.winfo_toplevel().nametowidget(
                'game_over_win').nametowidget('the_answer')
            the_answer_lable['text'] = self.the_answer + \
                ' in ' + str(self.number_of_guesses) + ' guesses!'
            self.clear_everything()
            self.winfo_toplevel().nametowidget('game_over_win').tkraise()

        if self.number_of_guesses == 20:
            the_answer_lable = self.winfo_toplevel().nametowidget(
                'game_over_lose').nametowidget('the_answer')
            the_answer_lable['text'] = self.the_answer + \
                ' in ' + str(self.number_of_guesses) + ' guesses!'
            
            self.clear_everything()
            self.winfo_toplevel().nametowidget('game_over_lose').tkraise()

        self.mark_off_letters()
        self.letters_pressed_count = 0
        self.the_guess = ''

        for index in range(self.number_of_letters):
            self.nametowidget('the_guessing_frame').nametowidget(
                'letter-' + str(index))['text'] = ' - '
            self.nametowidget('button_row').nametowidget('next_guess')[
                'state'] = tk.DISABLED

    def game_start_finish(self):
        super().game_start_finish()

        self.clear_widgets()
        self.nametowidget('button_row').nametowidget(
            'start_finish').config(state=tk.DISABLED)
        
        self.the_answer = self.this_word_object.get_random_word_from_list().the_word
        self.game_started = True
        self.the_guess = ''
        self.number_of_guesses = 0

    def build_game_over(self):

        this_frame_win = self.winfo_toplevel().nametowidget('game_over_win')
        return_frame = self.winfo_toplevel().nametowidget('play_game')
        main_frame = self.winfo_toplevel().nametowidget('main_frame')
        this_frame_lose = self.winfo_toplevel().nametowidget('game_over_lose')

        this_frame_win.grid_rowconfigure(0, weight=1)
        this_frame_win.grid_columnconfigure(0, weight=1)
        this_frame_win.grid_rowconfigure(5, weight=1)
        this_frame_win.grid_columnconfigure(2, weight=1)

        tk.Label(this_frame_win, text='YOU GOT IT!!!',
                font=font_return(30)).grid(row=1, column=1)
        tk.Label(this_frame_win, text='', name='the_answer',
                font=font_return(30)).grid(row=2, column=1)
        tk.Button(this_frame_win, text='Play Again', font=font_return(30), command=return_frame.tkraise,
                name='play_again').grid(row=3, column=1)
        tk.Button(this_frame_win, text='Return to Main Screen', font=font_return(30), command=main_frame.tkraise,
                name='play_again').grid(row=4, column=1)

        this_frame_lose.grid_rowconfigure(0, weight=1)
        this_frame_lose.grid_columnconfigure(0, weight=1)
        this_frame_lose.grid_rowconfigure(5, weight=1)
        this_frame_lose.grid_columnconfigure(2, weight=1)
        tk.Label(this_frame_lose, text='You lose!',
                font=font_return(30)).grid(row=1, column=1)
        tk.Label(this_frame_lose, text='', name='the_answer',
                font=font_return(30)).grid(row=2, column=1)
        tk.Button(this_frame_lose, text='Play Again', font=font_return(30), command=return_frame.tkraise,
                name='play_again').grid(row=3, column=1)
        tk.Button(this_frame_lose, text='Return to Main Screen', font=font_return(30), command=main_frame.tkraise,
                name='play_again').grid(row=4, column=1)
