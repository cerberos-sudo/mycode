import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many clients the server can listen to simultaneously
    server_socket.listen(2)  # Allow two clients to connect

    print("Waiting for player 1 to connect...")
    conn1, addr1 = server_socket.accept()  # accept player 1 connection
    print("Player 1 connected: " + str(addr1))

    conn1.send("You are Player 1. Waiting for Player 2 to connect...\n".encode())

    print("Waiting for player 2 to connect...")
    conn2, addr2 = server_socket.accept()  # accept player 2 connection
    print("Player 2 connected: " + str(addr2))

    conn2.send("You are Player 2. Game starts!\n".encode())

    while True:
        # Player 1's turn
        play_game(conn1, conn2, "Player 1")
        
        # Player 2's turn
        play_game(conn2, conn1, "Player 2")

    conn1.close()
    conn2.close()
    server_socket.close()

def play_game(player_conn, opponent_conn, player_name):
    options = ['rock', 'paper', 'scissors']
    
    # Notify player to make a move
    player_conn.send(f"{player_name}, it's your turn. Make a move (rock/paper/scissors): ".encode())
    
    # Receive player's choice
    player_choice = player_conn.recv(1024).decode().strip().lower()

    if player_choice not in options:
        player_conn.send("Invalid choice. Please choose rock, paper, or scissors.\n".encode())
        play_game(player_conn, opponent_conn, player_name)
        return
    
    # Notify opponent of player's choice
    opponent_conn.send(f"{player_name} chooses: {player_choice}\n".encode())
    
    # Wait for opponent's move
    opponent_conn.send("Waiting for opponent's move...\n".encode())
    opponent_choice = opponent_conn.recv(1024).decode().strip().lower()

    if opponent_choice not in options:
        opponent_conn.send("Invalid choice. Please choose rock, paper, or scissors.\n".encode())
        play_game(player_conn, opponent_conn, player_name)
        return
    
    # Notify player of opponent's move
    player_conn.send(f"Opponent chooses: {opponent_choice}\n".encode())
    
    # Determine winner
    if player_choice == opponent_choice:
        player_conn.send("It's a tie!\n".encode())
        opponent_conn.send("It's a tie!\n".encode())
    elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
         (player_choice == 'paper' and opponent_choice == 'rock') or \
         (player_choice == 'scissors' and opponent_choice == 'paper'):
        player_conn.send("You win!\n".encode())
        opponent_conn.send("You lose!\n".encode())
    else:
        player_conn.send("You lose!\n".encode())
        opponent_conn.send("You win!\n".encode())

if __name__ == '__main__':
    server_program()
