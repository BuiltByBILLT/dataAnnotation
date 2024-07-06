import socket
import time
import psutil

# IRC configuration
SERVER = "irc.libera.chat"
PORT = 6667
CHANNEL = "#pytest-bots"
NICKNAME = "TestBot-DA"

# Function to get CPU temperature
def get_cpu_temp():
    return 69
    temps = psutil.sensors_temperatures()
    if 'coretemp' in temps:
        for core in temps['coretemp']:
            if 'Core 0' in core.label:
                return core.current
    return None

# IRC bot class
class IRCBot:
    def __init__(self, server, port, channel, nickname):
        self.server = server
        self.port = port
        self.channel = channel
        self.nickname = nickname
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.irc_socket.connect((self.server, self.port))
        self.send_command(f"NICK {self.nickname}")
        self.send_command(f"USER {self.nickname} {self.nickname} {self.nickname} :CPU Temp Bot")
        self.send_command(f"JOIN {self.channel}")

    def send_command(self, command):
        self.irc_socket.send((command + "\r\n").encode())

    def send_message(self, message):
        self.send_command(f"PRIVMSG {self.channel} :{message}")

    def run(self):
        self.connect()
        while True:
            temp = get_cpu_temp()
            if temp is not None:
                self.send_message(f"CPU temperature: {temp}°C")
                print("sent")
            time.sleep(3600)  # Sleep for 1 hour

if __name__ == "__main__":
    bot = IRCBot(SERVER, PORT, CHANNEL, NICKNAME)
    bot.run()