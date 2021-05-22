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