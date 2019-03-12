'''
Aa program that displays the 
first 50 prime numbers in descending order. 
Uses a stack to store prime numbers.
'''

class Stack:
    def __init__(self):
        self.__elements = []

    # Return true if the tack is empty
    def isEmpty(self):
        return len(self.__elements) == 0

    # Returns the element at the top of the stack
    # without removing it from the stack.
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(elements) - 1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)


stack = Stack()
NUMBER_OF_PRIMES = 50 # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
count = 0  # Count the number of prime numbers
number = 2 # A number to be tested for primeness

print("The first 50 prime numbers in reverse are:")
print()

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    isPrime = True # Is the current number prime?

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, the number is not prime
            isPrime = False # Set isPrime to false
            break  # Exit the for loop
        divisor += 1

    # Display the prime number and increase the count
    if isPrime:
        count += 1 # Increase the count
        stack.push(number) # Store it in the stack

    # Check if the next number is prime
    number += 1


while not stack.isEmpty():
    print(stack.pop(), end=" ") # print numbers using pop function (to display in reverse)
