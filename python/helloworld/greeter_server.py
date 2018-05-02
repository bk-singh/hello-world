
from concurrent import futures
import time

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    count = 0
    def SayHello(self, request, context):
        response = helloworld_pb2.HelloReply(name =  request.name)
        self.count = self.count + 1
        response.id = self.count
        return response

    def SayHelloAgain(self, request, context):
        DATA = []

        helloReplyData = helloworld_pb2.HelloReply(id=1)
        helloReplyData.name = "name from hello Reply Data"
        helloReplyData.emplyee_code[1].name = "name from employee code"
        helloReplyData.emplyee_code[1].status = 3
        DATA.append(helloReplyData)
        DATA.append(helloReplyData)
        DATA.append(helloReplyData)
        del DATA[2]

        helloData = helloworld_pb2.HelloList(data=DATA)

        return helloData


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:8765')
    server.start()
    print("server started..")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
