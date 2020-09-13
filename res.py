from colorama import Fore, Back, Style
from colorama import init
import socket
import getpass
from datetime import datetime
import platform

def perror(str,time):
    init()
    if time:
        print(f"{Fore.RED}{gettime()}[x] {str}")
    else:
        print(f"{Fore.RED}[x] {str}")

def pwarn(str,time):
    init()
    if time:
        print(f"{Fore.YELLOW}{gettime()}[!] {str}")
    else:
        print(f"{Fore.YELLOW}[!] {str}")

def pinfo(str,time):
    init()
    if time:
        print(f"{Fore.BLUE}{gettime()}[+] {str}")
    else:
        print(f"{Fore.BLUE}[+] {str}")

def psuccess(str,time):
    init()
    if time:
        print(f"{Fore.GREEN}{gettime()}[v] {str}")
    else:
        print(f"{Fore.GREEN}[v] {str}")

def get_pv_ip():
    return socket.gethostbyname_ex(socket.gethostname())[1:]

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
    return getpass.getuser()

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
    return str(platform.system())

def get_full_os_name():
    return str(platform.platform())

def get_python_version():
    return str(platform.python_version())

