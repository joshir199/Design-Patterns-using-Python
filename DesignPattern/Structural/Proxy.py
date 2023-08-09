"""
 Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources
 by being always up, even though you only need it from time to time.

Instead of creating the object when the app launches, you can delay the object’s initialization to a time when
 it’s really needed.

 Access control (protection proxy). This is when you want only specific clients to be able to use the service object

 Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.

 Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.
 Caching request results (caching proxy). This is when you need to cache results of client requests and
 manage the life cycle of this cache, especially if results are quite large.

Smart reference. This is when you need to be able to dismiss heavyweight object once there are no clients that use it.
 Facade is similar to Proxy in that both buffer a complex entity and initialize it on its own.
 Note: Unlike Facade, Proxy has the same interface as its service object, which makes them interchangeable.
"""

from abc import ABC, abstractmethod


class ServerInterface(ABC):

    @abstractmethod
    def execute_cmd(self, cmd):
        pass


class Server(ServerInterface):

    def execute_cmd(self, cmd):
        print(f'Server Command executed: {cmd}')


# Uses same interface as Real Server class uses
# It should have a field for storing a reference to the service. Usually, proxies create and
# manage the whole life cycle of their services.
# It's a wrapper called by the client to access the real underlying object
class ProxyServer(ServerInterface):

    def __init__(self, user):
        self.authorised = False
        self.executor = Server()
        if user == "admin":
            self.authorised = True

        self.commands = ["rm", "wr"]

    def execute_cmd(self, cmd):

        if self.authorised:
            print("user is authorised")
            self.executor.execute_cmd(cmd)
        else:
            print("user is not authorised")
            if cmd in self.commands:
                raise Exception(f'{cmd} is not allowed for this user')
            else:
                self.executor.execute_cmd(cmd)


def client_code(proxy : ProxyServer):
    try:
        proxy.execute_cmd("rm")
        proxy.execute_cmd("rd")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("admin request to Server")
    obj = ProxyServer("admin")
    client_code(obj)

    print("employee request to Server")
    anotherObj = ProxyServer("employee")
    client_code(anotherObj)

