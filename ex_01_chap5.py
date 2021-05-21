'''Write a program which repeatedly reads numbers
until the user enters "done". Once "done" is entered,
print out the total, count, and average of the numbers.
If the user enters anything other than a number,
detect their mistake using try and except and print an
error message and skip to the next number.'''

def main():

    counter=0
    total = 0.0

    while True:
        number = input('Enter Number: ')

        if number == 'done':
            break

        try:
            fnumber = float(number)
        except:

            print('Invalid Input')
            continue

        if fnumber >=0:
            total = total + fnumber
            counter = counter+1

    avarage = total/counter
    print(total, counter, avarage)

if __name__ == '__main__':
    main()
