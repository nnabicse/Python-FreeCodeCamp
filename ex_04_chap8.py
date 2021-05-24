def main():

    fhand = open('romeo.txt','r+')
    fread = fhand.read()

    flist = fread.split()
    print(len(flist))
    print(flist)

    flist.sort()
    print(flist)

    for x in flist:
        if flist.count(x)>1:
            flist.remove(x)

    flist.sort()

    print(flist)

if __name__ == '__main__':
    main()