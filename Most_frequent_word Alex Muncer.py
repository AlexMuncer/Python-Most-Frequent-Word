# Author : Alex Muncer
# Date : 02/12/2021
# 
# 
# This program takes a list containing values (words) and outputs the most occoring value.
# If multiple values (words) occor the same amount of times, it will output the the value (word) with the latest first occorence in the list. 
# This has a quadratic aka O(n^2) Time complexity.
#
# Parameter "n" of the function "most_frequent_word" is the list of values (words) to be checked. Note there is no type checking and assumes input is a list of strings.
# Prints either error of empty array or the most frequent value (word).
#
# Variable "most_word" is the most occorinf value in the list.
# variable "max_frequency" is the number of times the "mostWord" has occored.
# vairable "current_frequency" is the number of times the currently selected value has occored in the list.
#
# e.g.  most_frequent_word([]) = Error: empty array.
#       most_frequent_word([1,2,3,4,5,4,3,5,4,3,2,"cheese","green","cheese"]) = Most frequent word is: 3 . Occurrences: 3 .
#       most_frequent_word(["purple","cheese", "and","toast", "water"]) = Most frequent word is: water . Occurrences: 1 .
#       most_frequent_word(['purple','chess','purple', 'welcome','chess','welcome']) = Most frequent word is: welcome . Occurrences: 2 .
#       most_frequent_word(['coffee','coffee','abc','abc', 'hello', 'hello', 'welcome']) = Most frequent word is: hello . Occurrences: 2 .
#       most_frequent_word(['purple','and', 'and','toast', 'water','purple','purple']) = Most frequent word is: purple . Occurrences: 3 .

def most_frequent_word(n):
    length = len(n)
    if length == 0: # This is a sanity check to see if there is anything in the array.
        print("Error: empty list.") # O(1) operation.
        return

    most_word = '' # this will be the most occoring word. O(1) operation.
    max_frequency = 0 # amount of occorences for the most occoring word. O(1) operation.
    
    for i in range(0,length): #select and assess every word in a list. O(n) operation. 
        current_frequency = 0 #reset the current amount of occorences to 0.  O(1) operation.
        
        for j in range(0,length): # compare every othor word in the list to the current word being assessed. O(n) operation.
            if n[i] == n[j]: # if the current word being assessed matches another word in the list.
                current_frequency = current_frequency + 1 # add 1 to the current frequency variable. O(1) operation.
                
#check if the current word being assessed has occored more times than the max occoring word
        if current_frequency >= max_frequency: 
            most_word = n[i] #if it has update the most occoring word. O(1) operation.
            max_frequency = current_frequency # update the max frequency to the current frequency. O(1) operation. 

            
    print("Most frequent word is:", most_word,". Occurrences:",max_frequency,".")# O(1) operation.
    return
                   


most_frequent_word([])
most_frequent_word([1,2,3,4,5,4,3,5,4,3,2,"cheese","green","cheese"])
most_frequent_word(["purple","cheese", "and","toast", "water"]) # water
most_frequent_word(['purple','chess','purple', 'welcome','chess','welcome']) # welcome
most_frequent_word(['aa','bb','cc','dd','aa','bb','cc','dd']) # dd
most_frequent_word(['purple','cheese', 'toast','toast', 'water']) # toast
most_frequent_word(['coffee','coffee','abc','abc', 'hello', 'hello', 'welcome']) # hello
most_frequent_word(['purple','and', 'and','toast', 'water']) # and
most_frequent_word(['purple','and', 'and','toast', 'water','purple','purple']) # purple


