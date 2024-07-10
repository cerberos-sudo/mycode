import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        
        print("from connected user: " + str(data))
        print("Type, Lets Play! to start the game.")
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
        if data == "Lets Play!"
            play_game(client_socket)            

    def play_game(client_socket):
    options = ['rock', 'paper', 'scissors']
    print(client_choice)    
    while True:
        # Receive player's choice
        client_choice = client_socket.recv(1024).decode().strip().lower()

    if client_choice not in options:
        client_socket.send("Invalid choice. Please choose rock, paper, or scissors.\n".encode())
        

        # Server's choice
    import random
    server_choice = input("Your move: ")
    client_socket.send(f"Server chooses: {server_choice}\n".encode())

        # Determine winner
    if client_choice == server_choice:
        client_socket.send("It's a tie!\n".encode())
    elif (client_choice == 'rock' and server_choice == 'scissors') or \
        (client_choice == 'paper' and server_choice == 'rock') or \
        (client_choice == 'scissors' and server_choice == 'paper'):
        client_socket.send("You win!\n".encode())
    else:
        client_socket.send("Server wins!\n".encode())
   
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
