# (15): Randomly re-select a destination, restaurant, transportation, or entertainment. 
# (10): Confirm that my day trip is “complete” once I like all of the random selections. 
# (10): Display my completed trip in the console. 

def destinations():
    dest_list = ['Beach', 'Zoo', 'Mall', 'Water Park', 'Amusement Park']
    for dest_result in dest_list:
        print(f'Would you like to visit the {dest_result} today? y/n?')
        answer = input()
        if answer == 'n':
            print('Understood.')
            print('')
        elif answer == 'y':
            print(f'Great News!! Have fun at the {dest_result} today!')
            print('')
            break
destinations()


def transportations():
    trans_list = ['Walk', 'Bike', 'Drive', 'Uber', 'Train']
    for trans_result in trans_list:
        print(f'How would you like to get there? Is today a/an {trans_result} kind of day? y/n?')
        answer = input()
        if answer == 'n':
            print('Understood.')
            print('')
        elif answer == 'y':
            print(f'Great News!! Have fun taking the {trans_result} today!')
            print('')
            break
transportations()

def diners():
    dine_list = ['Ceasars Grill', 'Italian Bistro', 'Irish Pub', 'Toro Cafe', 'Sticky Kitchen']
    for dine_result in dine_list:
        print(f'After the fun day, Would you like to dine at the {dine_result} for dinner? y/n?')
        answer = input()
        if answer == 'n':
            print('Understood.')
            print('')
        elif answer == 'y':
            print(f'Great News!! Have fun dining at the {dine_result} this evening!')
            print('')
            break
diners()

def shows():
    show_list = ['Musical Theatre', 'Live Concert', 'Dancing Ball', 'Sporting Event', 'Movie']
    for show_result in show_list:
        print(f'After Dinner, would you like to experience a {show_result}? y/n?')
        answer = input()
        if answer == 'n':
            print('Understood.')
            print('')
        elif answer == 'y':
            print(f'Great News!! Have fun watching the {show_result} tonight!')
            print('')
            break
shows()