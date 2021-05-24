def main():
    fhand = open('mbox-short.txt','r+')
    counter = 0

    for line in fhand:
        if line.startswith('From '):
            counter = counter+1
            fword = line.split()
            print(fword[1])

    print('There are %d Lines With From'%counter)

if __name__ == '__main__':
    main()
