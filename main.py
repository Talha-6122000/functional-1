from functools import reduce

#1 Capitalize all of the pet names and print the list
def captalize_word(list):
  return list.capitalize()
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(captalize_word,my_pets)))
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
x=list(zip(my_numbers,my_strings))
my_list=sorted(x,reverse=False)
print(my_list)

#3 Filter the scores that pass over 50%
def fiftyPercentMarks(list):
  return (list/100)*100>50


scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(fiftyPercentMarks,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))