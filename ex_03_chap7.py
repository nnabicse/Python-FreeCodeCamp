def main():
    fname = input('Enter File name: ')
    try:
        if fname == 'na na boo boo':
            print('NA NA BOO BOO TO YOU - You have been punkd!')
            exit()
        fhand = open(fname,'r+')

    except FileNotFoundError:
        print('File Not Found')
        exit()

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