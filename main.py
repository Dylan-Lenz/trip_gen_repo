
# Suffix Key:
# _ans = answer
# _sel = select
# _opt = option
# _lst = list
# _ch  = choice

import random

dest_lst = ['Beach', 'Zoo', 'Golf Course', 'Water Park', 'Amusement Park']
trans_lst = ['Walk', 'Bike', 'Drive', 'Uber', 'Train']
dine_lst = ['Ceasars Grill', 'Italian Bistro', 'Irish Pub', 'Toro Cafe', 'Sticky Kitchen']
show_lst = ['Live Musical Theatre', 'Live Concert', 'Wrestling Match', 'Sporting Event', 'Movie']

def greet():
    print('')
    print('Welcome to your Personal-Pocket-Planner.') 
    print('Where everything is handled by us, for you.') 
    print('')
    print('Your only responsiblity, choose how you would like to have fun.')
    print('We will provide you with plans for the day, dinner, and a show.')
    print('As well as arrange all accomodations necassary while giving you one convenient place to pay.')
    print('When you are ready, please make your first selection.')
    print('')

def dest_sel():
   for dest_ans in random.choices(dest_lst):
        dest_opt = input(f'Would you like to visit the {dest_ans} today? y/n? :')
        if dest_opt == 'y':
            print(f'Great Choice!! Have fun visiting the {dest_ans} today!')
            return dest_ans
        else:
            print('Let us try again...')
            print('')
            dest_sel()

def trans_sel():
    for trans_ans in random.choices(trans_lst):
        trans_opt = input(f'How would you like to get there? Is today a/an {trans_ans} kind of day? y/n? :')
        if trans_opt == 'y':
            print(f'Great Choice!! Have fun taking the {trans_ans} today!')
            return trans_ans
        else:
            print('Let us try again...')
            print('')
            trans_sel()

def dine_sel():
    for dine_ans in random.choices(dine_lst):
        dine_opt = input(f'After the fun day, Would you like to dine at the {dine_ans} for dinner? y/n? :')
        if dine_opt == 'y':
            print(f'Great Choice!! Have fun dining at the {dine_ans} this evening!')
            return dine_ans
        else:
            print('Let us try again...')
            print('')
            dine_sel()

def show_sel():
    for show_ans in random.choices(show_lst):
        show_opt = input(f'After Dinner, would you like to experience a {show_ans}? y/n? :')
        if show_opt == 'y':
            print(f'Great Choice!! Have fun watching the {show_ans} tonight!')
            return show_ans
        else:
            print('Let us try again...')
            print('')
            show_sel()

def trip_sel():
    greet()
    dest_ch = dest_sel()
    print('')
    trans_ch = trans_sel()
    print('')
    dine_ch = dine_sel()
    print('')
    show_ch = show_sel()
    print('')
    trip_lst = [dest_ch, trans_ch, dine_ch, show_ch]
    print('Your Request Has been submitted.')
    print('')
    print(f'Your plan for today is to take the {trans_ch} to the {dest_ch}.')
    print(f'Then this evening, you will dine at The World Famous {dine_ch} and then watch a {show_ch}.')
    print('')
    for i in trip_lst:
        trip_opt = input('Would you like to finalize your plan for today? y/n? :')
        if trip_opt == 'y':
            print('Great Choices!! Have fun!')
            return i
        else:
            print('')
            print('Let us start over...')
            trip_sel()

trip_sel()

