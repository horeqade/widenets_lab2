import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user('user', '123', 'server', perm='elrafmw')
    authorizer.add_user('boss', '123', 'server', perm='elradfmwMT')
    authorizer.add_user('guest', '', 'server/guest', perm='elrafmw')
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('127.0.0.1', 2121)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
