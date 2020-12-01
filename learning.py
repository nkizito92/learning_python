# module for random
import random
print(random.randrange(10,50))

name = "Kizito"
len(name)
# Created a FizzBuzz function in Python
def fizzBuzz(num):
    for x in range(1,num+1):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else: 
            print(x)

fizzBuzz(30)



arr = [1,5,8,9]
obj ={ "name":"kizito", "age":4}
type(arr)
type(obj)
def little_func(name):
    print(name + " is my name!")


# calling the function giving it an string for an
# argument!!
little_func("Kizito")
