def main():
    fhand = open('mbox-short.txt', 'r+')
    fdict = dict()

    for line in fhand:
        if line.startswith('From '):
            fword = line.split()
            #print(fword)
            for i in fword:
                if i != fword[5]:
                    continue
                if i == fword[5]:
                    #print(i)
                    fhour = i.split(':')
                    #print(fhour)

            for i in fhour:
                if i == fhour[0]:
                    fdict[i] = fdict.get(i, 0) + 1
    flist = []

    for k,v in fdict.items():
        ntup = (k,v)
        flist.append(ntup)
        #print(flist)
    flist = sorted(flist,reverse=True)
    #print(flist)

    for k,v in flist:
        fdict[k] = fdict.get(k,v)

    #print(fdict)

    for key in fdict:
        print (key, fdict[key])



if __name__ == '__main__':
    main()