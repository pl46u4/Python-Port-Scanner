import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()

print_lock = threading.Lock()

print(Fore.LIGHTRED_EX + "╔═══════════════╗")
print("║Made by Plague ║")
print("╚═══════════════╝")

ip = input("Enter the IP to scan: ")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.LIGHTWHITE_EX + f"[{port}]" + Fore.GREEN + "Opened")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(65535):
        executor.submit(scan, ip, port + 1)