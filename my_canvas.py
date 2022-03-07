import tkinter as tk
from constants import *

class One_Square():
    def __init__(self, row, column, upper_x, upper_y, lower_x, lower_y, color):

        self.row = row
        self.column = column
        self.upper_x= upper_x
        self.upper_y= upper_y
        self.lower_x = lower_x
        self.lower_y = lower_y
        self.color = color

    def point_in_square(self, x, y):

        if x<self.upper_x and x>self.lower_x:
            if y<self.upper_y and y>self.lower_y:
                return True

        return False

class My_Canvas(tk.Canvas):
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind('<Button-1>', self.button_click_event)
        
        self.The_Word_Object = None

        self.the_squares = []
        self.start_column = 150
        self.start_row = 175
        self.box_length = 100
        self.box_height = 100

        self.empty_length = 50
        self.empty_height = 50

        self.number_of_letters = 0
        self.test_word = []
        self.the_colors = []
        for i in range(5):
            self.the_colors.append(get_color('lightgray'))

    def do_analysis(self):
        self.The_Word_Object.analyze_algorithm()

    def button_click_event(self, event=None):
        x_coordinate = event.x
        y_coordinate = event.y
        
        this_square = self.get_square(x_coordinate, y_coordinate)
        if not(this_square==None):

            if this_square.row==-1:
                if this_square.color == get_color('red'):
                    self.remove_letter()
                if this_square.color == get_color('blue'):
                    self.do_analysis()
                elif this_square.color == get_color('pink'):
                    if self.number_of_letters==5:
                        self.The_Word_Object.filter(self.test_word, self.the_colors)
                        self.reset_screen()


                        next_guess = self.The_Word_Object.get_next_guess(True)

                        for x in next_guess.the_word:
                            self.add_letter(x)

            else:
                lower_x = self.start_column + self.box_length * \
                    this_square.column + self.empty_length*this_square.column
                upper_x = lower_x + self.box_length
                lower_y = self.start_row + self.box_height * \
                    0 + self.empty_height*0
                upper_y = lower_y + self.box_height
                self.create_rectangle(
                    lower_x, lower_y, upper_x, upper_y, fill=this_square.color)
                if this_square.column<self.number_of_letters:
                    self.create_text(
                        (lower_x+upper_x)/2, (lower_y+upper_y)/2, text=self.test_word[this_square.column], font='Times 20')


                self.the_colors[this_square.column]=this_square.color

        self.winfo_toplevel().update()

    def reset_screen(self):

        for x in range(5):
            self.create_rectangle(
                self.the_squares[x].lower_x, self.the_squares[x].lower_y, self.the_squares[x].upper_x, self.the_squares[x].upper_y, fill=get_color('lightgray'))

            self.test_word = []
            self.the_colors = []
            self.number_of_letters = 0
            for i in range(5):
                self.the_colors.append(get_color('lightgray'))

        self.winfo_toplevel().update()

    def remove_letter(self):
        if self.number_of_letters==0:
            return

        self.number_of_letters -= 1
        lower_x = self.start_column + self.box_length * \
            self.number_of_letters + self.empty_length*self.number_of_letters
        upper_x = lower_x + self.box_length
        lower_y = self.start_row + self.box_height * \
            0 + self.empty_height*0
        upper_y = lower_y + self.box_height


        self.create_rectangle(
            lower_x, lower_y, upper_x, upper_y, fill=self.the_colors[self.number_of_letters])
        # self.create_text(
        #     (lower_x+upper_x)/2, (lower_y+upper_y)/2, text=' ', font='Times 20')

        self.test_word.pop(self.number_of_letters)

    def get_square(self, x, y):

        for one_square in self.the_squares:
            if one_square.point_in_square(x, y):
                return one_square

        return None

    def add_letter(self, letter):

        lower_x = self.start_column + self.box_length * \
            self.number_of_letters + self.empty_length*self.number_of_letters
        upper_x = lower_x + self.box_length
        lower_y = self.start_row + self.box_height * \
            0 + self.empty_height*0
        upper_y = lower_y + self.box_height
        self.create_text(
            (lower_x+upper_x)/2, (lower_y+upper_y)/2, text=letter, font='Times 20')

        self.number_of_letters += 1
        self.test_word.append(letter)

        self.winfo_toplevel().update()

    def build_canvas(self):

        #build four rows of 5 squares


        these_colors = [get_color('lightgray'), get_color(
            'lime'), get_color('LightGoldenrodYellow')]
        for row_index in range(3):
            for column_index in range(5):
                lower_x = self.start_column + self.box_length * \
                    column_index + self.empty_length*column_index
                upper_x = lower_x + self.box_length
                lower_y = self.start_row + self.box_height * \
                    row_index + self.empty_height*row_index
                upper_y = lower_y + self.box_height

                self.the_squares.append(One_Square(row_index, column_index, upper_x, upper_y, lower_x, lower_y, these_colors[row_index]))

                self.create_rectangle(
                    lower_x, lower_y, upper_x, upper_y, fill=these_colors[row_index])

        row_index = -1
        column_index = 0
        lower_x = self.start_column + self.box_length * \
            column_index + self.empty_length*column_index
        upper_x = lower_x + self.box_length
        lower_y = self.start_row + self.box_height * \
            row_index + self.empty_height*row_index
        upper_y = lower_y + self.box_height
        self.create_rectangle(
            lower_x, lower_y, upper_x, upper_y, fill=get_color('red'))
        self.the_squares.append(One_Square(
            row_index, column_index, upper_x, upper_y, lower_x, lower_y, get_color('red')))

        row_index = -1
        column_index = 4
        lower_x = self.start_column + self.box_length * \
            column_index + self.empty_length*column_index
        upper_x = lower_x + self.box_length
        lower_y = self.start_row + self.box_height * \
            row_index + self.empty_height*row_index
        upper_y = lower_y + self.box_height
        self.create_rectangle(
            lower_x, lower_y, upper_x, upper_y, fill=get_color('pink'))
        self.the_squares.append(One_Square(
            row_index, column_index, upper_x, upper_y, lower_x, lower_y, get_color('pink')))


        row_index = -1
        column_index = 3
        lower_x = self.start_column + self.box_length * \
            column_index + self.empty_length*column_index
        upper_x = lower_x + self.box_length
        lower_y = self.start_row + self.box_height * \
            row_index + self.empty_height*row_index
        upper_y = lower_y + self.box_height
        self.create_rectangle(
            lower_x, lower_y, upper_x, upper_y, fill=get_color('blue'))
        self.the_squares.append(One_Square(
            row_index, column_index, upper_x, upper_y, lower_x, lower_y, get_color('blue')))


    def set_word_object(self, The_Word_Object):
        self.The_Word_Object = The_Word_Object

        first_guess = self.The_Word_Object.get_next_guess(False)

        for x in first_guess.the_word:
            self.add_letter(x)
