import random


destinations = ['Minneapolis','Madison','Milwaukee','Lacrosse','Green Bay','Marquette', 'Hudson']
restaurants = ['a Barbeque','an Italian',' an Asian','an American','a family','a Greek',]
modes_of_transportation = ['driving','a helicopter ride','the train','Horse and Buggy', 'motorcycle' ]
forms_of_entertainment = ['going to a play','seeing a sporting event','going to a concert','hiking','starting an uprising']

#randomizer for selecting from lists
def random_generator(list):
    result = random.choice(list)
    return result
    
# Variables to be used in 
random_destination = random_generator(destinations)
random_restaurant = random_generator(restaurants)
random_transportation = random_generator(modes_of_transportation)
random_entertainment = random_generator(forms_of_entertainment)

question = 'Are you satisfied with the choices given? (y/n)'

# menu options will allow you to select a new random from each list.
def menu_options():
        options = ('Enter 1 for different destination\n'
                'Enter 2 for different restaurant\n'
                'Enter 3 for different transportation\n'
                'Enter 4 for different entertainment\n'
                'Enter 5 to confirm : ')
        choice = input(options)
        return int(choice)
# main menu required to set paramaters for change in desired trip

def main_menu(destination, restaurant, transportation, entertainment):
    user_confirmed = False
    while user_confirmed == False:
        choice = menu_options()
        if choice == 1:
            destination = random_generator(destinations)
            print(f'{destination} will be your new destination')
        elif choice == 2:
            restaurant = random_generator(restaurants)
            print(f'{restaurant} will be your new restaurant.') 
        elif choice == 3:
            transportation = random_generator(modes_of_transportation)
            print(f'{transportation} will be your new means of transportation.') 
        elif choice == 4:
            entertainment = random_generator(forms_of_entertainment)
            print(f'{entertainment} will be your new entertainment for the night.') 
        elif choice == 5:
            print('We are glad you are happy with the choices provided.')
            print(f'Congratulations you will be headed to {destination} by means of {transportation}. During your trip you will be eating at {restaurant} restaurant, and you will be {entertainment}.')
            user_confirmed = True
            return 

# make this ito a funciton 
# will be easier to call and run it when we want
def here_or_there(): #function made to direct pathways I want taken needs to be at the end of the code or will automatically run everything after.
    desired_trip = f'Congratulations you will be headed to {random_destination} by means of {random_transportation}. During your trip you will be eating at {random_restaurant} restaurant, and you will be {random_entertainment}.'
    print(desired_trip)
    isSatisfied = False          #default variable has to be equal to while loop so that it can enter 
    while isSatisfied == False: 
        satisfied = input(question)  #secondary variable is needed to be able to switch the value of default variable
        if satisfied == 'y': #this pathway skips the menu and takes you to a final message
            isSatisfied = True #flips the default variable so that you can exit function
            print('We are happy to hear we could help!')
            print(f'Again, {desired_trip} We look forward to your business in the future.')
        elif satisfied == 'n': #this pathway takes you to the menu system.
            print('We are sorry to hear, is there something you would like to change?')
            main_menu(random_destination, random_restaurant, random_transportation, random_entertainment)
        return isSatisfied
  
here_or_there()
