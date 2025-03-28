import tkinter as tk
import socket

# Define the IP address and port number for the server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888

# Connect to the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((SERVER_IP, SERVER_PORT))

# Receive a message from the server confirming the connection
message = server_socket.recv(1024).decode()
print(f"{message}")

# Define function to send move to the server


def send_move(move, round_num):
    # Send the move to the server
    server_socket.sendall(move.encode())

    # Receive the winner of the round from the server and update the label
    round_winner = server_socket.recv(1024).decode()
    result_label.config(text=f'Round {round_num}: {round_winner}')


# Create the GUI window
window = tk.Tk()
window.title('Rock Paper Scissors Game')

# Set the window size and background color
window.geometry('400x300')
window.configure(background='#f39c12')

# Add a title label
title_label = tk.Label(window, text='Rock Paper Scissors Game', font=(
    'Arial', 24), pady=20, bg='#f39c12', fg='white')
title_label.pack()

# Add a welcome label
welcome_label = tk.Label(window, text='Welcome player to the game!', font=(
    'Arial', 14), pady=10, bg='#f39c12', fg='white')
welcome_label.pack()

# Add rock button
rock_button = tk.Button(window, text="Rock", font=('Arial', 14), bg='#34495e',
                        fg='white', padx=20, pady=10, command=lambda: send_move('Rock', 1))
rock_button.pack()

# Add paper button
paper_button = tk.Button(window, text="Paper", font=(
    'Arial', 14), bg='#34495e', fg='white', padx=20, pady=10, command=lambda: send_move('Paper', 2))
paper_button.pack()

# Add scissors button
scissors_button = tk.Button(window, text="Scissors", font=(
    'Arial', 14), bg='#34495e', fg='white', padx=20, pady=10, command=lambda: send_move('Scissors', 3))
scissors_button.pack()

# Add a label to display the result of each round
result_label = tk.Label(window, font=('Arial', 14),
                        pady=10, bg='#f39c12', fg='white')
result_label.pack()

# Start the GUI event loop
window.mainloop()

# Close the socket
server_socket.close()
