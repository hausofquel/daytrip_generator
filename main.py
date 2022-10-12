# As a developer, I want to make at least 3 commits with descriptive messages.
# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.
# As a user, I want a destination to be randomly selected for my day trip.
# As a user, I want a restaurant to be randomly selected for my day trip.
# As a user, I want a mode of transportation to be randomly selected for my day trip.
# As a user, I want a form of entertainment to be randomly selected for my day trip.
# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections.
# As a user, I want to display my completed trip in the console.
#As a developer, I want all of my locations to have a single responsibility. Remember each funtion must do one thing.


#List of Destinations, restaurants, transportation, and entertainment to be randomized.

destinations_list = ["Los Angeles, California" , "Houston, Texas" , "Miami, Florida" , "Sedona, Arizona" , "Boise,Idaho"]

restaurant_list = ["TACOS GALORE" , "Steak-Steak-Steak" , "Bolive Barden" , "Benny's" , "Tempura Takeover"]

transportation_list = ["Uber" , "Taxi Cab" , "Walk" , "E-BIKE" , "Horse-Back"]

entertainment_list = ["Karaoke" , "Jet Ski" , "4x4" , "Surfing" , "Snorkeling for Sea Shells by the Seashore"] 

import random

#randomizer

destination = random.choice(destinations_list)
restaurant = random.choice(restaurant_list)
transportation = random.choice(transportation_list)
entertainment = random.choice(entertainment_list)

day_trip = (f'{destination} , {restaurant} , {transportation} , {entertainment}')

print(day_trip)
confirm_choice = input("Enter 'y' or 'n' to confirm your trip, 'y' if you are happy with selections made or 'n' if you would like to randomize step by step. ")

#if the user is not happy with their trip they are given the opportunity to re select3

def new_dest(confirm_choice):
  while confirm_choice != 'y':
    destination = random.choice(destinations_list)
    confirm_choice = input(f'New destination selected: {destination}! Would you like to proceed? ')
  else:
    print(f'Destination selected: {destination}! ')

new_dest(confirm_choice)

def new_restaurant(confirm_choice):  
  while confirm_choice != 'y':
    restaurant = random.choice(restaurant_list)
    confirm_choice = input(f'New restaurant selected: {restaurant}! Would you like to proceed? ')
  else:
    print(f'Restaurant selected: {restaurant}! ')

new_restaurant(confirm_choice)

def new_trans(confirm_choice):  
  while confirm_choice != 'y':
    transportation = random.choice(transportation_list)
    confirm_choice = input(f'New mode of transportation selected: {transportation}! Would you like to proceed? ')
  else:
    print(f'Transporation selected: {transportation}! ')

new_trans(confirm_choice)

def new_entertainment(confirm_choice):  
  while confirm_choice != 'y':
    entertainment = random.choice(entertainment_list)
    confirm_choice = input(f'New entertainment selected: {entertainment}! Would you like to proceed? ')
  else:
    print(f'Entertainment selected: {entertainment}! ')

new_entertainment(confirm_choice)

print("Enjoy your trip!" )
