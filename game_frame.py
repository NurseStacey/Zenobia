import tkinter as tk
from constants import *
from word_object import The_Word_Class
from tkinter import font as font
from WidgetControls import ScrollableFrame
from WidgetControls import font_return


class game_frame_class(tk.Frame):

    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_of_guesses = 0
        self.button_images = []
        self.the_colors = []
        self.number_of_letters = 5
        self.this_word_object=None
        self.number_of_guesses = 0
        self.the_guess = ''
        self.game_started = False

    def set_button_images(self, button_object):

        self.button_object=button_object
        # for one_image in button_images:
        #     self.button_images.append(one_image)

    def build_frame(self):

        
        self.number_of_guesses = 0
        
        self.this_word_object = None
        self.the_colors = []
        

        main_frame_row = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(main_frame_row, weight=1)

        top_row_frame = tk.Frame(self, width=800,  name='top_row',
                                 bg=get_color('cyan'),
                                 highlightbackground="yellow", highlightthickness=2)
        top_row_frame.grid(row=main_frame_row, column=1)

        this_row = 0

        tk.Label(top_row_frame, text=' ',  name='frame_title', font=font_return(
            20)).grid(row=this_row, column=1, columnspan=5)

        this_row += 1
        tk.Label(top_row_frame, text='Play with ', bg=get_color(
            'cyan'), font=font_return(15)).grid(row=this_row, column=1)
        tk.Button(top_row_frame, name='up_button', image=self.button_object.button_images[0], command=lambda: self.change_number_letters(
            -1)).grid(row=this_row, column=2)
        tk.Label(top_row_frame, name='number_letters', bg=get_color('cyan'), text='  ' + str(self.number_of_letters) + '  ',
                 font=font_return(15)).grid(row=this_row, column=3)
        tk.Button(top_row_frame, name='down_button', image=self.button_object.button_images[1], command=lambda: self.change_number_letters(
            1)).grid(
            row=this_row, column=4)
        tk.Label(top_row_frame, bg=get_color('cyan'), text=' letters ', font=font_return(
            15)).grid(row=this_row, column=5)

        main_frame_row += 1
        button_frame = tk.Frame(self, width=800,
                                name='button_row',  bg=get_color('cyan'),
                                highlightbackground="yellow", highlightthickness=2)
        button_frame.grid(row=main_frame_row, column=1)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(2, weight=1)

        this_row = 0
        tk.Button(button_frame, name='start_finish', command=self.game_start_finish, text='Start', font=font_return(
            15), width=10, bg=get_color('pink')).grid(row=this_row, column=1)
        tk.Button(button_frame, name='start_over', command=self.game_start_over, text='New Game', font=font_return(
            15), width=10, bg=get_color('pink')).grid(row=this_row, column=2)
        button_frame.nametowidget('start_over').config(state=tk.DISABLED)

        this_row += 1
        tk.Button(button_frame, name='return', command=self.exit_game, text='Main Menu', font=font_return(
            15), width=10, bg=get_color('pink')).grid(row=this_row, column=1)
        tk.Button(button_frame, name='next_guess', command=self.next_guess, text='Next Guess', font=font_return(
            15), width=10, bg=get_color('pink')).grid(row=this_row, column=2)
        button_frame.nametowidget('next_guess').config(state=tk.DISABLED)

        main_frame_row += 1

        the_guessing_frame = tk.Frame(self, name='the_guessing_frame', bg=get_color('cyan'))
        the_guessing_frame.grid(row=main_frame_row, column=1)

        self.add_guessing_widgets(self.number_of_letters)

        main_frame_row += 1

        bottom_row_frame = tk.Frame(
            self, name='bottom_row_frame', bg=get_color('pink'))
        bottom_row_frame.grid(row=main_frame_row, column=1)

        bottom_row_frame.grid_columnconfigure(0, weight=1)
        bottom_row_frame.grid_columnconfigure(3, weight=1)

        the_guesses_frame = ScrollableFrame(bottom_row_frame, width=450, height=150, name='the_guesses_frame',
                                             bg=get_color('red'))
        the_guesses_frame.grid(row=1, column=1, rowspan=2)
        #the_guesses_frame.scrollable_frame.config(bg=get_color('red'))
        tk.Label(bottom_row_frame, name='number_guesses_label', bg=get_color('pink'), text='Number\nOf\nGuesses', font=font_return(16)).grid(
            row=1, column=2)

        tk.Label(bottom_row_frame, text='-',
                 name='number_guess').grid(row=2, column=2)

        the_alphabet_frame = tk.Frame(bottom_row_frame, width=400, name='the_alphabet',
                                      bg=get_color('cyan'),
                                      highlightbackground="yellow", highlightthickness=2)
        the_alphabet_frame.grid(row=1, column=3, rowspan=2)

        for index_row in range(5):
            for index_column in range(5):
                letter = chr(index_row*5+index_column + 65)
                tk.Label(the_alphabet_frame, bg=get_color('cyan'), text=letter, font=font_return(
                    14), name='label-' + letter).grid(row=index_row, column=index_column)

        letter = chr(90)
        tk.Label(the_alphabet_frame, text=letter, bg=get_color('cyan'), font=font_return(14), name='label-' +
                 letter).grid(row=4, column=5)

        main_frame_row += 1
        self.grid_rowconfigure(main_frame_row, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def clear_everything(self):
        self.nametowidget('button_row').nametowidget(
            'start_finish').config(state=tk.NORMAL)

        if self.game_started:
            self.game_start_over()
            self.clear_widgets()


    def exit_game(self):
        self.clear_everything()        
        self.winfo_toplevel().nametowidget('main_frame').tkraise()
        

    def add_guessing_widgets(self,new_number_of_letters):
        

        self.the_colors = []
        the_guessing_frame = self.nametowidget('the_guessing_frame')
        for index in range(new_number_of_letters):

            self.the_colors.append(get_color('lightgray'))
            tk.Label(the_guessing_frame, width=1, bg=get_color('lightgray'), font=font_return(
                30), text='-', name='letter-' + str(index), bd=0).grid(row=2, column=index+1, pady=10, padx=20)

    def clear_widgets(self):
        self.clear_scrollable_frame()
        self.clear_alphabet_frame()
        self.remove_letter_labels()
        self.add_guessing_widgets(self.number_of_letters)
        self.nametowidget('bottom_row_frame').nametowidget(
            'number_guesses_label')['text'] = 'Number\nOf\nGuesses'
        self.game_started = False

    def clear_alphabet_frame(self):
        the_alphabet_frame = self.nametowidget('bottom_row_frame').nametowidget('the_alphabet')

        for index in range(26):
            the_alphabet_frame.nametowidget('label-'+ chr(65+index)).config(bg=get_color('cyan'))

    def clear_scrollable_frame(self):

        for child in self.nametowidget('bottom_row_frame').nametowidget('the_guesses_frame').scrollable_frame.winfo_children():
            child.destroy()

    def add_guess_to_scrollable_frame(self):

        the_guesses_frame = self.nametowidget('bottom_row_frame').nametowidget('the_guesses_frame')
        winner = True

        font_size = 30
        pad_size = 20

        if self.number_of_letters>6:
            font_size -=8
            pad_size -=4

        if self.number_of_letters>8:
            font_size -=5
            pad_size -=5

        for index in range(self.number_of_letters):
            tk.Label(the_guesses_frame.scrollable_frame, bg=self.the_colors[index], font=font_return(
                font_size), text=self.the_guess[index]).grid(row=20-self.number_of_guesses, column=index+1, padx=pad_size)
            if not(self.the_colors[index]==get_color('lime')):
                winner=False

        return winner    

    def mark_off_letters(self):
        the_alphabet_frame = self.nametowidget(
            'bottom_row_frame').nametowidget('the_alphabet')

        green_letters = []

        yellow_letters = []
        gray_letters = []


        for index in range(self.number_of_letters):
            if self.the_colors[index]==get_color('lime'):
                green_letters.append(self.the_guess[index])
                this_letter = the_alphabet_frame.nametowidget(
                  'label-' + self.the_guess[index])
                this_letter.config(bg=get_color('lime'))

        for index in range(self.number_of_letters):
            if not (self.the_guess[index] in green_letters) and self.the_colors[index] == get_color('LightGoldenrodYellow'):
                yellow_letters.append(self.the_guess[index])
                this_letter = the_alphabet_frame.nametowidget(
                    'label-' + self.the_guess[index])
                this_letter.config(bg=get_color('LightGoldenrodYellow'))

        for index in range(self.number_of_letters):
            if not (self.the_guess[index] in green_letters) and not (self.the_guess[index] in yellow_letters):
                gray_letters.append(self.the_guess[index])
                this_letter = the_alphabet_frame.nametowidget(
                    'label-' + self.the_guess[index])
                this_letter.config(bg=get_color('lightgray'))

    def next_guess(self):
        self.number_of_guesses += 1
        bottom_row_frame = self.nametowidget('bottom_row_frame')

        bottom_row_frame.nametowidget('number_guesses_label')[
           'text'] = 'Number\nOf\nGuesses\n'+ str(self.number_of_guesses)

    def game_start_finish(self):

        
        self.nametowidget('button_row').nametowidget('start_over').config(state=tk.NORMAL)
        self.nametowidget('button_row').nametowidget('next_guess').config(state=tk.NORMAL)

        top_row_frame = self.nametowidget('top_row')
        top_row_frame.nametowidget('down_button')[
            'state'] = tk.DISABLED
        top_row_frame.nametowidget('up_button')[
            'state'] = tk.DISABLED
 
        self.this_word_object = None
        self.this_word_object = The_Word_Class(self.number_of_letters)

    def change_number_letters(self, direction):

        top_row_frame = self.nametowidget('top_row')

        if self.number_of_letters == 4 and direction < 0:
            return

        if self.number_of_letters == 10 and direction > 0:
            return

        self.remove_letter_labels()

        self.number_of_letters += direction

        self.add_guessing_widgets(self.number_of_letters)

        top_row_frame.nametowidget('number_letters')[
            'text'] = ' ' + str(self.number_of_letters) + ' '

    def remove_letter_labels(self):

        the_guessing_frame = self.nametowidget('the_guessing_frame')

        for index in range(self.number_of_letters):
            the_guessing_frame.nametowidget(
                'letter-' + str(index)).destroy()
        
    def game_start_over(self):
        self.nametowidget('button_row').nametowidget(
            'start_finish').config(state=tk.NORMAL)

        self.number_of_guesses = 0
        the_guessing_frame = self.nametowidget('the_guessing_frame')

        for index in range(self.number_of_letters):
            the_guessing_frame.nametowidget(
                'letter-'+str(index))['text'] = '-'
            the_guessing_frame.nametowidget(
                'letter-'+str(index)).config(bg=get_color('lightgray'))

        top_row_frame = self.nametowidget('top_row')
        top_row_frame.nametowidget('down_button')[
            'state'] = tk.NORMAL
        top_row_frame.nametowidget('up_button')[
            'state'] = tk.NORMAL
        
