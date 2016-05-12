import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('0.0.0.0', 2222)) 
s.listen(1) 
while True:
        conn, addr = s.accept()
        while True:
                data = conn.recv(2222)
                if data == b'close'
                conn.send(data)
        conn.close()
