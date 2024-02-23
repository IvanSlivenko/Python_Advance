# example 1 ( UDP client socket)
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.sendto(b'Test message client', ('127.0.0.1', 8888)) #------------------ Відправляємо Message
sock.sendto(b'Test message client', ('localhost', 8888)) #------------------ Відправляємо Message на localhost
