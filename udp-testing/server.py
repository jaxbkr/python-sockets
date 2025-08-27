import socket

localIP = "10.20.42.237"
localPort = 4010
bufferSize = 1024


msgFromServer = "Hello UDP Client\n"


bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

#listen for incoming datagrams

while(True):
        try:
                message, address = UDPServerSocket.recvfrom(bufferSize)

                clientMsg = "Message from Client:{}".format(message.decode())
                clientIp = "Client IP Address:{}".format(address)

                print(clientMsg)
                print(clientIp)

                UDPServerSocket.sendto(bytesToSend, address)
        except KeyboardInterrupt:
                print("\nClosing server")
                UDPServerSocket.close()
                break

