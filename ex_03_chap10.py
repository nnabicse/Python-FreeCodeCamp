def main():
    fhand = open('mbox-short.txt','r+')

    fread = fhand.read()
    flower = fread.lower()
    print(flower)

    counter = 0

    for i in flower:
        if i.isalpha():
            counter+=1

    print(counter)

if __name__ == '__main__':
    main()