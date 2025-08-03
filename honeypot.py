import socket,paramiko,threading

import os
from cryptography.fernet import Fernet
# Banner
from datetime import datetime
from colorama import init, Fore, Style

init()

banner = (
    "\033[38;5;205m"  # Start bright pink
    r"""
  _____                _____        ______  _____   ______         _____    ____   ____ 
 |\    \   _____   ___|\    \   ___|\     \|\    \ |\     \    ___|\    \  |    | |    |
 | |    | /    /| |    |\    \ |     \     \\\    \| \     \  /    /\    \ |    | |    |
 \/     / |    || |    | |    ||     ,_____/|\|    \  \     ||    |  |    ||    |_|    |
 /     /_  \   \/ |    |/____/ |     \--'\_|/ |     \  |    ||    |  |____||    .-.    |
|     // \  \   \ |    |\    \ |     /___/|   |      \ |    ||    |   ____ |    | |    |
|    |/   \ |    ||    | |    ||     \____|\  |    |\ \|    ||    |  |    ||    | |    |
|\ ___/\   \|   /||____| |____||____ '     /| |____||\_____/||\ ___\/    /||____| |____|
| |   | \______/ ||    | |    ||    /_____/ | |    |/ \|   ||| |   /____/ ||    | |    |
 \|___|/\ |    | ||____| |____||____|     | / |____|   |___|/ \|___|    | /|____| |____|
    \(   \|____|/   \(     )/    \( |_____|/    \(       )/     \( |____|/   \(     )/  
     '      )/       '     '      '    )/        '       '       '   )/       '     '
"""
    "\033[0m"  # Reset color
)

print(banner)

print(Fore.WHITE + "\n****************************************************************")
print("*  Copyright of wrench project, 2025                           *")
print(f"*  Loaded at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                *")
print("****************************************************************" + Style.RESET_ALL)
class SSH_server(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        print(f"{username}:{password}")
        return paramiko.AUTH_FAILED
    def check_auth_publickey(self, username, key):
       return paramiko.AUTH_FAILED
def handle_connection(client_sock,server_key):
        transport= paramiko.Transport(client_sock)
        transport.add_server_key(server_key)
        ssh=SSH_server()
        transport.start_server(server=ssh)
def main():
        server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server_sock.bind(('0.0.0.0',22))
        server_sock.listen(100)
        server_key=paramiko.RSAKey.generate(2048)
        while True:
            client_sock,client_addr=server_sock.accept()
            print (f"connection: {client_addr[0]}:{client_addr[1]}")
            t=threading.Thread(target=handle_connection,args=(client_sock,server_key))
            t.start()
if __name__=="__main__":
     main()  