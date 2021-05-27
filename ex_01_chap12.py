def main():
    import socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    url = input('Enter URL: ')
    for i in url:
        domain = url.split('/')
        try:
            for x in domain:
                if x == domain[2]:
                    # print(x)
                    sdomain = x
                    sock.connect((sdomain, 80))
                    command = ('GET' + url + ' HTTP/1.0\r\n\r\n').encode()
                    print(command)
                    sock.send(command)
                    while True:
                        data = sock.recv(512)
                        if len(data) < 1:
                            break
                        print(data.decode())
                    sock.close()
                elif x != domain[2]:
                    continue
                    # print(sdomain)
            break
        except:
            print('Invalid Imput')
        break

if __name__ == '__main__':
    main()