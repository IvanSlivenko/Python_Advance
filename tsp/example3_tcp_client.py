import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.106', 8888))
sock.send(b'Test message TCP')
sock.close()