'''Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message.
If the score is between 0.0 and 1.0, print a grade'''

def main():
    grade = input('Enter Grade: ')

    try:
        fgrade = float(grade)
    except:
        fgrade = -1

    if fgrade <0.0:
        print('Bad Grade')
    elif fgrade >1.0:
        print('Bad grade')
    elif fgrade >= 0.9 and fgrade <=1.0:
        print('A')
    elif fgrade >= 0.8 and fgrade <= 0.9:
        print('B')
    elif fgrade >= 0.7 and fgrade <= 0.8:
        print('C')
    elif fgrade >= 0.6 and fgrade <= 0.7:
        print('D')
    elif fgrade < 0.6:
        print('F')
    else:
        print('Invalid Input')

if __name__ == '__main__':
    main()