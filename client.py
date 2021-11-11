import socket


class Session:
    def __init__(self, host, port):
        print("Server connection {}:{}".format(host, port))
        self.sock = socket.socket()
        self.sock.bind(('localhost', 1000))
        self.sock.connect((host, port))

    def connect(self):
        while True:
            data = self.sock.recv(1024).decode()
            if data == "_error_":
                self.sock.close()
                return

            print(data)
            msg = input("Sending to server:")
            if msg == "":
                continue

            self.sock.send(msg.encode())
            if msg == "exit":
                self.sock.close()
                break


if __name__ == "__main__":
    session = Session('localhost', 9080)
    session.connect()