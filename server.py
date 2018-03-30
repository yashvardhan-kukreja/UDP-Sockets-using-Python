import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = socket.gethostbyname(socket.gethostname())
port = 1269

hostaddress = (ip, port)

server.bind(hostaddress)

while True:
    data, address = server.recvfrom(1024)
    print("Message from client " + address[0] + ":" + str(address[1]) + "- " + data.decode("utf-8"))
    if data == "Bye" or data == "bye":
        server.close()
        break
    message = input("Enter a message for the client: ")
    server.sendto(str.encode(message), address)
    if message == "Bye" or message == "bye":
        server.close()
        break