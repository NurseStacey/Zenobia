import tkinter as tk
from constants import *
from word_object import The_Word_Class
from tkinter import font as font
from WidgetControls import font_return
from PIL import Image, ImageTk
from game_frame import game_frame_class
from play_game import game_play_frame
from zenobia_plays import zenobia_play_class
from analyzing_frame import analyzing_frame_class

class icons_class():
    def __init__(self):
        self.button_images = []
        img = Image.open('Image_Files\\down.png')
        self.button_images.append(ImageTk.PhotoImage(img))

        img = Image.open('Image_Files\\up.png')
        self.button_images.append(ImageTk.PhotoImage(img))

# def load_icons():
#     img = Image.open('Image_Files\\down.png')
#     button_images.append(ImageTk.PhotoImage(img))

#     img = Image.open('Image_Files\\up.png')
#     button_images.append(ImageTk.PhotoImage(img))

def build_main_frame ():
    
    main_frame = root.nametowidget('main_frame')

    this_row = 0
    main_frame.grid_rowconfigure(this_row, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)
    
    
    this_row += 1
    tk.Button(main_frame, text='Play Game', command=root.nametowidget('play_game').tkraise, width=30, height=2,
              font=font_return(30)).grid(row=this_row, column=1, pady=20)
    this_row += 1
    tk.Button(main_frame, text='Have Zenobia Play', command=root.nametowidget('zenobia_play').tkraise, width=30, height=2, font=font_return(
        30)).grid(row=this_row, column=1, pady=20)
    this_row += 1        
    tk.Button(main_frame, text='Analysis Zenobia\'s System', command=root.nametowidget('analyze').tkraise, width=30, height=2,  font=font_return(
        30)).grid(row=this_row, column=1, pady=20)
    
    this_row += 1
    main_frame.grid_rowconfigure(this_row, weight=1)
    main_frame.grid_columnconfigure(2, weight=1)

root = tk.Tk()

main_frame = None

root.title('Zenobia')

icons_obj = icons_class()

tk.Frame(root, name='main_frame',
         width=300, height=500, bg='red').grid(row=0, column=0, sticky='NEWS')

game_play_obj = game_play_frame(root, name='play_game', width=300, height=500,
                bg=get_color('cyan'))
game_play_obj.grid(row=0, column=0, sticky='NEWS')
game_play_obj.set_button_images(icons_obj)

tk.Frame(root, name='game_over_win', width=300, height=500,
         bg=get_color('lime')).grid(row=0, column=0, sticky='NEWS')
tk.Frame(root, name='game_over_lose', width=300, height=500,
         bg=get_color('Beige')).grid(row=0, column=0, sticky='NEWS')

zenobia_play_obj = zenobia_play_class(
    root, name='zenobia_play', width=300, height=500, bg=get_color('cyan'))
zenobia_play_obj.grid(row=0, column=0, sticky='NEWS')
zenobia_play_obj.set_button_images(icons_obj)
analyze_obj = analyzing_frame_class(root, name='analyze', width=300, height=500,
                      bg='pink')
analyze_obj.grid(row=0, column=0, sticky='NEWS')
analyze_obj.set_button_images(icons_obj)

build_main_frame()
game_play_obj.build_play_game_frame()
game_play_obj.build_game_over()
zenobia_play_obj.build_frame()
analyze_obj.build_frame()

root.nametowidget('main_frame').tkraise()

root.mainloop()

