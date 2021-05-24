def main():
    fhand = open('mbox-short.txt', 'r+')
    fdict = dict()

    for line in fhand:
        if line.startswith('From '):
            fword = line.split()
            for i in fword:
                if i != fword[1]:
                    continue
                if i == fword[1]:
                    fdict[i] = fdict.get(i, 0) + 1

    rlist = []

    for k,v in fdict.items():
        ntup = (v,k)
        rlist.append(ntup)

    rlist = sorted(rlist,reverse=True)
    #print(rlist)

    flist = {}

    for v,k in rlist:
        flist[k] = flist.get(k,v)

    #print(flist)

    max = 0

    for key in flist:
        if flist[key]>max:
            max = flist[key]


    for key in flist:
        if flist[key] == max:
            print(key, max)

if __name__ == '__main__':
    main()