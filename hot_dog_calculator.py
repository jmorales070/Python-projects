# 
# Hot Dog Cookout Calculator
# Calculates the number of packages of hot dogs and buns needed, with the minimum amount of leftovers
# Input(s)
#  people, htd_per_person, htd_per_package, buns_per_package
#
# Output
#  htd_per_package, buns_per_package, required_htd_packages, required_buns_package, leftover_htd, leftover_buns

# User knows what the program does
print('The program calculates the number of packages of hot dogs and hot dog buns needed for a cookout, with the minimum amount of leftovers.')

# Use math function to round up
import math

# User inputs the number of people attending the cookout
people = int(input('Enter the number of people attending the cookout: '))
# User inputs the number of hot dogs each person will be given
htd_per_person = int(input('Enter the number of hot dogs each person will be given: '))
# User inputs the number of hot dogs per hot dog package
htd_per_package = int(input('Enter the number of hot dogs per package: '))
# User inputs the number of hot dog buns per package of buns
buns_per_package = int(input('Enter the number of hot dog buns per package: '))

# Calculate total hot dogs
total_htd = people * htd_per_person
# Calculate the minimum number of packages of hot dogs required
required_htd_packages = math.ceil(total_htd / htd_per_package) # Round up
# Calculate the minimum number of packages of hot dog buns required
required_buns_package = math.ceil(total_htd / buns_per_package) # Round up
# Calculate the number of hot dogs that will be leftover
leftover_htd = (required_htd_packages * htd_per_package) - total_htd
# Calculate the number of hot dog buns that will be leftover
leftover_buns = (required_buns_package * buns_per_package) - total_htd

# Display Cook Out
print()
print('*' * 30)
print('Cookout'.center(30))
print('=' * 30)

# Display Size of Package
print('Size of Package')
print('-' * 30)
print(f'Hot Dogs\t {htd_per_package:>10}') # hot dog
print(f'Hot Dog Buns\t {buns_per_package:>10}') # hot dog buns
print('=' * 30)
# Display Number of Packages
print('Number of Packages')
print('-' * 30)
print(f'Hot Dogs\t {required_htd_packages:>10}')
print(f'Hot Dog Buns\t {required_buns_package:>10}')
print('=' * 30)
# Display Leftovers
print('Leftovers')
print('-' * 30)
print(f'Hot Dogs\t {leftover_htd:>10}')
print(f'Hot Dog Buns\t {leftover_buns:>10}')
print('=' * 30)
print()

# User knows program ended
print('Program ends.')