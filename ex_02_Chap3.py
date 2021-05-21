'''Exercise 2: Rewrite your pay program using try and
except so that your program handles non-numeric input
gracefully by printing a message and exiting the program.'''

def main():
    hour = input('Enter Hours: ')
    rate = input('Enter Rate: ')

    try:
        fhour = float(hour)
    except:
        fhour = -1
    try:
        frate = float(rate)
    except:
        frate = -1

    if fhour <0:
        print('InValid Number')
    elif frate<0:
        print('Invalid Number')
    else:
        if fhour > 40:
            print('Overtime')
            pay = fhour * frate
            otp = (fhour - 40) * (frate * 0.5)
            pay = pay + otp
        else:
            print('Regular')
            pay = fhour * frate

        print('Pay Is: %.2f' % pay)


if __name__ == '__main__':
    main()