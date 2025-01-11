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

collatz(int(input("Enter a number:")))