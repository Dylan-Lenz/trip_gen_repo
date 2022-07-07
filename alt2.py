# (15): Randomly re-select a destination, restaurant, transportation, or entertainment. 
# (10): Confirm that my day trip is “complete” once I like all of the random selections. 
# (10): Display my completed trip in the console. 

dest_list = ['Beach', 'Zoo', 'Mall', 'Water Park', 'Amusement Park']

for dest_result in dest_list:
    print(f'Would you like to visit the {dest_result} today? y/n?')
    answer = input()
    if answer == 'n':
        print('Understood.')
    elif answer == 'y':
        print(f'Great News!! Have fun at the {dest_result} today!')
        break
        