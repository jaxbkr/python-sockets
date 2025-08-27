import socket

serverIP = "10.20.42.237"
serverPort = 4010          
bufferSize = 1024

# Create UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("Type messages to send. Press Ctrl+C to quit.\n")

while True:
    try:
        msg = input("You: ")

        UDPClientSocket.sendto(msg.encode(), (serverIP, serverPort))

        data, addr = UDPClientSocket.recvfrom(bufferSize)
        print("Server:", data.decode().strip())

    except KeyboardInterrupt:
        print("\nClosing client...")
        UDPClientSocket.close()
        break
