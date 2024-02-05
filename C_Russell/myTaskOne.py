def primeNum(list):
   # This is a function that calculates all of the prime numbers from a list
   listOfPrimes = []
   # This variable only needs to be accessed by the function, so it is defined locally
   for num in list: 
       if num >= 2:
           for i in range(2, num):
            # This goes through all the numbers in the range 2 to num minus one (num is the user input)
            # And if the user input (num) has a modulus (remainder) of 0 at any divsion it means it is not a prime number
                if num % i == 0:
                    break
                continue
           else:
                    listOfPrimes.append(num)    
   return listOfPrimes

def calculateStatistics(list):
    # This is a function that uses a list provided by the user to calculate the sum of all the numbers and the mean
    minOfNums = list[0]
    maxOfNums = list[-1]

    sumOfNums = 0
    meanOfNums = 0
    for num in list:
        sumOfNums += num
        continue

    meanOfNums = sumOfNums / len(list)

    return minOfNums, maxOfNums, sumOfNums, meanOfNums

userInput = print("Please enter a number, no letters are allowed. Write stop when you have finished.")

userListOfNumbers = []

while userInput != "STOP":
    # As soon as the user doesn't want to input any more numbers they input stop
    try:
    # The try catch catches any invalid user inputs and continues the loop instead of breaking the code.
        userInput = input("Please enter a number to stop entering numbers enter STOP: ")
        if userInput == "STOP":
            break
        userListOfNumbers.append(int(userInput))
    except ValueError:
        print("Invalid input")
    
    print(userListOfNumbers)

sortedList = userListOfNumbers.sort()
# The code below is executing the functions and displaying all of the results

print("\n\nThis is your list:\t", userListOfNumbers)

minOfNums, maxOfNums, sumOfNums, meanOfNums = calculateStatistics(userListOfNumbers)
listOfPrimeNums = primeNum(userListOfNumbers)

print("The amount of numbers in the list is:\t", len(userListOfNumbers))
print("The sum of your numbers: {} \nAnd the mean of all your numbers is: {}" .format(sumOfNums, meanOfNums))
print("The minimum value of this list is: {} and the maximum of the list is: {}." .format(minOfNums, maxOfNums))
print("Here are all the prime numbers from your list:\t", listOfPrimeNums)
