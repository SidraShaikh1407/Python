# Aim: Write a Python program to create a simple socket for basic information exchange between server
# Branch: Comps
# Year: SE
# Sem: IV
# Subject: Python
# Name: Sidra Shaikh
# UIN: 231P064
# Roll No: 40

import socket

HOST = '127.0.0.1'
PORT = 12345

try:
    print("Attempting to connect to server...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")

    while True:
        client_message = input("Client: ")
        client_socket.send(client_message.encode())

        if client_message.lower() == "bye":
            print("Closing connection.")
            break

        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

        if data.lower() == "bye":
            print("Server closed the connection.")
            break

    client_socket.close()

except Exception as e:
    print(f"Error: {e}")
