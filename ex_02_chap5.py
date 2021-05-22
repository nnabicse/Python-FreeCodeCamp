'''Write another program that prompts for a list of numbers as above and at 
the end prints out both the maximum and minimum of the numbers'''

def main():
    list = []
    c = int(input('How many Elements To Input: '))

    for i in range (c):
        e = int(input('Enter %dth Elements: '%c))
        list.append(e)
        c-=1

    print('List: ',list)
    print('Max Value: ',max(list))
    print('Min Value: ',min(list))



if __name__ == '__main__':
    main()
