from colorama import Fore, Back, Style
from colorama import init
import socket
from getpass import getpass, getuser
from datetime import datetime
from platform import system, platform, python_version
from os import getcwd, path

def perror(str,time=False):
    init()
    if time:
        print(f"{Fore.RED}{gettime()} [x] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.RED}[x] {str} {Fore.WHITE}")

def pwarn(str,time=False):
    init()
    if time:
        print(f"{Fore.YELLOW}{gettime()} [!] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.YELLOW}[!] {str} {Fore.WHITE}")

def pinfo(str,time=False):
    init()
    if time:
        print(f"{Fore.BLUE}{gettime()} [+] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.BLUE}[+] {str} {Fore.WHITE}")

def psuccess(str,time=False):
    init()
    if time:
        print(f"{Fore.GREEN}{gettime()} [v] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.GREEN}[v] {str} {Fore.WHITE}")

def get_pv_ip():
    ip = socket.gethostbyname_ex(socket.gethostname())[1:]
    if "127.0.1.1" in str(ip) or "127.0.1.1" in str(ip) or "127.0.1.1" in str(ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    else :
        return ip

def get_pb_ip():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("bot.whatismyipaddress.com",80))
    sock.send(b"GET / HTTP/1.1\nHost: bot.whatismyipaddress.com\n\n")
    ip = str(sock.recv(1024).decode("utf-8")).split("\n")[-1]
    sock.close()
    return ip

def gethostname():
    return socket.gethostname()

def getusername():
    return getuser()

def gettime():
    return str(datetime.now().strftime("%H:%M:%S"))

def getdate():
    return str(datetime.today()).split()[0]

def check_internet():
    try:
        socket.create_connection(("1.1.1.1", 53),2)
        return True
    except:
        return False


def is_available(website, port = None):
    if port !=None:
        try:
            socket.create_connection((website, port),2)
            return True
        except:
            return False
    else:
        try:
            socket.create_connection((website, 80),2)
            return True
        except:
            return False

def get_os_name():
    return str(system())

def get_full_os_name():
    return str(platform())

def get_python_version():
    return str(python_version())

def get_file_number_of_lines(fname):
    with open(f"{getcwd()}/{fname}") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_file_size(fname):
    byte = int(path.getsize(f"{getcwd()}/{fname}"))
    return f"{byte/1000000}Megabytes"



