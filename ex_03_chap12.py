def main():
    import urllib.request, urllib.parse, urllib.error
    url = input('Enter URL: ')
    count = 0
    fc = 0

    fhand = urllib.request.urlopen(url)

    for line in fhand:
        file = line.decode().strip()
        count = count+1
        print(file)
        if len(file) < 1 or count >= 3000:
            break
    for x in fhand:
        final = x.decode()
        for x in range (len(final)):
            fc = fc+1
    print(fc)

if __name__ == '__main__':
    main()