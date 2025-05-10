#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range (10,0,-1):
        print(i)
    else:
        print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list=[int * int for int in int_list]
    print(int_list)
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i%3 == 0 and i%5 ==0:
           print("FizzBuzz")
        elif i%3 == 0:
         print("Fizz")
        elif i%5 == 0:
         print("Buzz")
        else:
         print(i)
    pass

happy_new_year()
square_integers([1,5,6,8,7,9,3])
fizzbuzz()