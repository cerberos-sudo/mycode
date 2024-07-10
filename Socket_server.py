import socket
import random

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
        
        if data == "Lets Play!":
            play_game(conn)
        else:
            conn.send("Type 'Lets Play!' to start the game.\n".encode())

    conn.close()  # close the connection

def play_game(conn):
    options = ['rock', 'paper', 'scissors']

    while True:
        # Server's choice
        server_choice = random.choice(options)
        conn.send("Server is ready. Your move (rock/paper/scissors): ".encode())
        
        # Receive player's choice
        client_choice = conn.recv(1024).decode().strip().lower()

        if client_choice not in options:
            conn.send("Invalid choice. Please choose rock, paper, or scissors.\n".encode())
            continue
        
        conn.send(f"Server chooses: {server_choice}\n".encode())

        # Determine winner
        if client_choice == server_choice:
            conn.send("It's a tie!\n".encode())
        elif (client_choice == 'rock' and server_choice == 'scissors') or \
            (client_choice == 'paper' and server_choice == 'rock') or \
            (client_choice == 'scissors' and server_choice == 'paper'):
            conn.send("You win!\n".encode())
        else:
            conn.send("Server wins!\n".encode())
        
        break  # Exit the game loop after one round

if __name__ == '__main__':
    server_program()
