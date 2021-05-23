def main():
    fname = input('Enter File name: ')
    fhand = open(fname,'r+')

    string = 'X-DSPAM-Confidence:'
    count = 0
    sum = 0

    for line in fhand:
        if not line.startswith(string):
            continue
        else:
            count = count+1
            num = float(line[len(string):])
            sum = sum+num

    print(sum)

if __name__ == '__main__':
    main()


