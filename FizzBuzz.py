#Write a method fizz_buzz(max) that takes in a number max and returns an array containing all numbers greater than 0 and less than max that are divisible by either 4 or 6, but not both.
def fizz_buzz(max):
    numbers = []

    for i in range(0, max):
        if(i % 4 == 0 or i % 6 == 0) and not (i % 4 == 0 and i % 6 == 0):
            numbers.append(i)

            i += 1
            print(numbers)
print(fizz_buzz(30))