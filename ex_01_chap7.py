def main():

    fhand = open('mbox-short.txt', 'r+')

    read = fhand.read()

    print(read.upper())

if __name__ == '__main__':
    main()