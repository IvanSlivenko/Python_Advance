# example 1 ( UDP server socket)
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(('127.0.0.1', 8888)) #-------------- Резервуємо порт 127.0.0.1
sock.bind(('', 8888)) #-------------- Резервуємо (відкриваємо всі ) порти
result = sock.recv(1024) #----------------- Приймаємо повідомлення
print('Message :', result.decode('utf-8'))#------------------- Декодуємо result
sock.close()#----------------------------------------- Звільняємо (закриваємо) порт



