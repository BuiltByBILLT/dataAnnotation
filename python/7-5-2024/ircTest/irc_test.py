import socket

# IRC configuration
SERVER = "irc.libera.chat"
PORT = 6667
CHANNEL = "#pytest-bots"
NICKNAME = "TestBot-DA"

# Function to send a command to the IRC server
def send_command(irc_socket, command):
    irc_socket.send((command + "\r\n").encode())

# Connect to the IRC server and send a test message
def main():
    try:
        irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Connecting to {SERVER}:{PORT}")
        irc_socket.connect((SERVER, PORT))
        
        send_command(irc_socket, f"NICK {NICKNAME}")
        send_command(irc_socket, f"USER {NICKNAME} 0 * :Test Bot")
        print(f"Joined channel {CHANNEL}")
        send_command(irc_socket, f"JOIN {CHANNEL}")
        
        print(f"Sending message to {CHANNEL}")
        send_command(irc_socket, f"PRIVMSG {CHANNEL} :Hello, this is a test message from TestBot!")
        
        # Listen for server responses for a short period
        irc_socket.settimeout(10)
        while True:
            try:
                response = irc_socket.recv(4096).decode("UTF-8")
                print("Server response: ", response)
                if "PING" in response:
                    send_command(irc_socket, "PONG :" + response.split(":")[1])
            except socket.timeout:
                break

        # Disconnect after sending the message
        send_command(irc_socket, "QUIT")
        irc_socket.close()
        print("Disconnected from server")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
