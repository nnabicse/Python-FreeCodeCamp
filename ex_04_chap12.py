def main():
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl
    count = 0

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL: ')
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tsearch = input('Enter Tag: ')
    tags = soup(tsearch)
    for tag in tags:
        count = count+1
    print(count)
        #print(tag.get('a'))

if __name__ == '__main__':
    main()