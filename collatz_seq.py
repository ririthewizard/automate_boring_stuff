def collatz(number):

    if number == 1:
        return number
    else:
        if number % 2 == 0:
            number = number // 2
            print(number)
            return collatz(number)
        
        number = 3 * number + 1
        print(number)
        return collatz(number)

try:
    collatz(int(input("Enter a number:")))
except:
    print("You have to enter an integer")
    collatz(int(input("Enter a number:")))