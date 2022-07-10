
dest_list = ['Beach', 'Zoo', 'Mall', 'Water Park', 'Amusement Park']
trans_list = ['Walk', 'Bike', 'Drive', 'Uber', 'Train']
dine_list = ['Ceasars Grill', 'Italian Bistro', 'Irish Pub', 'Toro Cafe', 'Sticky Kitchen']
show_list = ['Musical Theatre', 'Live Concert', 'Dancing Ball', 'Sporting Event', 'Movie']

def greet():
    print('')
    print('Welcome to your Personal-Pocket-Planner.') 
    print('Where everything is handled by us, for you.') 
    print('')
    print('Your only responsiblity, choose how you would have fun.')
    print('We will provide you with plans for the day, dinner, and show.')
    print('As well as arrange all accomodations necassary, and give you one convenient place to pay.')
    print('When you are ready, please make your first selection.')
    print('')
greet()

def destination():
    for dest_result in dest_list:
        print(f'Would you like to visit the {dest_result} today? y/n?')
        answer = input()
        if answer == 'n':
            print('Aplogies.')
        elif answer == 'y':
            print(f'Great Choice!! Have fun at the {dest_result} today!')
            print('')
            break

def transportaion():
    for trans_result in trans_list:
        print(f'How would you like to get there? Is today a/an {trans_result} kind of day? y/n?')
        answer = input()
        if answer == 'n':
            print('Aplogies.')
        elif answer == 'y':
            print(f'Great Choice!! Have fun taking the {trans_result} today!')
            print('')
            break

def dining():
    for dine_result in dine_list:
        print(f'After the fun day, Would you like to dine at the {dine_result} for dinner? y/n?')
        answer = input()
        if answer == 'n':
            print('Aplogies.')
        elif answer == 'y':
            print(f'Great Choice!! Have fun dining at the {dine_result} this evening!')
            print('')
            break

def show():
    for show_result in show_list:
        print(f'After Dinner, would you like to experience a {show_result}? y/n?')
        answer = input()
        if answer == 'n':
            print('Aplogies.')
        elif answer == 'y':
            print(f'Great Choice!! Have fun watching the {show_result} tonight!')
            print('')
            break

result_list = [dest_result, trans_result, dine_result, show_result]

for i in result_list:
    print(f'You have made some wonderful choices.') 
    print(f'Your plan is to take the {trans_result} to the {dest_result}.')
    print(f'After that you will dine at {dine_result}, then watch a {show_result}.')
    print('')
    print('If you confirm these plans, please choose y/n.')
    answer = input()
    if answer == 'n':
        print('Aplogies. Let us try again.')
    elif answer == 'y':
        print(f'Awesome!! Have fun! Glad we could Help.')
        print('')
        break

dest_lst = ['Beach', 'Zoo', 'Mall', 'Water Park', 'Amusement Park']

def dest_sel():
    for dest_ans in dest_lst:
        dest_opt = input(f'Would you like to visit the {dest_ans} today? y/n? :')
        if dest_opt == 'y':
            print(f'Great Choice!! Have fun at the {dest_ans} today!')
            return dest_ans
        else:
            print('Let us try again...')

dest_ch = dest_sel()
trip_lst = [dest_ch]