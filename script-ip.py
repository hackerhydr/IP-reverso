import socket

print("=== DNS Reverso Tool ===")

ip = input("Digite o IP: ")

try:
    host = socket.gethostbyaddr(ip)
    print("\nResultado:", host[0])
except Exception as e:
    print("\nErro:", e)