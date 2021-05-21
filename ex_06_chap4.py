'''Rewrite your pay computation with time-and-a-half
for overtime and create a function called computepay
which takes two parameters (hours and rate).'''

def computepay(hour, rate):
    if float(hour) > 40:
        print('Overtime')
        pay = float(hour) * float(rate)
        otp = (float(hour) - 40) * (float(rate) * 0.5)
        pay = pay + otp
    else:
        print('Regular')
        pay = float(hour) * float(rate)

    print('Pay Is: ',pay)
    return pay

def main():
    hour = input('Enter Hours: ')
    rate = input('Enter Rate: ')

    computepay(hour,rate)

if __name__ == '__main__':
    main()
