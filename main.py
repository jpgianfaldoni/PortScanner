import socket

def portConnection(IP, port):
    try:
        print(f"Trying {IP}:{port}") 
        socket.setdefaulttimeout(0.5)
        s = socket.socket()
        s.connect((IP,port))
        x = s.recv(1024)
        s.close()
        return x
        
    except Exception as e:
        print(e)
        return None

initial_ip = input("Digite o ip inicial: Ex: 192.188.0.1: ")

try:
    socket.inet_aton(initial_ip)
except socket.error:
    print("Invalid initial IP")

final_ip = input("Digite o ip final: ")

try:
    socket.inet_aton(final_ip)
except socket.error:
    print("Invalid final IP")

initial_port = int(input("Digite a porta inicial: Ex 22: "))
final_port = int(input("Digite a porta final: "))


common_ip = initial_ip.split(".")
common_ip.remove(common_ip[-1])
common_ip = '.'.join(common_ip) + "."
init_ip_num = int(initial_ip.split(".")[-1])
final_ip_num = int(final_ip.split(".")[-1])
valid_ports = []


for port in range(initial_port, final_port):
    for i in range(init_ip_num, final_ip_num+1):
        ip = common_ip + str(i)
        port_check = portConnection(ip, port)
        if port_check is not None:
            valid_ports.append((f"IP: {ip}",f"Port: {port}" ))


print("Lista de IPs e portas abertas: \n")
print(valid_ports)