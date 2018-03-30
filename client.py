import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = socket.gethostbyname(socket.gethostname())
port = 1269

hostaddress = (ip, port)

client.connect(hostaddress)

while True:
    message = input("Enter a message to the server: ")
    if message == "Bye" or message == "bye":
        client.close()
        break
    client.sendto(str.encode(message), hostaddress)
    data, address = client.recvfrom(1024)
    print("Message from server: " + data.decode("utf-8"))
    if data == "Bye" or data == "bye":
        client.close()
        break
