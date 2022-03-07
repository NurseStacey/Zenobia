import tkinter as tk
from tkinter import ttk
from constants import *
from WidgetControls import font_return

class ScrollableFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        canvas = tk.Canvas(
            self, width=kwargs['width'], height=kwargs['height'])
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas,  width=kwargs['width'], height=kwargs['height'])
        self.scrollable_frame.grid(row=1, column=1)
        self.scrollable_frame.bind(
             "<Configure>",
             lambda e: canvas.configure(
                 scrollregion=canvas.bbox("all")
             )
        )

        canvas.grid(row=1, column=1)
        canvas.create_window(
            0, 0, width=kwargs['width'], window=self.scrollable_frame,  anchor="nw")
        

        canvas.configure(scrollregion=canvas.bbox(
            'all'),  yscrollcommand=self.scrollbar.set)

        self.scrollbar.grid(row=1, column=2, sticky='NS')

root= tk.Tk()
root.geometry('1000x200')
tk.Frame(root, name='this_frame').grid(row=1, column=1, sticky='NEWS')

this_frame = root.nametowidget('play_game')

this_row = 0

this_frame.grid_columnconfigure(0, weight=1)
this_frame.grid_rowconfigure(this_row, weight=1)

top_row_frame = tk.Frame(this_frame, width=800,  name='top_row',
                         bg=get_color('cyan'),
                         highlightbackground="yellow", highlightthickness=2)
top_row_frame.grid(row=this_row, column=1)

tk.Label(top_row_frame, text='Play with ', bg=get_color(
    'cyan'), font=font_return(30)).grid(row=1, column=1)
tk.Button(top_row_frame, text='>').grid(row=1, column=2)
tk.Label(top_row_frame, name='number_letters', bg=get_color('cyan'), text='  ' + str(number_of_letters) + '  ',
         font=font_return(30)).grid(row=1, column=3)
tk.Button(top_row_frame,  text='<').grid(
    row=1, column=4)
tk.Label(top_row_frame, bg=get_color('cyan'), text=' letters ', font=font_return(
    30)).grid(row=1, column=5)

this_row += 1
button_frame = tk.Frame(this_frame, width=800,
                        name='button_row',  bg=get_color('cyan'),
                        highlightbackground="yellow", highlightthickness=2)
button_frame.grid(row=this_row, column=1)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(2, weight=1)
tk.Button(button_frame, name='start_finish', text='Start', font=font_return(
    30), bg=get_color('pink')).grid(row=1, column=1)
tk.Button(button_frame, text='Check Word', state=tk.DISABLED, font=font_return(
    30), name='check_word').grid(row=2, column=1)

#the letters
this_row += 1

the_guessing_frame = tk.Frame(this_frame, bg=get_color('cyan'))
the_guessing_frame.grid(row=this_row, column=1)

#add_letter_labels(number_of_letters)

this_row += 1
the_guesses_frame = ScrollableFrame(this_frame, width=800, height=150,
                                    highlightbackground="yellow", highlightthickness=2)
the_guesses_frame.grid(row=this_row, column=1, columnspan=3)

this_row += 1
this_frame.grid_rowconfigure(this_row, weight=1)
this_frame.grid_columnconfigure(2, weight=1)

root.mainloop()
