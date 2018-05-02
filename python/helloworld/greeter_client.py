#  Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc
from google.protobuf import json_format as json_format


def run():
    channel = grpc.insecure_channel('localhost:8765')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    print("connected to channel")
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='Bala'))
    print("Greeter client received: " + str(response.id) + '  '+ response.name)

    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='Bkkk'))
    for item in response.data:
        print(item)

    # convert message to json format
    # message = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='BBBBKKKKKKK'))
    # json_string = json_format.MessageToJson(message)
    # print("json_string:: " + json_string)

    # # convert message to json format
    # message = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='Krishna'))
    # json_string = json_format.MessageToJson(message)
    # print("json_string:: " + json_string)
    # print("Greeter client received: " + str(message.id) + '  '+ message.name + ' ' + message.emplyee_code[1].name)
    #

if __name__ == '__main__':
    run()
