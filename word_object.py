from constants import *
import tkinter as tk
import copy
import random
import ctypes
from WidgetControls import font_return_times

class Word_For_Analysis():
    def __init__(self, the_word):
        self.the_word = the_word
        self.path = []
        self.number_of_iterations = 0

class One_Word_Class():
    def __init__(self, the_word):
        self.the_word = the_word
        self.ranking = 0
        self.testing_word = the_word

    def all_unique_letters(self):

        temp = ''
        for x in self.the_word:
            if x in temp:
                return False
            else:
                temp = temp + x

        return True

class One_Letter_Class():
    def __init__(self, the_letter, the_count, the_rank):
        self.the_letter = the_letter
        self.the_count = the_count
        self.the_rank = the_rank

class The_Word_Class():
    def __init__(self, size_of_words):

        self.get_next_guess = self.get_next_guess_simple
        #all_words_file = open('5 letter words.txt', 'r')
        all_words_file = open('All Words.txt', 'r')
        #all_words_file = open('some_words.txt', 'r')
        #all_words_file = open('wordle_word_list.txt','r')
        # wordle_word_list are the words from the original wordle game
        # Much smaller list

        self.analysis_words = []
        self.the_words = []
        
        for one_line in all_words_file.readlines():

            one_line = one_line.replace('\n', '')
            if len(one_line) == size_of_words:
                self.the_words.append(One_Word_Class(one_line.upper()))
                self.analysis_words.append(Word_For_Analysis(one_line.upper()))

        all_words_file.close()
        self.size_of_words = size_of_words
    
    def compare_words(self,guess, answer):
        answer_copy = copy.deepcopy(answer)
        #length_of_word = len(guess)
        colors = []
        for index in range(self.size_of_words):
            colors.append(get_color('lightgray'))

        index_to_skip = []

        for index, letter in enumerate(guess):
            if answer_copy[index] == letter:
                #colors.append(get_color('lime'))
                colors[index]=get_color('lime')
                answer_copy = answer_copy[:index] + \
                    ' ' + answer_copy[index+1:self.size_of_words]
                index_to_skip.append(index)

        for index, letter in enumerate(guess):
            if not(index in index_to_skip):
                if letter in answer_copy:
                    colors[index] = get_color('LightGoldenrodYellow')
                    #colors.append(get_color('LightGoldenrodYellow'))
                    answer_copy = answer_copy.replace(
                        letter, ' ', 1)

        return colors

    def analyze_algorithm(self, update_frame, the_results):
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

        total_number_of_words = len(self.the_words)
        words_completed = 0
        percent_completed = 0
        update_frame.nametowidget('status_bar')['text'] = str(
            percent_completed) + chr(37) + ' completed'
        update_frame.winfo_toplevel().winfo_toplevel().update()

        frequency_of_iterations = []
        for x in range(30):
            frequency_of_iterations.append(0)
        
        copy_of_the_words = copy.deepcopy(self.the_words)

        for one_word in self.analysis_words:

            one_word.number_of_iterations=0

            allow_duplicates = True

            while True:
                one_word_copy = copy.deepcopy(one_word)
                next_guess = self.get_next_guess(allow_duplicates)
                one_word.path.append(next_guess.the_word)
                one_word.number_of_iterations += 1

                if next_guess.the_word==one_word.the_word:
                    frequency_of_iterations[one_word.number_of_iterations] += 1
                    break

                allow_duplicates = True

                colors = []

                for index, letter in enumerate(next_guess.the_word):
                    if one_word_copy.the_word[index] == letter:
                        colors.append(get_color('lime'))
                        one_word_copy.the_word = one_word_copy.the_word[:index] + \
                            ' ' + \
                            one_word_copy.the_word[index+1:self.size_of_words]
                    elif letter in one_word_copy.the_word:
                        colors.append(get_color('LightGoldenrodYellow'))
                        one_word_copy.the_word = one_word_copy.the_word.replace(letter, ' ', 1)
                    else:
                        colors.append(get_color('lightgray'))
                
                self.filter(next_guess.the_word, colors)

            self.the_words = copy.deepcopy(copy_of_the_words)
            words_completed +=1

            if (int(100*words_completed/total_number_of_words)-percent_completed)>10:
                percent_completed += 10
                update_frame.nametowidget('status_bar')['text']=str(percent_completed) + chr(37)+ ' completed'
                update_frame.winfo_toplevel().winfo_toplevel().update()

        number_of_tries = 0
        most_common = []
        #least_iterations = []
        highest = 0
        sum_for_average_calc = 0

        update_frame.nametowidget('status_bar')['text'] = 'Finished'
        for index in range(30):
            x = frequency_of_iterations[index]
            number_of_tries += x
            sum_for_average_calc += x*index
            if x>0:
                highest = index

            if len(most_common)==0:
                most_common.append(index)
            elif x == frequency_of_iterations[most_common[0]]:
                most_common.append(index)
            elif x>frequency_of_iterations[most_common[0]]:
                most_common = []
                most_common.append(index)

        the_average = int(1000*sum_for_average_calc/number_of_tries)/1000

        output = []
        this_text = 'The Results'
        tk.Label(the_results, text=this_text,
                 font=font_return_times(16)).grid(sticky='W', row=1, column=1)
        output.append(this_text)

        this_text = 'Averege number of iterations = ' + str(the_average)
        tk.Label(the_results, text=this_text,  font=font_return_times(
            16)).grid(sticky='W', row=2, column=1)
        output.append(this_text)

        this_text = 'Most common number of iterations = ' + str(frequency_of_iterations[most_common[0]])
        tk.Label(the_results, text=this_text,  font=font_return_times(
            16)).grid(sticky='W', row=3, column=1)
        output.append(this_text)

        this_text='Most iterations = ' + str(highest)
        tk.Label(the_results, text=this_text,  font=font_return_times(
            16)).grid(sticky='W', row=4, column=1)
        output.append(this_text)


        for index in range(len(frequency_of_iterations)):
            if frequency_of_iterations[index]>0:
                this_text='The number with ' + str(index) + ' iterations: ' + str(frequency_of_iterations[index])
                tk.Label(the_results, text=this_text,  font=font_return_times(16)).grid(sticky='W', row=6+index, column=1)
                output.append(this_text)

        this_file = open('output.txt','w')
        for one_line in output:
            this_file.write(one_line + '\n')
    
        this_file.close()

        update_frame.winfo_toplevel().winfo_toplevel().update()
        
        ctypes.windll.kernel32.SetThreadExecutionState(
            0x80000000)  # set the setting back to normal

    def get_next_guess_simple(self, allow_duplicate_letters):

        if  len(self.the_words)==0:
            return One_Word_Class('ZZZZZ')

        letter_frequence = []
        
        #calculate the rank of each letter
        number_of_letters = self.size_of_words*len(self.the_words)

        for index in range(26):
            count = 0

            for one_word in self.the_words:
                count += one_word.the_word.count(chr(index+65))

            letter_frequence.append(One_Letter_Class(
                chr(index+65), count, count/number_of_letters))

        
        #give each word a ranking based on frequency and get the maximum word
        maximum_word = One_Word_Class('ZZZZZ')
        #maximum_word = []
        #maximum_word.append(One_Word_Class('ZZZZZ'))
        maximum_word.ranking = 0
        #maximum_word[0].ranking = 0
        #sum_for_average_rank = 0
        #current_average = (sum_for_average_rank/len(maximum_word))

        for one_word in self.the_words:
            one_word.ranking = 0
            if allow_duplicate_letters or one_word.all_unique_letters():
                for index in range(5):
                    letter_index = ord(one_word.the_word[index])-65
                    one_word.ranking += letter_frequence[letter_index].the_rank

##          this is the simplest
                if one_word.ranking > maximum_word.ranking:
                    maximum_word = one_word

##          this involves some randomness
            
            # if (one_word.ranking - current_average) > .03:
            #     maximum_word = []
            #     maximum_word.append(one_word)
            #     sum_for_average_rank = 0
            # elif abs(one_word.ranking-current_average)<.03:
            #     maximum_word.append(one_word)
            #     sum_for_average_rank += one_word.ranking

        #this reutrns a random word from the maximum rankings          
        #return random.choice(maximum_word)   

        return maximum_word

    def get_next_guess_random(self, allow_duplicate_letters):

        #this_file = open('testing.txt', 'w')

        if len(self.the_words) == 0:
            return One_Word_Class('ZZZZZ')

        letter_frequence = []

        #calculate the rank of each letter
        number_of_letters = self.size_of_words*len(self.the_words)

        for index in range(26):
            count = 0

            for one_word in self.the_words:
                count += one_word.the_word.count(chr(index+65))

            letter_frequence.append(One_Letter_Class(
                chr(index+65), count, count/number_of_letters))

        #give each word a ranking based on frequency and get the maximum word
        
        maximum_word = []
        maximum_word.append(One_Word_Class('ZZZZZ'))
        
        maximum_word[0].ranking = 0
        sum_for_average_rank = 0
        current_average = (sum_for_average_rank/len(maximum_word))

        for one_word in self.the_words:
            one_word.ranking = 0
            if allow_duplicate_letters or one_word.all_unique_letters():
                for index in range(5):
                    letter_index = ord(one_word.the_word[index])-65
                    one_word.ranking += letter_frequence[letter_index].the_rank

            #this_file.write(one_word.the_word + ': ' + str(one_word.ranking) + '\n')
##          this involves some randomness

            if (one_word.ranking - current_average) > .03:
                maximum_word = []
                maximum_word.append(one_word)
                sum_for_average_rank = one_word.ranking
                
            elif abs(one_word.ranking-current_average)<.03:
                maximum_word.append(one_word)
                sum_for_average_rank += one_word.ranking

            current_average = sum_for_average_rank/len(maximum_word)
        #this reutrns a random word from the maximum rankings

        #this_file.close()
        return random.choice(maximum_word)

    def get_random_word_from_list(self):
        return random.choice(self.the_words)

    def filter(self, letters, colors):
        indexes_to_remove = []

        for index in range(self.size_of_words):

            if colors[index]==get_color('lime'):
                for word_index, one_word in enumerate(self.the_words):

                    if not word_index in indexes_to_remove:
                        if not(one_word.testing_word[index] == letters[index]):
                            indexes_to_remove.append(word_index)
                        else:
                            one_word.testing_word = one_word.testing_word[:index] + \
                                ' ' + \
                                one_word.testing_word[index +
                                                      1:self.size_of_words]

        for index in range(self.size_of_words):
            if colors[index] == get_color('LightGoldenrodYellow'):
                #for one_word in self.the_words:
                for word_index, one_word in enumerate(self.the_words):

                    if not word_index in indexes_to_remove:
                        if one_word.testing_word[index] == letters[index]:
                            indexes_to_remove.append(word_index)
                        elif not(letters[index] in one_word.testing_word):
                            indexes_to_remove.append(word_index)
                        else:
                            one_word.testing_word = one_word.testing_word.replace(
                                letters[index], ' ', 1)

        for index in range(self.size_of_words):
            if colors[index]==get_color('lightgray'):
                for word_index, one_word in enumerate(self.the_words):

                    if not word_index in indexes_to_remove:
                        if letters[index] in one_word.testing_word:
                            indexes_to_remove.append(word_index)

        for one_word in self.the_words:
            one_word.testing_word = one_word.the_word

        indexes_to_remove.sort()
        for index in reversed(indexes_to_remove):
            self.the_words.pop(index)
