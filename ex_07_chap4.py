def computegrade(score):
    if score <0.0:
        x = ('Bad Grade')
    elif score >1.0:
        x = ('Bad grade')
    elif score >= 0.9 and score <=1.0:
        x = ('A')
    elif score >= 0.8 and score <= 0.9:
        x = ('B')
    elif score >= 0.7 and score <= 0.8:
        x = ('C')
    elif score >= 0.6 and score <= 0.7:
        x = ('D')
    elif score < 0.6:
        x = ('F')
    else:
        x = ('Invalid Input')

    return print(x)

def main():

    sscore = input('Enter Score: ')
    score = float(sscore)
    computegrade(score)


if __name__ == '__main__':
    main()

