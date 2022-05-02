# Angelica Cabato
# Dr. Shawn X Wang, Professor
# CPSC 485 - 01
# 2 May 2022

import numpy as np


def print_alignment(alignment, word, i, j,word_alignment, diff, pos):
    # if second word
    if pos == 2:
        if i <= 0 and j <= 0:
            print(word_alignment)
            return word_alignment
        if diff == 0:
            if i <= 0 or j <= 0:
                print(word_alignment)
                return word_alignment
        if alignment[i, j] == 'd':
            idx = (i + diff) - 1
            word_alignment = word[idx] + word_alignment
            print_alignment(alignment, word, i - 1, j - 1, word_alignment,
                            diff, pos)
        else:
            if alignment[i, j] == 'u':
                idx = (i + diff) - 1
                word_alignment = word[idx] + word_alignment
                word_alignment = '_' + word_alignment
                print_alignment(alignment, word, i - 1, j, word_alignment,
                                diff, pos)
            else:
                idx = (i + diff) - 1
                word_alignment = word[idx] + word_alignment
                # word_alignment = '_' + word_alignment
                print_alignment(alignment, word, i, j - 1, word_alignment, diff,
                            pos)
    else:
        if i <= 0 and j <= 0:
            print(word_alignment)
            return word_alignment
        if alignment[i, j] == 'd':
            idx = (i + diff) - 1
            word_alignment = word[idx] + word_alignment
            print_alignment(alignment, word, i - 1, j - 1, word_alignment, diff,
                            pos)
        else:
            if alignment[i, j] == 'u':
                idx = (i + diff) - 1
                word_alignment = word[idx] + word_alignment
                print_alignment(alignment, word, i - 1, j, word_alignment, diff,
                            pos)
            else:
                word_alignment = '_' + word_alignment
                print_alignment(alignment, word, i, j - 1, word_alignment, diff,
                            pos)


def edit_distance(first_word, second_word):
    indel = 1

    n = len(first_word)
    m = len(second_word)

    row = n + 1
    col = m + 1

    # initializing the matrices
    x = np.zeros((row, col), dtype=int)
    alignment = np.empty((row, col), dtype=str)

    if row > col:
        larger_axis = row
    else:
        larger_axis = col

    for idx in range(larger_axis):
        if idx <= n:
            x[idx, 0] = idx
            alignment[idx, 0] = 'u'
        if idx <= m:
            x[0, idx] = idx
            alignment[0, idx] = 'l'

    alignment[0, 0] = 'd'

    first_word_alignment = " "
    second_word_alignment = " "

    # building the matrix
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                continue
            else:
                cur_cell = x[i, j]
                left_cell = x[i, j - 1]
                up_cell = x[i - 1, j]
                diag_cell = x[i - 1, j - 1]
                a = first_word[i - 1]
                b = second_word[j - 1]
                if (first_word[i - 1] != second_word[j - 1]):
                    closest_neighbors = (left_cell, up_cell, diag_cell)
                    x[i, j] = min(closest_neighbors) + indel
                    if (min(closest_neighbors) == left_cell):
                        alignment[i, j] = 'l'
                    if (min(closest_neighbors) == up_cell):
                        alignment[i, j] = 'u'
                    elif (min(closest_neighbors) == diag_cell):
                        alignment[i, j] = 'd'
                else:
                    closest_neighbors = (left_cell, up_cell, diag_cell)
                    x[i, j] = min(closest_neighbors)
                    if (min(closest_neighbors) == left_cell):
                        alignment[i, j] = 'l'
                    if (min(closest_neighbors) == up_cell):
                        alignment[i, j] = 'u'
                    elif (min(closest_neighbors) == diag_cell):
                        alignment[i, j] = 'd'


    # Print out information
    print("Below are the results: \n")
    print("The matrix:")
    print(x)
    print("\nThe edit distance is: ", x[n, m])
    print("\nThe alignment is:")

    # Print Alignment
    first_word_alignment = " "
    second_word_alignment = " "

    if n != m:
        first_word_alignment = print_alignment(alignment, first_word, i, j,
                                               first_word_alignment, diff=0,pos=1)
        second_word_alignment = print_alignment(alignment, second_word, i, j,second_word_alignment, diff=1, pos=2)
    else:
        first_word_alignment = print_alignment(alignment, first_word, i, j, first_word_alignment, diff=0,pos=1)
        second_word_alignment = print_alignment(alignment, second_word, i, j,
                                                second_word_alignment, diff=0, pos=2)


def main():

    # Welcome message
    print("Welcome! This program calculates the edit distance between two words "
          "and output both the matrix of distance calculation and an alignment "
          "that demonstrates the result.\n")
    print("Please follow the prompts below to input your words. Input cannot "
          "contain a number or symbol and no need for a space before or after entering your word.\n")


    # Accept User Input and validate that it is a string

    first_word = input("Enter first word: ")
    if not first_word.isalpha():
        while first_word.isalpha() is False:
            print("Input cannot contain a number, please try again.")
            first_word = input("Enter first word: ")

    second_word = input("Enter second word: ")
    if not second_word.isalpha():
        while second_word.isalpha() is False:
            print("Input cannot contain a number, please try again.")
            second_word = input("Enter second word: \n")

    edit_distance(first_word, second_word)


if __name__ == "__main__":
    main()
