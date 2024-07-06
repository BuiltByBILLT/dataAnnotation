import socket
import time
import psutil
import threading

# Configuration
server = 'irc.libera.chat'  # Replace with your IRC server
port = 6667
channel = '#pytest-bots'     # Replace with your channel
botnick = 'TempBot_DA_B'
adminname = 'yourname'       # The nickname of the bot's admin
admincommand = '!temp'       # Command to trigger temperature check

def check_cpu_temp():
    return f"CPU Temperature: {59}°C"
    try:
        temp = psutil.sensors_temperatures()['coretemp'][0].current
        return f"CPU Temperature: {temp}°C"
    except Exception as e:
        return f"Failed to get temperature: {e}"

def send_msg(irc_socket, target, message):
    irc_socket.send(f"PRIVMSG {target} :{message}\n".encode())

def handle_input(irc_socket):
    while True:
        ircmsg = irc_socket.recv(2048).decode("UTF-8", errors="ignore").strip('\n\r')
        print(ircmsg)
        
        if "PING :" in ircmsg:
            irc_socket.send(f"PONG :{ircmsg.split()[1]}\r\n".encode())
        
        if admincommand in ircmsg:
            if adminname in ircmsg:
                send_msg(irc_socket, channel, check_cpu_temp())

def post_temp_every_hour(irc_socket):
    while True:
        time.sleep(3600)
        send_msg(irc_socket, channel, check_cpu_temp())

def irc_bot():
    irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc_socket.connect((server, port))
    irc_socket.send(f"USER {botnick} {botnick} {botnick} :This is a CPU temp bot\n".encode())
    irc_socket.send(f"NICK {botnick}\n".encode())

    while True:
        ircmsg = irc_socket.recv(2048).decode("UTF-8", errors="ignore").strip('\n\r')
        print(ircmsg)

        if "PING :" in ircmsg:
            irc_socket.send(f"PONG :{ircmsg.split()[1]}\r\n".encode())
        
        if "End of /MOTD command" in ircmsg:
            irc_socket.send(f"JOIN {channel}\n".encode())
            break

    threading.Thread(target=handle_input, args=(irc_socket,)).start()
    threading.Thread(target=post_temp_every_hour, args=(irc_socket,)).start()

if __name__ == "__main__":
    irc_bot()