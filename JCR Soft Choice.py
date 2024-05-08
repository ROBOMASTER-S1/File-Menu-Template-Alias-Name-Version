# J.C.R Soft~Choice File Menu Python program alias name version example:

# Created by Joseph C. Richardson, GitHub.com

# You will need to import your own files to correctly make this Python
# file menu program example work. You can also use some of my program
# examples to create a working Python file menu of your very own. I
# created this file menu and its files associated with it, using def
# functions(). This Python file menu example shows how to create modules
# and how to import them into your very own file menu. Note: you must
# store all your files within the very same folder you create your file
# menu in. If you don't do such, the file menu won't be able to find the
# files you want in your file menu.

import os,time,math
from Ascii_Code_Translator import ascii_codes as characters # as alias name
from Majestic_Calculator import maj_cal as calculator # as alias name
from Grocery_List_Creator import items_list as shopping_cart # as alias name
from Fantastique_Plastique import fan_plast as plastic_mix # as alias name
from Ontario_Lotto_649 import ont_lotto as good_luck # as alias name
from Typewriter_Game import type_game as learn_typing_skills # as alias name
from Know_Your_Polygons import kyp as shapes # as alias name

text_features=(
    'cls', # index 0 = clear screen
    ' '*45, # index 1 = 45 spaces
    '*'*118, # index 2 = 118 asterisks
    '\x1b[31m', # index 3 = red
    '\x1b[32m', # index 4 = green
    '\x1b[33m', # index 5 = yellow
    '\x1b[34m', # index 6 = blue
    '\x1b[37m'  # index 7 = white
    )

text_words=(
    f'\n{text_features[1]}{text_features[5]}J.C.R \
Soft{text_features[4]}~{text_features[5]}Choice', # index 0 = text_words

    f'\n{text_features[4]}{text_features[2]}', # index 1 = text_words

    f'\n{text_features[5]}To open a choice, press any one of \
the selected number keys below, then press \
({text_features[3]}ENTER{text_features[5]}) to confirm.', # index 2 = text_words

    f'\n({text_features[4]}1{text_features[5]}): ASCII CODE \
TRANSLATOR', # index 3 = text_words

    f'\n({text_features[4]}2{text_features[5]}): Majestic Calculator', # index 4 = text_words

    f'\n({text_features[4]}3{text_features[5]}): Grocery List Creator', # index 5 = text_words

    f'\n({text_features[4]}4{text_features[5]}): FANTASTIQUE \
PLASTIQUE Easy Mix Converter', # index 6 = text_words

    f'\n({text_features[4]}5{text_features[5]}): ONTARIO LOTTO \
6/49 RANDOM NUMBER GENERATOR', # index 7 = text_words

    f'\n({text_features[4]}6{text_features[5]}): Typewriter Game', # index 8 = text_words

     f'\n({text_features[4]}7{text_features[5]}): Know Your Polygons', # index 9 = text_words

    f'\nPress ({text_features[3]}Q{text_features[5]}) to \
exit J.C.R Soft~Choice.' # index 10 = text_words
    )

text_info=(
    f'\n{text_features[3]}READY:{text_features[4]} ', # index 0 = text_info

    f'\n{text_features[5]}Thanks for choosing J.C.R Soft~Choice.' # index 1 = text_info
    )

choice=('1','2','3','4','5','6','7','q') # choices, q = quit

os_title=('title J.C.R Soft~Choice')

def file_menu():
    os.system(os_title)

    while True:
        os.system(text_info[0])
        os.system(text_features[0])
        for i in text_words:
            print(i)

        button=input(text_info[0]).lower().strip()

        if button==(choice[0]):
            characters()
        elif button==(choice[1]):
            calculator()
        elif button==(choice[2]):
            shopping_cart()
        elif button==(choice[3]):
            plastic_mix()
        elif button==(choice[4]):
            good_luck()
        elif button==(choice[5]):
            learn_typing_skills()
        elif button==(choice[6]):
            shapes()
        elif button==(choice[7]):
            os.system(text_features[0])
            print(text_info[1])
            time.sleep(3)
            break

file_menu()
