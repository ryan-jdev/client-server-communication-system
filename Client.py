from socket import * # import socket
serverName = 'localhost'
serverPort = 11500

# 1. Create the TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# 2. Try connecting to the server
try:
    clientSocket.connect((serverName, serverPort))

except ConnectionRefusedError:
    print("Could not connect to the server.");
    exit()

# 3. Automatically assign a random incremental name
clientName = clientSocket.recv(1024).decode()

if not clientName:
    print("Could not connect: Server is full.")
    clientSocket.close()
    exit()

print(f"You are assigned as: {clientName}")

# Indefinite loop
while True:
    message = input("> ")
    clientSocket.send(message.encode())

    if message.lower() == "exit":
        print("Disconnected.")
        break

    # 5. Receive information, and print the server reply
    try:
        response = clientSocket.recv(1024).decode()
        print(response)

    except:
        print("Connection lost.")
        break

# Cut off connection
clientSocket.close()
print("Connection closed.")



