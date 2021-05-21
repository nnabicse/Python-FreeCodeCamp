'''Exercise 1: Rewrite your pay computation to
give the employee 1.5 times the hourly rate
for hours worked above 40 hours.'''

def main():

    hour = input('Enter Hours: ')
    rate = input('Enter Rate: ')

    if float(hour)>40:
        print('Overtime')
        pay = float(hour) * float(rate)
        otp = (float(hour)-40)*(float(rate)*0.5)
        pay = pay+otp
    else:
        print('Regular')
        pay = float(hour)*float(rate)

    print('Pay Is: %.2f'%pay)
    
if __name__ == '__main__':
    main()