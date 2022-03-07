import tkinter as tk
from constants import *
from word_object import The_Word_Class
from tkinter import font as font
from WidgetControls import font_return
from WidgetControls import ScrollableFrame

class analyzing_frame_class(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_of_letters = 5
        self.this_word_object = None
        self.button_images = []

    def set_button_images(self, button_object):
        
        self.button_object = button_object
        # for one_image in button_images:
        #     self.button_images.append(one_image)

    def start_analyzing(self):
        
        this_word_object = The_Word_Class(self.number_of_letters)
        this_word_object.analyze_algorithm(self.nametowidget(
            'update_frame'), self.nametowidget('the_results').scrollable_frame)

    def build_frame(self):

        this_frame_row = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(this_frame_row, weight=1)
        this_frame_row += 1
        
        top_row_frame = tk.Frame(self, width=800, name='top_row_frame',
                                bg=get_color('cyan'))
        top_row_frame.grid(row=this_frame_row, column=1)
        top_row_frame.grid_columnconfigure(0, weight=1)
        this_row = 0
        tk.Label(top_row_frame, text="Analyze Zenobia's methodology",
                font=font_return(30)).grid(row=this_row, column=1, columnspan=5)
        top_row_frame.grid_rowconfigure(this_row, weight=1)
        this_row += 1
        tk.Label(top_row_frame, text='Play with ', bg=get_color('cyan'),
                font=font_return(30)).grid(row=this_row, column=1)
        tk.Button(top_row_frame, name='up_button', image=self.button_object.button_images[0], command=lambda: self.change_number_letters(
            -1)).grid(row=this_row, column=2)
        tk.Label(top_row_frame, name='number_letters', bg=get_color('cyan'), text='  ' + str(self.number_of_letters) + '  ',
                font=font_return(30)).grid(row=this_row, column=3)
        tk.Button(top_row_frame, name='down_button', image=self.button_object.button_images[1], command=lambda: self.change_number_letters(
            1)).grid(row=this_row, column=4)
        tk.Label(top_row_frame, bg=get_color('cyan'), text=' letters ', font=font_return(
            30)).grid(row=this_row, column=5)
        this_row += 1
        tk.Button(top_row_frame, name='start_analyzing', command=self.start_analyzing, text='Start Analysis', font=font_return(
            30)).grid(row=this_row, column=1, columnspan=5)
        this_row += 1
        tk.Button(top_row_frame, name='return', command=self.winfo_toplevel().nametowidget('main_frame').tkraise, text='Return to Main Menu', font=font_return(
            30), bg=get_color('pink')).grid(row=this_row, column=1, columnspan=5)

        top_row_frame.grid_columnconfigure(6, weight=1)

        this_frame_row += 1

        update_frame = tk.Frame(self, name='update_frame', bg=get_color('pink'))

        update_frame.grid(row=this_frame_row, column=1)
        update_frame.rowconfigure(0,weight=1)
        update_frame.rowconfigure(2,weight=1)
        tk.Label(update_frame, name='status_bar', bg=get_color('yellow'), font=font_return(30), text = '').grid(row=1, column=1)

        this_frame_row += 1
        ScrollableFrame(self, name='the_results', bg=get_color(
            'LightCoral'), width=600, height=175).grid(row=this_frame_row, column=1)

        this_frame_row += 1

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(this_frame_row, weight=1)

    def change_number_letters(self, direction):

        if self.number_of_letters == 4 and direction < 0:
            return

        if self.number_of_letters == 15 and direction > 0:
            return

        self.number_of_letters += direction

        self.nametowidget('top_row_frame').nametowidget('number_letters')[
            'text'] = ' ' + str(self.number_of_letters) + ' '
        self.winfo_toplevel().update()
