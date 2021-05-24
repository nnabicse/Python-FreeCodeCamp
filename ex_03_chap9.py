def main():
    fhand = open('mbox-short.txt','r+')
    fdict = dict()

    for line in fhand:
        if line.startswith('From '):
            fword = line.split()
            for i in fword:
                if i != fword[1]:
                    continue
                if i == fword[1]:
                    fdict[i] = fdict.get(i,0)+1

    print(fdict)


if __name__ == '__main__':
    main()