import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('127.0.0.1', 2222)) 
s.listen(1) 
while True:
        conn, addr = s.accept()
        while True:
                data = conn.recv(2222)
                if not data : break
                conn.send(data)
        conn.close()
