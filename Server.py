from socket import * # importations
import time
import threading

# Distinct server port
serverPort = 11500
MAXCLIENT = 3
currClients = 0
clientCount = 0
CacheInfo = {}

def getFileList():

    return fileList

# Handle multiple clients
def multipleClient(connectionSocket, address, clientName):
    global currClients

    # Send the client their assigned name(s)
    if currClients <= MAXCLIENT:
        connectionSocket.send(clientName.encode())

    # Receives and responds to client messages
        while True:
            sentence = connectionSocket.recv(1024).decode()

            if not sentence:
                break

            print(f"Received from {clientName}: {sentence}")

            # If client types exist, disconnect them
            if sentence.lower() == "exit":
                print("You have been disconnected.")
                break

            response = f"Server Response: {sentence} ACK"
            connectionSocket.send(response.encode())

    # After client disconnects, subtract current client value by 1
    connectionSocket.close()
    currClients -= 1

# Set up server pocket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(MAXCLIENT)
print("Server is ready")

# Loop to accept client connection
while True:
    try:
        connectionSocket, address = serverSocket.accept()

        if currClients >= MAXCLIENT:
            print(f"Connection from {address} rejected: server full.")
            connectionSocket.send("SERVER_FULL".encode())
            connectionSocket.close()
            continue
        currClients += 1
        clientCount += 1
        
        # Assign client names
        clientName = f"Client{clientCount}"
        print(f"Client {clientCount} connected from {address}. Active clients: {currClients}")

        # Start a new thread
        clientThread = threading.Thread(target=multipleClient, args = (connectionSocket, address, clientName))
        clientThread.start()

    except KeyboardInterrupt:
        print("The server is down!")
        break

serverSocket.close()